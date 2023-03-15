import time
import winsound
import pyaudio
from pydub import AudioSegment
from pydub.playback import play

class Audio:
    def __init__(self, path):
        self.sound = AudioSegment.from_file(path)

    def play(self):
        self.sound = self.sound.fade(to_gain=10, start=0, end=len(self.sound))
        play(self.sound)

class Activity:
    def __init__(self):
        self.audio = Audio("./media/game_start_split.mp3")
        self.time_total = 0

    def new_activity(self, name, number_time):
        print(f'>>> {name} -> {number_time} minutes')
        seconds = number_time * 60
        count = 0
        print(f'Start: {self.get_time()}')
        while True:
            value_time = self.convert_seconds_to_format(count)#time.strftime('%H:%M:%S', time.gmtime(count))
            print(f'\rRunning: {value_time}', end='')
            time.sleep(1)
            count += 1
            if (seconds == count - 1):
                self.audio.play()                   
                print(f' Finish: {self.get_time()}')
                self.time_total += seconds + 1
                break 

    def start(self):
        self.audio.play()

    def rest(self, time = 5):
        self.new_activity("Rest", time)

    def get_time(self):    
        t = time.localtime()
        return time.strftime("%H:%M:%S", t)    

    def convert_seconds_to_format(self, value):
        return time.strftime('%H:%M:%S', time.gmtime(value))
    
    def get_time_total(self):
        print(f'*********** Congratulation, you`re a beast - The time total is: {self.convert_seconds_to_format(self.time_total)} ***********')

# Write command how next and go to the next activiy, pause and continue

# Turn on automatically my pc at 5:45 a.m., colocate an alarm

# Start automatically at 6 a.m.

activity = Activity()

activity.start() ## Change the sound start for any more slighlty
# activity.new_activity("English", 30) ## minutes
# # activity.rest()
# activity.new_activity("Startup", 10)
activity.new_activity("Platzi", 30)
# activity.rest()   
activity.new_activity("Master", 9)
activity.new_activity("Thesis", 30)
# activity.rest()
activity.new_activity("Memorize", 5)
activity.new_activity("Project", 15)
# activity.rest()
activity.new_activity("AWS", 10)
# activity.rest()
activity.new_activity("SoyHenry", 5)
#-- minutes
activity.new_activity("Guitar", 9)
activity.new_activity("Ballet", 9)
activity.new_activity("Salsa", 9)
activity.new_activity("Bachata", 9)

# Una app donde puedas colocar todas tus actividades que puedas hacer, colocar sus prioridades, todo tu tiempo disponible y otra app que te haga 

activity.get_time_total()