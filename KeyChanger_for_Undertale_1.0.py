import keyboard
import pydirectinput
import time
print('KeyChanger_for_Undertale (version 1.0)')
def main():
    start = input('start program? (y/n): ')
    if start == 'y':
        print('program started!')
        print('press f6 to pause program')
        change()
    else:
        exit()

def change():
    pydirectinput.PAUSE = 0.0
    keys = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    check = {'w': False, 'a': False, 's': False, 'd': False}
    while True:
        if keyboard.is_pressed('f6'):
            print('program stopped')
            for arrow in keys.values():
                pydirectinput.keyUp(arrow)
            main()
        for key, arrow in keys.items():
            is_pressed = keyboard.is_pressed(key)
            if is_pressed and not check[key]:
                pydirectinput.keyDown(arrow)
                check[key] = True
            elif not is_pressed and check[key]:
                pydirectinput.keyUp(arrow)
                check[key] = False
        time.sleep(0.001)
if __name__ == "__main__":
    main()