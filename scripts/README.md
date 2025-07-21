Rename the script to main.py and save it to the rpi at /main.py

## 🖥️ OLED Display Visualization

After running `main_v3.py`, the Raspberry Pi Pico WH will scan Wi-Fi networks and display real-time signal strength (updated every 2 seconds) on an SSD1306 OLED screen.

### 📷 OLED Output Overview

<p align="center">
  <img src="https://github.com/user-attachments/assets/60a652cb-c669-4f31-bbd6-415b1d41bad0" width="640" alt="OLED Display showing Wi-Fi Scan Results">
</p>


### 🎥 Demo Video

<p align="center">
  <a href="https://www.youtube.com/watch?v=ZatuagblglM" target="_blank">
    <img src="https://github.com/user-attachments/assets/60a652cb-c669-4f31-bbd6-415b1d41bad0" width="640" alt="Watch demo video">
    <br>🔗 Click to watch the demo video...;)
  </a>
</p>


### 📐 Display Details:
- Shows up to **4 active networks**
- SSID truncated to **first 10 characters**
- Signal strength estimated from **RSSI**
- Refreshed every **2 seconds** for updated visibility (you can change this for a different refresh time)
