# Test I2C Communication
Use the below script check if the Pico WH detects the OLED. If the wiring is correct it wil return [60] or [0x3c].
run this iside the thonny shell:
```python
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
print(i2c.scan())
```
this will return [60] or [0x3c]. if it returns empty [] then check the wiring angin.

# Test OLED Display with a test script
in thonny create and run a new file and copy paste the below code, save it to the rpi /main.py.
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("Hello", 0, 0)
oled.contrast(255)
oled.show()
print("Display test successful")
```
