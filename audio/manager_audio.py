from pydub import AudioSegment
from pydub.playback import play

# load the audio file
audio_file = AudioSegment.from_file(file = "C:/Users/axel1/Desktop/gitDataScience/interval_timer/audio/security_alarm.wav",
                                    format = 'wav')
play(audio_file)

# set the start and end times for the trim (in milliseconds)
start_time = 10000
end_time = 15000

# perform the trim
trimmed_audio = audio_file[start_time:end_time]

# export the trimmed audio to a file
trimmed_audio.export("output.wav", format="wav")