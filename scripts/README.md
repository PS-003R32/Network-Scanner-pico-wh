Rename the script to main.py and save it to the rpi at /main.py

## 🖥️ OLED Display Visualization

After running `main_v3.py`, the Raspberry Pi Pico WH will scan Wi-Fi networks and display real-time signal strength (updated every 2 seconds) on an SSD1306 OLED screen.

### 📷 Example Screenshots:

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc2eaeaf-67c3-4b0f-992b-5c9858795191" width="480" alt="Wi-Fi Scan Result">
  <br><img src="https://github.com/user-attachments/assets/70182122-3b86-4eed-8fda-9d9983074694" width="480" alt="Signal Strength OLED">
</p>

### 📐 Display Details:
- Shows up to **4 active networks**
- SSID truncated to **first 10 characters**
- Signal strength estimated from **RSSI**
- Refreshed every **2 seconds** for updated visibility (you can change this for a different refresh time)
