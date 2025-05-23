from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import os
import json
from typing import List

# Initialize FastAPI
app = FastAPI(title="STM32 UART Monitor")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Store active WebSocket connections
active_connections: List[WebSocket] = []

@app.get("/")
async def get_index(request: Request):
    """Serve the main HTML page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handle WebSocket connections"""
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        # Send stored messages to the new client
        from uart_monitor import get_stored_messages
        for msg in get_stored_messages():
            await websocket.send_text(json.dumps(msg))
        
        # Keep the connection open
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)

async def broadcast_message(message: str):
    """Send a message to all connected clients"""
    for connection in active_connections:
        try:
            await connection.send_text(message)
        except:
            # Remove dead connections
            if connection in active_connections:
                active_connections.remove(connection)