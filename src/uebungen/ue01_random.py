import random

liste = []
for i in range(-10,10):
	liste.append(random.randint(-10,10))
# Variablen können in einer print Anweisung mit {} makiert und ausgegeben werden
# Vor den " " muss allerdings ein f stehen, ansosten werdie die Variablen nicht erkannt
# Ich kann natürlich ein eine print-Anweisung im C-Style schreiben
print(f"Eine Liste mit {len(liste)} Zahlen: {liste}")

