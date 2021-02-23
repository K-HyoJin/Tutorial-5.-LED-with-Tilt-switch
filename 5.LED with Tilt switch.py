from pyfirmata import Arduino,util
import time

#핀 모드 세팅
board = Arduino('COM8')

digital_input = board.get_pin('d:2:i') # 2번핀 입력
led = board.get_pin('d:13:o') # 13번핀 출력

it = util.Iterator(board) # 회로의 입력상태를 읽어올 변수선언
it.start()

while True:
    input_value = digital_input.read()
    print(input_value)
    for i in range(1):
        if input_value is None:
            time.sleep(3)
            break
        if input_value is True:
            led.write(1)
        else:
            led.write(0)
            


