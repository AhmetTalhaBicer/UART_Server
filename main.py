import asyncio
import uvicorn
from server import app
from uart_monitor import start_uart_monitor

if __name__ == "__main__":
    # Start the UART monitor in a background task
    asyncio.run(start_uart_monitor())
    
    # Start the web server
    print("Starting UART Server")
    print("Open http://localhost:8000 in your browser")
    uvicorn.run(app, host="0.0.0.0", port=8000)