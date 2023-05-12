import time


def countdown_timer(time_string):
    hours, minutes, seconds = map(int, time_string.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds:
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 60
        print(f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")


time_in_string = input("Input time to count down (h:m:s): ")
countdown_timer(time_in_string)