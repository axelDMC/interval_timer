import time
import winsound

def get_time():
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)

print()
print(' *** Interval time ***')
print()

cycles = int(input('Number of cycles --> '))
seconds_exercise = int(input('Seconds of exercise --> '))
seconds_rest = int(input('Seconds of rest --> '))
print()

spaces = ' ' * 30
print('\rGet ready, the timer will start in: 5 ', end = '')
for n in reversed(range(0,5)):

    time.sleep(1)
    if n > 0:
        print(get_time())
        print('\rGet ready, the timer will start in: {} '.format(n), end='')
    else:
        print('\rGoooooo!!' + spaces, end='')

winsound.Beep(3500, 1000)

for cycle in range(cycles):
    print('\rExercise: 0' + spaces, end='')
    for n in range(seconds_exercise):
        print(get_time())
        time.sleep(1)
        print('\rExercise: {} '.format(n+1), end='')     

    winsound.Beep(3500, 500)

    if cycle + 1 == cycles:
        print('\rWELL DONDE !!' + spaces, end='')   
        break
    else:
        print('\rRest: 0' + spaces, end='')
        for n in range(seconds_rest):
            print(get_time())
            time.sleep(1)
            print('\Rest: {} '.format(n+1), end='')

    winsound.Beep(3500, 150)
    winsound.Beep(3500, 150)

winsound.Beep(3500, 1500)

