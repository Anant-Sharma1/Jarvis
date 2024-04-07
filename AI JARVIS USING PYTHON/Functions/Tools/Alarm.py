import time
import pygame
from threading import Thread

alarm_thread = None
alarm_should_stop = False  # Shared flag to signal the thread to stop

def set_alarm(alarm_time, sound_file="audio\\Music\\back-in-black.mp3"):
    global alarm_thread, alarm_should_stop
    alarm_should_stop = False  # Reset the flag before starting the alarm
    print("ALARM STARTED")
    alarm_thread = Thread(target=set_set_alarm, args=(alarm_time, sound_file))
    alarm_thread.start()

def set_set_alarm(alarm_time, sound_file):
    global alarm_should_stop
    while not alarm_should_stop:  # Check the flag regularly
        current_time = time.strftime("%H:%M:%S")
        if current_time >= alarm_time:
            print("Time's up sir!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() and not alarm_should_stop:  # Check flag within the loop
                pygame.time.Clock().tick(10)

            # Stop the music when the flag is set
            pygame.mixer.music.stop()
            
    time.sleep(1)

def stop_alarm():
    global alarm_should_stop
    global alarm_thread
    if alarm_thread is not None:
        alarm_should_stop = True  # Set the flag to signal the thread to stop
        alarm_thread.join()  # Wait for the thread to finish gracefully
        print("ALARM STOPPED")
        alarm_thread = None
