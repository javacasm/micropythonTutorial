# LCD_I2C
# Usa la libreria https://github.com/dhylands/python_lcd
# Para I2C hay que subir los ficheros esp8266_i2c_lcd.py y lcd_api.py
# https://github.com/dhylands/python_lcd/blob/master/lcd/esp8266_i2c_lcd_test.py



from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4),freq=400000) # SCL = D1 SDA D2 
lcd = I2cLcd(i2c, 63, 2, 16)
lcd.putstr("It Works!\nSecond Line")

sleep_ms(3000)
lcd.clear()
count = 0
while True:
    lcd.move_to(0, 0)
    lcd.putstr("%7d" % (ticks_ms() // 1000))
    sleep_ms(1000)
    count += 1
    if count % 10 == 3:
        print("Turning backlight off")
        lcd.backlight_off()
    if count % 10 == 4:
        print("Turning backlight on")
        lcd.backlight_on()
    if count % 10 == 5:
        print("Turning display off")
        lcd.display_off()
    if count % 10 == 6:
        print("Turning display on")
        lcd.display_on()
    if count % 10 == 7:
        print("Turning display & backlight off")
        lcd.backlight_off()
        lcd.display_off()
    if count % 10 == 8:
        print("Turning display & backlight on")
        lcd.backlight_on()
        lcd.display_on()
