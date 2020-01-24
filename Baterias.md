




Har'ia este https://diyprojects.io/test-shield-battery-lipo-wemos-d1-mini-voltage-measurement-level-charge/#.Xe_c7B-E6Hs

Ejemplo sencillo https://arduinodiy.wordpress.com/2016/12/25/monitoring-lipo-battery-voltage-with-wemos-d1-minibattery-shield-and-thingspeak/ 

muy cientifico https://ezcontents.org/esp8266-battery-level-meter

Sobre esp32 https://forum.arduino.cc/index.php?topic=595924.0 


## [Shield v1.2](https://wiki.wemos.cc/products:d1_mini_shields:battery_shield)

[Producto](Shield v1.2 https://www.banggood.com/3pcs-Wemos-Battery-Shield-V1_2_0-For-Wemos-D1-Mini-Single-Lithium-Battery-Charging-Boost-Module-p-1293010.html)

![](https://imgaz.staticbg.com/images/oaupload/banggood/images/2C/A9/40c349b7-35ed-4747-9203-faf3bd94631b.jpg.webp)

![](https://imgaz.staticbg.com/images/oaupload/banggood/images/44/AE/562f8665-bc67-4dd4-b9aa-07371f23de0f.jpg)

![](https://imgaz.staticbg.com/images/oaupload/banggood/images/8F/CF/9f72a165-7c5e-4787-b3b6-ece5daa0959b.jpg.webp)

![](https://imgaz.staticbg.com/images/oaupload/banggood/images/1C/3D/a53b414b-8598-4daf-b7ad-15a270f5dabb.jpg)

El jumper J2 nos permite medir el voltaje de la batería (con una resistencia de 130kOhmios en serie)

[Ejemplo](https://diyprojects.io/test-shield-battery-lipo-wemos-d1-mini-voltage-measurement-level-charge/#.Xh7Y0d-E6Ht
)


```python
import machine

adc = machine.ADC(0)

def getBatteryVoltage():
 vRaw = adc.read()
 volt = map (vRaw,min,max,0, )
 return volt


def getBatteryLevel():
 vRaw = adc.read()
 volt = map (vRaw,min,max,0,100)
 return volt
```

```python
import time
import machine 
import pcd8544_test  
pcd8544_test.init()
pcd8544_test.initFB()

adc = machine.ADC(0) 

pcd8544_test.showText(0,0,'Midiendo')
time.sleep(1)
pcd8544_test.clear() 
N = 50
while True:
    media = 0
    for i in range(0,N):
        value = adc.read()
        media += value*1.0
        time.sleep(0.1)
    value = media/N
    print(value)
    pcd8544_test.clear()
    pcd8544_test.showText(0,0,str(value))  
```

|ADC|Voltaje
|---|---
|909|3,88
|912|3,89
|914|3,90
|916|3,91
|919|3,92
|921|3,93
|923|3,94

## ADC(1) ¿para medir el voltaje de la laimentación de 3.3v?

https://github.com/micropython/micropython/issues/2352
Parece que si medimos esto no podemos usar ADC(0) https://nodemcu.readthedocs.io/en/dev/modules/adc/#adcforce_init_mode https://bbs.espressif.com/viewtopic.php?t=827

