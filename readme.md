STM32 UART to FastAPI Web Monitor
Overview
This project showcases a real-time data monitoring system that captures data sent from an STM32F407G-DISC microcontroller via UART and displays it on a web interface using FastAPI. The system leverages WebSocket technology to provide live updates, making it ideal for learning about embedded systems, serial communication, and web-based data visualization. Designed as an educational project, it demonstrates the integration of hardware and software for IoT applications.
Features

Real-Time Data Display: View UART data from the STM32 microcontroller instantly on a web page.
WebSocket Integration: Ensures seamless, live updates of incoming data without manual refresh.
Simple Web Interface: Clean and user-friendly HTML-based dashboard for monitoring data with timestamps.
Lightweight Backend: Utilizes FastAPI for efficient and easy-to-learn API and WebSocket handling.
Educational Focus: Ideal for beginners to explore embedded systems and web development integration.

Prerequisites
To set up and run this project, ensure you have the following:
Hardware

STM32F407G-DISC microcontroller (or similar STM32 board with UART support).
USB-to-UART converter (e.g., ST-Link or FTDI) for serial communication with a computer.

Software

STM32CubeIDE or equivalent for programming the microcontroller.
Python 3.8 or higher for running the web server.
A modern web browser (e.g., Chrome, Firefox) to view the data.
Optional: Tera Term for initial UART communication testing.

Installation
Follow these steps to set up the project:

Clone the RepositoryDownload the project files from the GitHub repository to your local machine.

Set Up the Python EnvironmentCreate a virtual environment and install the required Python packages: FastAPI, Uvicorn, and PySerial. This ensures the web server and UART communication work seamlessly.

Configure the Microcontroller

Use STM32CubeIDE to program the STM32F407G-DISC.
Configure UART2 with a baud rate of 9600 for data transmission.
Flash the firmware to the microcontroller to start sending data (e.g., sample messages or sensor readings).

Set Up the Serial Port

Identify the serial port used by the STM32 (e.g., COM14 on Windows, /dev/ttyUSB0 on Linux).
Update the project configuration with the correct port and ensure the baud rate matches the microcontroller settings.

Usage

Start the Web ServerLaunch the FastAPI server to begin reading UART data and broadcasting it via WebSocket.

Access the Web InterfaceOpen a web browser and navigate to http://localhost:8000. The interface will display incoming UART data with timestamps in real-time.

Monitor DataAs the STM32 sends data (e.g., text messages or sensor values), the web page updates automatically, showing each message alongside its receipt time.

Project Structure
The project is organized as follows:

Web Server Files: Contains the FastAPI application and WebSocket logic for handling incoming data.
UART Monitoring: Manages serial port communication to read data from the STM32.
Web Interface: A simple HTML template for displaying data in a clean, scrollable list.
Microcontroller Firmware: Example firmware for the STM32 to send UART data (provided for reference).

Troubleshooting

Serial Port Issues: Ensure the correct serial port is selected and no other application is using it.
No Data Displayed: Confirm the STM32 is transmitting data and the baud rate matches the server configuration.
WebSocket Disconnection: The web interface automatically attempts to reconnect every 2 seconds if the connection is lost.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

FastAPI: For providing a lightweight and powerful framework for building APIs and WebSocket servers.
STM32CubeIDE: For enabling easy firmware development for the STM32 microcontroller.
Community: Inspired by open-source IoT and embedded systems projects.
