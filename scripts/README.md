Rename the script to main.py and save it to the rpi at /main.py
You can modify the code to display your own customized output on the oled.
Open to improvements and collaboration.

##  OLED Display Demonstration

After running `main_v3.py`, the Raspberry Pi Pico WH will scan Wi-Fi networks and display real-time signal strength (updated every 2 seconds) on an SSD1306 OLED screen.

###  OLED Output Photos:

<p align="center">
  <img width="336" height="290" alt="image" src="https://github.com/user-attachments/assets/ec9098a7-39b5-4efd-b19a-5d50d4dd376e" />

</p>


###  Demo Video:

<p align="center">
  <a href="https://www.youtube.com/watch?v=ZatuagblglM" target="_blank">
<img width="336" height="290" alt="image" src="https://github.com/user-attachments/assets/ec9098a7-39b5-4efd-b19a-5d50d4dd376e" />
    <br>🔗 Click to watch the demo video  ;)
  </a>
</p>


###  Display Details:
- Shows up to **4 active networks**
- SSID truncated to **first 10 characters** (you can change this if your display is larger.)
- Signal strength estimated from **RSSI**
- Refreshed every **2 seconds** for updated visibility (you can change this for a different refresh time)
