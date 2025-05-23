Certainly! Here's the improved and more visually appealing version of your `README.md` in English, with better formatting and structure:

---

# 📡 STM32 UART to FastAPI Web Monitor

**Live monitor your embedded system data via a modern web interface.**

This project demonstrates a real-time data monitoring system where data transmitted from an **STM32F407G-DISC** microcontroller via **UART** is displayed on a live dashboard built with **FastAPI** and **WebSockets**. It is designed as an educational resource to bridge the gap between embedded hardware and modern web technologies.

---

## ✨ Features

- 🔄 **Real-Time Data Display**
  Instantly view incoming UART data from the STM32 on a web interface.

- 🔌 **WebSocket Integration**
  Live updates without refreshing the page.

- 🖥️ **Simple and Clean UI**
  A minimalist HTML-based interface with timestamped data entries.

- ⚡ **Lightweight FastAPI Backend**
  Easy-to-learn, high-performance API with WebSocket support.

- 🎓 **Educational Project**
  Perfect for beginners exploring embedded systems and web development integration.

---

## 📦 Prerequisites

### 🔧 Hardware

- STM32F407G-DISC microcontroller (or any STM32 board with UART).
- USB-to-UART converter (e.g., ST-Link, FTDI, or PL2303).

### 💻 Software

- STM32CubeIDE (or equivalent) for microcontroller programming.
- Python 3.8+ environment.
- A modern web browser (Chrome, Firefox, etc.).
- (Optional) Tera Term or PuTTY for UART testing.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AhmetTalhaBicer/UART_Server.git
cd UART_Server
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Required packages:

- `fastapi`
- `uvicorn`
- `pyserial`

### 3. Program the STM32

- Open STM32CubeIDE.
- Configure **UART2** with a baud rate of **9600**.
- Upload the provided firmware or your custom code to send UART data (e.g., `"Temp: 24.5C"`).

### 4. Configure the Serial Port

Update `config.py` or the corresponding section of the server code:

```python
SERIAL_PORT = "/dev/ttyUSB0"  # or COMX on Windows
BAUD_RATE = 9600
```

---

## 🧪 Usage

### 1. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 2. Open the Web Dashboard

Navigate to: [http://localhost:8000](http://localhost:8000)

You’ll see a real-time feed of UART messages, each with a timestamp.

---

## 📁 Project Structure

```bash
UART_Server/
│
├── main.py           # Entry point, starts the server
├── uart_monitor.py   # UART reading functionality
├── server.py         # FastAPI server definitions
├── templates/        # HTML templates
│   └── index.html    # Web interface
├── requirements.txt  # Dependencies
├── LICENSE           # MIT License
└── .gitignore        # Git ignore file
```

---

## 🛠️ Troubleshooting

- **Serial Port Not Found**
  Ensure the correct port is selected and not used by another app.

- **No Data Displayed**
  Check if STM32 is sending data and the baud rate matches.

- **WebSocket Disconnection**
  The web client attempts to reconnect every 2 seconds automatically.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FastAPI** – Modern and fast web framework.
- **STM32CubeIDE** – Great tool for STM32 firmware development.
- **The Open-Source Community** – Inspiration from countless IoT and embedded projects.
