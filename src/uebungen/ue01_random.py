import random

liste = []
for i in range(-10,10):
	liste.append(random.randint(-10,10))
print(f"Eine Liste mit {len(liste)} Zahlen: {liste}")
