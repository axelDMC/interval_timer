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
        self.audio = Audio("./media/security_alarm_split.wav")

    def new_activity(self, name, number_time):
        print(f'>>> {name} -> {number_time} minutes')
        seconds = number_time * 60
        count = 0
        print(f'Start: {self.get_time()}')
        while True:
            value_time = time.strftime('%H:%M:%S', time.gmtime(count))
            print(f'\rRunning: {value_time}', end='')
            time.sleep(1)
            count += 1
            if (seconds == count - 1):
                self.audio.play()                   
                print(f' Finish: {self.get_time()}')
                break 

    def rest(self):
        self.new_activity("Rest", 5)

    def get_time(self):    
        t = time.localtime()
        return time.strftime("%H:%M:%S", t)        

activity = Activity()

activity.new_activity("English", 0.1) ## minutes
activity.rest()
activity.new_activity("Startup", 10)
activity.rest()
activity.new_activity("Platzi", 30)
activity.new_activity("Master", 5)
activity.new_activity("Thesis", 30)
activity.rest()
activity.new_activity("Memorize", 7)
activity.new_activity("Project", 15)
activity.rest()
activity.new_activity("AWS", 10)
activity.rest()
activity.new_activity("Henry", 10)