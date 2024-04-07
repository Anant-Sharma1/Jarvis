import datetime
import time
import random
from playsound import playsound

def Greetings():
    """Generates a greeting with time and adds a random variation."""

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    playsound("DataBase\\audio\\start_sound.mp3")  # Play the start sound

    greetings = {
        "morning": [
            f"Good Morning sir, it's {tt}. Have a delightful day!",
            f"Top of the morning to you, sir! It's {tt}.",
            f"Rise and shine!  It's {tt} already, sir."
        ],
        "afternoon": [
            f"Good Afternoon sir, it's {tt}. Hope you're having a productive day!",
            f"The sun's still high! It's {tt}, sir.",
            f"Hello again! It's {tt} now, sir."
        ],
        "evening": [
            f"Good Evening sir, it's {tt}.",
            f"The day is winding down, sir. It's {tt}.",
            f"Time to relax! It's {tt}, sir."
        ]
    }

    # Select random greeting based on time period
    if hour >= 0 and hour < 12:
        random_greeting = random.choice(greetings["morning"])
    elif hour >= 12 and hour < 18:
        random_greeting = random.choice(greetings["afternoon"])
    else:
        random_greeting = random.choice(greetings["evening"])

    return random_greeting
