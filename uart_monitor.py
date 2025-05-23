import asyncio
import serial
import datetime
import json
from server import broadcast_message

# Serial port configuration
SERIAL_PORT = "COM14"  # Change to match your STM32 UART port
BAUD_RATE = 9600      # Match the baud rate in your STM32 code

# Store recent messages
messages = []

def get_stored_messages():
    """Return the stored messages"""
    return messages

async def start_uart_monitor():
    """Start monitoring the UART port in a background task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(_uart_reader())
    return task

async def _uart_reader():
    """Read from UART and broadcast messages"""
    print(f"Attempting to connect to {SERIAL_PORT} at {BAUD_RATE} baud...")
    
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Successfully connected to {SERIAL_PORT}")
        
        while True:
            try:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        # Create message object
                        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                        message = {"text": line, "time": timestamp}
                        messages.append(message)
                        print(f"[{timestamp}] Received: {line}")
                        
                        # Broadcast to all connected clients
                        await broadcast_message(json.dumps(message))
                        
                        # Limit stored messages
                        if len(messages) > 100:
                            messages.pop(0)
                
                await asyncio.sleep(0.01)
            except Exception as e:
                print(f"Error reading UART: {e}")
                await asyncio.sleep(1)
    except serial.SerialException as e:
        print(f"Could not open serial port {SERIAL_PORT}: {e}")
        print("Server running, but UART connection failed. Check your device connection.")