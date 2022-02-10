import socket
import signal
import time
import pyautogui


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# 0 is Halo
# 1 is Minecraft
# 2 is COD
# 3 is Oregon Trail
choice = 1

time.sleep(5)
print("starting")

counter = 3


print("Listening on port: " + str(UDP_PORT))
try:
    while True:
        data, addr = sock.recvfrom(32000) # buffer size is 1024 bytes

        cleanedMessage = data[419:424].decode('UTF-8')
        print("received message: %s" % str(cleanedMessage))

        if data != None:

            if choice == 0 and str(cleanedMessage) =='Key_F':
                # Halo Macro
                pyautogui.keyDown('w')
                time.sleep(1)
                pyautogui.keyDown(']')
                time.sleep(1)
                pyautogui.keyUp(']')
                time.sleep(3)
                pyautogui.keyDown('space')
                pyautogui.keyUp('space')
                pyautogui.keyDown('[')
                time.sleep(3)
                pyautogui.keyUp('[')
                pyautogui.keyUp('w')

            elif choice == 1 and str(cleanedMessage) =='Key_J':
                # Minecraft Macro - Aim Left
                # pyautogui.hotkey('alt', 'tab')
                # pyautogui.typewrite(['esc'])
                # look left
                time.sleep(1)
                pyautogui.keyDown('j')
                if counter == 0:
                    time.sleep(0.8)
                    counter += 1
                else:
                    time.sleep(0.9)
                    counter += 1

                pyautogui.keyUp('j')
                time.sleep(2)

            elif choice == 1 and str(cleanedMessage) == 'Key_L':
                # look right
                time.sleep(1)
                pyautogui.keyDown('l')
                if counter == 1:
                    time.sleep(0.8)
                    counter += 1
                else:
                    time.sleep(0.9)
                    counter += 1

                pyautogui.keyUp('l')
                time.sleep(2)
                counter += 1

            elif choice == 1 and str(cleanedMessage) == 'Key_F':
                # Fire!
                time.sleep(1)
                pyautogui.keyDown('e')
                time.sleep(2)
                pyautogui.keyUp('e')
                time.sleep(1)
                pyautogui.typewrite(['e'])
                time.sleep(1)

            elif choice == 1 and str(cleanedMessage) == 'Key_I':
                # look up
                time.sleep(1)
                pyautogui.keyDown('i')
                time.sleep(0.22)
                pyautogui.keyUp('i')
                time.sleep(2)

            elif choice == 2 and str(cleanedMessage) == 'Key_F':
                pyautogui.mouseDown(button='right')
                pyautogui.mouseDown(button='left')
                time.sleep(3)
                pyautogui.mouseUp(button='right')
                pyautogui.mouseUp(button='left')

            elif choice == 3:
                # Oregon Trail, simple keystroke
                # F == enter
                pyautogui.typewrite([str(cleanedMessage)[-1], 'enter'], interval=1)


            date = None
except Exception as e:
    print(e)
