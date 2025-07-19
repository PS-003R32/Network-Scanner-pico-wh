# Scanning Networks using Raspberry Pi pico WH <br>
The pico wh has 2 wi-fi modes: station mode (STA) and access point mode(AP). We will use the STA mode to scan for available networks<br>
and display the signal strength in percentage (0-100) in the ssd1306 OLED module. You can buy the display of Amazon [Ds Robotics® 0.96 
Inch OLED Module 12864 128x64 Driver IICI2C Serial Self-Luminous Display Board Compatible with Arduino Raspberry PI (1 Piece)](https://www.amazon.in/Ds-Robotics%C2%AE-Self-Luminous-Compatible-Raspberry/dp/B0BWNHXYN9) this one worked for me.<br>

<img width="576" height="352" alt="image" src="https://github.com/user-attachments/assets/bc2eaeaf-67c3-4b0f-992b-5c9858795191" /><br>

<img width="428" height="172" alt="image" src="https://github.com/user-attachments/assets/7fef6fa2-0326-442c-b223-8a20b9328154" /><br>

<img width="303" height="267" alt="image" src="https://github.com/user-attachments/assets/70182122-3b86-4eed-8fda-9d9983074694" />


# Setting up Thony<br>
Press Hold the BOOTSEL button on the rpi and connect the usb with your pc and open Thony, your rpi should show up in the files window.<br>
If the raspberry pi pico wh doesnt show in the files window, go to Run > Configure Interpreter. Select the options as shown in the image.<br>


<img width="285" height="335" alt="image" src="https://github.com/user-attachments/assets/c15315a2-2ef7-4850-8f18-93ff4b1437b2" /><br>

<img width="450" height="358" alt="image" src="https://github.com/user-attachments/assets/b452facc-963f-446c-883f-a888c6158c39" /><br>


Install the necessary drivers for running the ssd1306 OLED module by going to Tools > Manage packages...<br>

<img width="682" height="287" alt="image" src="https://github.com/user-attachments/assets/b732e73a-aac1-413e-904b-cd74a55820bc" /><br>


Search for ssd1306 and install.<br>
<img width="835" height="607" alt="image" src="https://github.com/user-attachments/assets/d721db7c-fb6d-4286-876f-e326fb5fda2f" /><br>

If you dont find any, use the drivers i have in this repository. Save the drivers inside the lib/ directory by creating one.<br>

# Circuit Diagram<br>
After setting up thony, the next stpe is to connect the OLED display to the pico. We will need 4 male  to male jumper wires and <br>
a bread board. Connect the following using jumper wires:<br>

|---Raspberry Pi Pico WH-------|------SSD1306 OLED------|<br>
|------------------------------|------------------------|<br>
|VBUS (Pin 40) or 3V3 (Pin 36)-|----------VCC-----------|<br>
|GND (Pin 38)------------------|----------GND-----------|<br>
|GP4 (Pin 26)------------------|----------SDA (data)----|<br>
|GP5 (Pin 27)------------------|----------SCL (clock)---|<br>

# Theres a complete debug guide if your display is not working/turning on in a seperate section in this repository.<br>

# The Coding<br>

We will use MicroPython modules for this project. the script is available in this repository aswell. save the file with name "main.py"<br>
in the rpi at /main.py.<br>

<img width="567" height="386" alt="image" src="https://github.com/user-attachments/assets/780e786d-83bd-4d1d-a5e5-e492451c37ef" /><br>

You can run and test if your circuit is working by running the script (without disconnecting it with your pc).if everything is correct the 
cmd line will show no errors and usually displays "MPY: soft reboot". After setting everything up you can disconnect the rpi from your pc 
and connect to a power source. Your network scanner is ready. ;)
