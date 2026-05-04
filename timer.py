import time

print("=== Study Timer ===")

subject = input("Enter subject name: ")
minutes = int(input("Enter study time in minutes: "))

seconds = minutes * 60

print(f"Starting {subject} for {minutes} minutes...")

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds -= 1

print("/ntime's up! Well done.")

choice = input("Do you want a 5 minute break? (yes/no): ")

if choice.lower() == "yes":
    break_seconds = 5 * 60

    while break_seconds > 0:
        mins = break_seconds // 60
        secs = break_seconds % 60
        print(f"Break Time {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        break_seconds -= 1

    print("\nBreak over. Back to work.")
    
else:
    print("Good. Keep Studying.")