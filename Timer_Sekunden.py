import time
x = int(input("Wie viele Sekunden soll der Timer dauern? "))
print("Noch " + str(x) + " sekunden.")
time.sleep(1)
while x > 2:
    x -= 1
    print("Noch " + str(x) + " sekunden.")
    time.sleep(1)
else:
    x -= 1
    print("Noch " + str(x) + " sekunde.")
    time.sleep(1)
    x -= 1
    print("Noch " + str(x) + " sekunden.")
    from playsound import playsound

    playsound("telephone-ring-02.mp3")
