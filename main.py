import time

import pyautogui as pyautogui
import serial
ser = serial.Serial(port='COM14', baudrate=9600)
time.sleep(3)
previousMode = "none"
mode = "none"

while True:
    if ser.readable():
        res = ser.readline()
        if "\\r\\n'" in str(res):
            try:
                serial_input = str(res).replace("b'", "").replace("\\r\\n'", "").split("\\t")

                rotate = float(serial_input[0])
                frontBack = float(serial_input[1])
                leftRight = float(serial_input[2])

                if frontBack < -30:
                    if frontBack < -70:
                        mode = "none"
                    else:
                        mode = "left"
                elif frontBack > 20:
                    if frontBack > 70:
                        mode = "none"
                    else:
                        mode = "right"
                else:
                    mode = "none"

                if mode == "none" and previousMode != "none":
                    previousMode = "none"

                    pyautogui.mouseUp()
                    pyautogui.mouseUp(button="right")
                if mode == "left" and previousMode != "left":
                    previousMode = "left"

                    pyautogui.mouseUp(button="right")
                    pyautogui.mouseDown()
                if mode == "right" and previousMode != "right":
                    previousMode = "right"

                    pyautogui.mouseUp()
                    pyautogui.mouseDown(button="right")

                print(str(frontBack) + " : " + str(rotate) + " : " + str(leftRight))
            except:
                print("error")
