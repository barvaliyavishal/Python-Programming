import time
import webbrowser

total_breaks = int(input("How Many breaks Do you want"))
break_count = 0
minutes = int(input("minutes between two breaks"))

while(break_count < total_breaks):
    time.sleep(minutes*60)
    webbrowser.open("https://www.youtube.com/watch?v=RgKAFK5djSk&ab_channel=WizKhalifa")
    break_count = break_count + 1