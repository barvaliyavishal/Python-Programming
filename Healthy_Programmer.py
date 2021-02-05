import multiprocessing
import time
from datetime import datetime
from playsound import playsound

time.sleep(10)
print(" reminder for eyes ExerCise")
p = multiprocessing.Process(target=playsound, args=("Music/Wiz Khalifa - See You Again ft. Charlie Puth _Official Video_ Furious 7 Soundtrack ( 128kbps ).mp3",))
p.start()
x=""
while x != "Done":
    x = input("Enter Done to stop playback")

with open("Healthy_Programmer.txt",'a') as file:

    now = datetime.now()
    file.write(f" {now} : Done Eye Exercise \n")

p.terminate()


time.sleep(15)
print(" reminder for water")
p = multiprocessing.Process(target=playsound, args=("Music/Soundtrack Fast and Furious 8 (Theme Song 2017) - Trailer Music Fast & Furious 8 ( 128kbps ).mp3",))
p.start()
x=""
while x != "Done":
    x = input("Enter Done to stop playback")

    with open("Healthy_Programmer.txt", 'a') as file:
        now = datetime.now()
        file.write(f" {now} : Drank a glass of water \n")

p.terminate()

time.sleep(15)
print(" reminder for exercise")
p = multiprocessing.Process(target=playsound, args=("Music/The Chainsmokers & Coldplay - Something Just Like This (Lyric) ( 128kbps ).mp3",))
p.start()
x=""
while x != "Done":
    x = input("Enter Done to stop playback")

with open("Healthy_Programmer.txt", 'a') as file:
    now = datetime.now()
    file.write(f" {now} : Done Exercise \n")

p.terminate()

print()
print()
f = open("Healthy_Programmer.txt",'r')
data = f.read()
print(data)
f.close()

