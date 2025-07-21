# 📶 Scanning Networks with Raspberry Pi Pico WH

Harness the power of **Raspberry Pi Pico WH** and MicroPython to scan Wi-Fi networks in **station mode (STA)** and display signal strength on a sleek **SSD1306 OLED screen**.

---

## 🔧 What You'll Need

- Raspberry Pi Pico WH  
- SSD1306 OLED Module (Amazon link: [Ds Robotics® 0.96" OLED Display](https://www.amazon.in/Ds-Robotics%C2%AE-Self-Luminous-Compatible-Raspberry/dp/B0BWNHXYN9))  
- Breadboard & Jumper Wires  
- Thonny IDE  
- MicroPython drivers (preloaded or installable)

---

## 🖥️ Display Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc2eaeaf-67c3-4b0f-992b-5c9858795191" alt="OLED Display Network Scan" width="500">
  <br><img src="https://github.com/user-attachments/assets/7fef6fa2-0326-442c-b223-8a20b9328154" alt="Signal Strength" width="400">
  <br><img src="https://github.com/user-attachments/assets/70182122-3b86-4eed-8fda-9d9983074694" alt="OLED Scan Result" width="300">
</p>

---

## 🛠️ Setting Up Thonny & Your Pico WH

1. **Connect the Pico WH:**
   - Press and hold `BOOTSEL`, connect USB to PC, launch Thonny.
2. **Configure the Interpreter:**
   - Go to `Run > Configure Interpreter`.
   - Select correct interpreter settings (see image below).

<p align="center">
  <img src="https://github.com/user-attachments/assets/c15315a2-2ef7-4850-8f18-93ff4b1437b2" alt="Thonny Config" width="280">
  <br><img src="https://github.com/user-attachments/assets/b452facc-963f-446c-883f-a888c6158c39" alt="Interpreter Setup" width="360">
</p>

---

## 📦 Installing SSD1306 Drivers

- Open Thonny, go to `Tools > Manage packages...`  
- Search and install `ssd1306` module.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b732e73a-aac1-413e-904b-cd74a55820bc" alt="Package Manager" width="680">
  <br><img src="https://github.com/user-attachments/assets/d721db7c-fb6d-4286-876f-e326fb5fda2f" alt="Search SSD1306" width="830">
</p>

> If unavailable, use the provided driver files in `/lib/` directory of this repository.

---

## 🔌 Circuit Diagram

Connect your OLED as follows:

| Raspberry Pi Pico WH         | SSD1306 OLED       |
|------------------------------|--------------------|
| VBUS (Pin 40) or 3V3 (Pin 36) | VCC                |
| GND (Pin 38)                 | GND                |
| GP4 (Pin 26)                 | SDA (Data Line)    |
| GP5 (Pin 27)                 | SCL (Clock Line)   |

> Full debug guide available in the dedicated **troubleshooting section** if your display doesn’t turn on.

---

## 💡 Coding the Network Scanner

- Script: `main.py` (available in this repo)  
- Save to your device as `/main.py`

<p align="center">
  <img src="https://github.com/user-attachments/assets/780e786d-83bd-4d1d-a5e5-e492451c37ef" alt="Running Script" width="560">
</p>

Run and verify using Thonny. If it prints `"MPY: soft reboot"`, everything is good to go! Disconnect and power the board externally.

---

## ✅ Project Outcome

- Scan and list available Wi-Fi networks  
- Display signal strengths (0–100%)  
- Run independently without PC after setup

---

## 📂 Directory Structure
📁 Network-Scanner-pico-wh/ ├── main.py └── lib/ └── ssd1306.py


---

## 📬 Feedback & Collaboration

Maintained by [PS-003R32](https://github.com/PS-003R32).  
Feel free to open Issues or Pull Requests for suggestions or improvements!

---

## 🧾 License

MIT – Use it freely. Share, remix, and build your own versions.


