import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load('mixkit-facility-alarm-sound-999.wav')  # Replace with the correct path if needed
    pygame.mixer.music.play()
    print("⏰ Alarm ringing!")
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def countdown_alarm():
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = minutes * 60 + seconds

        print(f"⏳ Countdown started for {minutes} minute(s) and {seconds} second(s)...")

        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            print(f"{mins:02d}:{secs:02d}", end='\r')
            time.sleep(1)
            total_seconds -= 1

        play_alarm()

    except ValueError:
        print("❌ Invalid input. Please enter integers for minutes and seconds.")

if __name__ == "__main__":
    countdown_alarm()
