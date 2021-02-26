# Arudino example 5
Tutorial 5.LED with Tilt switch\
Tilt switch sensor를 사용하여 기울기에 따라 LED에 불이 들어오도록 제작

## circuit
LED : digital 13pin \
Tilt switch sensor : digital 2pin\
<img src="https://user-images.githubusercontent.com/79436159/108855988-ece4fa80-762c-11eb-8e02-0b1841811361.png" width="500">

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` analog_input = board.get_pin('d:2:i')``` \
  -> 2번핀을 digital신호 입력핀으로 설정\
  ```led = board.get_pin('d:13:o') ```\
  -> 13번 핀을 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 
 
 ``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

```input_value = digital_input.read()```\
 sensor와 연결된 2번핀의 입력을 읽어와서 변수 input_value에 저장

```\
for i in range(1):
  if input_value is None: 
   time.sleep(3)
   break  
``` 
입력으로 들어온 input_value값이 None이면 지연시키고 for문에서 빠져나옴

```\
  if input_value is True:
    led.write(1)
  else:
   led.write(0)           
```
입력으로 들어온 input_value값이 ture이면 led가 켜지도록 1을 입력으로 주고\
아니면 led가 꺼지도록 0을 입력으로 줌
