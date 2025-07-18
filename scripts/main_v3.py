import network
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=200000)
oled = SSD1306_I2C(128, 64, i2c)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while True:
    scan_list = wlan.scan()
    networks = {}
    for net in scan_list:
        ssid = net[0].decode()
        rssi = net[3]

        if ssid not in networks:
            networks[ssid] = rssi

    network_list = list(networks.items())

    oled.fill(0)
    oled.text("Networks in range:", 0, 0)
    max_lines = 4
    for i, (ssid, rssi) in enumerate(network_list[:max_lines]):
        strength = 100 + rssi if rssi < 0 else rssi
        oled.text(ssid[:10], 0, (i + 1) * 14)
        oled.text(str(strength), 100, (i + 1) * 14)
    oled.show()
    time.sleep(2)
