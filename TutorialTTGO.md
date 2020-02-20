# TT-GO T-DISPLAY ESP32 LCD

[Producto comprado](https://es.aliexpress.com/item/4000296985840.html)

[Producto original](https://es.aliexpress.com/item/33048962331.html)

[Producto en tindie](https://www.tindie.com/products/ttgo/lilygor-ttgo-t-display-esp32-wifibluetooth-module/)

![pinout](https://ae01.alicdn.com/kf/H55f08657882b4f57a8143687eed0ed25j.jpg)


![pinout original](https://ae01.alicdn.com/kf/H39c2130da52e43e7ac7ccee871075b46E.jpg)


[Esquema](https://github.com/Xinyuan-LilyGO/TTGO-T-Display/blob/master/schematic/ESP32-TFT(6-26).pdf)

QSPI flash, 4 MB
SRAM	SRAM de 520 kB

[Github](https://github.com/Xinyuan-LilyGO/TTGO-T-Display)

![](https://ae01.alicdn.com/kf/HTB1Dif0XND1gK0jSZFKq6AJrVXas.jpg)

[Modulo para la pantalla](https://github.com/devbis/st7789py_mpy)

[micropython psRAM logo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/issues/310)

## Medida del voltaje de la bateria
### Ejemplo C++

#define TFT_BL          4  // Display backlight control pin
#define ADC_EN          14
#define ADC_PIN         34
#define BUTTON_1        35
#define BUTTON_2        0

int vref = 1100;

uint16_t v = analogRead(ADC_PIN);
float battery_voltage = ((float)v / 4095.0) * 2.0 * 3.3 * (vref / 1000.0);

### Ejemplo en micropython
```python
import machine

def batLevel():
    adcBat = machine.ADC(machine.Pin(34))
    adcBat.atten(machine.ADC.ATTN_11DB) # rango de 3.6V
    adcBat.width(machine.ADC.WIDTH_12BIT)
    adcValue = adcBat.read()
    voltBat = adcValue /4095 *  3.3 * 1100 / 1000
    percentBat = voltBat*100/4.2
    print('%1.2fv - %d%%'%(voltBat,percentBat))
    return percentBat
```

# TTGO ESP32 (OLED + 18650)

![](http://forums.4fips.com/2018/4fips.com_esp32_ttgo_oled_lcd_18650_wifi_bluetooth_module.jpg)

[Instalacion](https://forums.4fips.com/viewtopic.php?f=3&t=6905)