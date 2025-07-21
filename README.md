#  Network scanner using Raspberry Pi Pico WH

The **Raspberry Pi Pico WH** has two wifi modes: station mode (**STA**) and access point(**AP**) mode. we will use the **STA** mode to detect and display available networks.
Make a simple wifi scanner usinfg raspberry pi pico wh and MicroPython to scan Wi-Fi networks in **station mode (STA)** and display signal strength on a small **SSD1306 OLED screen**.

---

##  Requirements

- Raspberry Pi Pico WH  
- SSD1306 OLED Module (Amazon link: [Ds Robotics® 0.96" OLED Display](https://www.amazon.in/Ds-Robotics%C2%AE-Self-Luminous-Compatible-Raspberry/dp/B0BWNHXYN9))  
- Breadboard & Jumper Wires  
- Thonny IDE  
- MicroPython drivers (preloaded or installable)

---
---

##  Display Outputs

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec9098a7-39b5-4efd-b19a-5d50d4dd376e" alt="OLED Display Network Scan" width="500">
  <br><img src="https://github.com/user-attachments/assets/7fef6fa2-0326-442c-b223-8a20b9328154" alt="Signal Strength" width="400">
  <br><img src="https://github.com/user-attachments/assets/70182122-3b86-4eed-8fda-9d9983074694" alt="OLED Scan Result" width="300">
</p>

---

##  Setting Up Thonny & Pico WH

1. **Connecting the Pico WH:**
   - Press and hold `BOOTSEL` button on the board, connect USB to PC and launch `Thonny`.
2. **Files window**
   -If the files window is not there, go to `View` then click 'Files`.
3. **Configure the Interpreter:**
   - Go to `Run > Configure Interpreter`.
   - Set the  interpreter settings (follow image below).

<p align="center">
  <img src="https://github.com/user-attachments/assets/c15315a2-2ef7-4850-8f18-93ff4b1437b2" alt="Thonny Config" width="260">
  <br><img src="https://github.com/user-attachments/assets/b452facc-963f-446c-883f-a888c6158c39" alt="Interpreter Setup" width="360">
</p>

---

##  Installing SSD1306 Drivers

- Open Thonny, go to `Tools > Manage packages...`  
- Search and install `ssd1306` module.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b732e73a-aac1-413e-904b-cd74a55820bc" alt="Package Manager" width="680">
  <br><img src="https://github.com/user-attachments/assets/d721db7c-fb6d-4286-876f-e326fb5fda2f" alt="Search SSD1306" width="680">
</p>

> If unavailable, use the drivers i have in the files in `/lib/` directory of this repository.
> If the display is not working or turming on, there's a complete troubleshooting guide to solve or test the display insid Thonny.

---

##  Circuit Pin Diagram

Connect your OLED to the pico as follows:

| Raspberry Pi Pico WH         | SSD1306 OLED       |
|------------------------------|--------------------|
| VBUS (Pin 40) or 3V3 (Pin 36) | VCC                |
| GND (Pin 38)                 | GND                |
| GP4 (Pin 26)                 | SDA (Data Line)    |
| GP5 (Pin 27)                 | SCL (Clock Line)   |

> I have uploaded a full debug guide in the **troubleshooting section** if your display is no t turning on.

---

##  Coding

- Script: `main.py` (available in this repo)  
- Save it to the pico in `/main.py` directory.

<p align="center">
  <img src="https://github.com/user-attachments/assets/780e786d-83bd-4d1d-a5e5-e492451c37ef" alt="Running Script" width="560">
</p>

Run and verify using Thonny. If it prints `"MPY: soft reboot"`, everything is good to go! Disconnect and power the board externally. (It should run automatically.)

---

##  Directory
-save in the foplloeing paths only:
1. -pico/main.py
2. -pico/lib/ssd1306.py


---

##  Collaboration

Maintained by [PS-003R32](https://github.com/PS-003R32).  
You can open Issues or Pull Requests for suggestions or improvements! ;)

---
