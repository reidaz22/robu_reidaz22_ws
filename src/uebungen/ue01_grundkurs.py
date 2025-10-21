# 14.10.25 4AHMBA

#Kommentare: Hashtag # -> einzeiliger Kommentar
#DocStrings: ''' Kommentar '''
#Python Interpreter Öffnnen/Schließen
#öffen CLI: python3
#schließen CLI: exit()



# Einzeiliger Kommentar

''' 
Mehr Zeiliger Kommentar 
Dieser Kann auch als Docstring verwendet werden
'''

#DocString ist ein Hilfe-Text der von Visual Studio 
#Code automatisch bei Funktionen eingeblendet wird
#DocStrings werden gleich nach der Deklaration
#des Funktionsnamens implementiert
#Python Interpreter: führt  den Code auf jedem Betriebssystem aus 
#Vorteil es wird kein Compiler benötigt
#Start des Interpreters in der CLI: python3
#Start eines Programms in der CLI: python3 pfad-zum-programm
#                                            z.B. python3 ue01_grundkurs.py

#Bilbliotheken

# Bibliotheken

print("servas")

import math                     # Importiert die gesamte Bibliothek 
from math import pi as M_PI     # Importiert nur die Konstante pi aus der Bibliothek
                                # Mit as können zusätzlich den Namen umbenennen

print(math.pi)                  #Verwendung der Konstante aus der gesamten Bibliothek
print(M_PI)                     #Verwendung als importierte Konstante

#Das Schlüsselwort as kann auch dafür verwendet werden, Namen abzukürzen
import matplotlib.pyplot as plt

#Variablen-Namen
#Nur Kleinbuchstaben und Ziffern
#keine Sonderzeichen
#keine Umlaute
#keine Ziffern zu Beginn der Bezeichnung
#ein Underscore ist erlaubt: z.B.: meine_variable
#Private Variablen beginne mit einem Underscore z.B.: _meine_variable
#es dürfen keine Python-Schlüsselwörter verwendet werden (z.B.: while, for , if , import, ...)
#Python unterscheidet zwischen Groß- und Kleinschreibung ( case sensitiv)

#Grundlegende Datentypen
#int, float, complex, str

titel = "Datentypen" #String-Variable
vorname = " Daniel"
nachname = " Reinhart" # zwische "" und '' wird nicht unterschieden

name = vorname + " " + nachname #Texte werde verkettet
klassenvorstand = True       #bool
groesse = 1.85               #float
schuhgroesse = 43            #int
impedanz= 10 + 20j           #complexe variable

#print("Ausgabe von unterschiedlichen", titel, ":")
print(f"Ausgabe von unterschiedlichen {titel}:")
print(f"Meine Name ist {name}")
print(klassenvorstand, type(klassenvorstand))
print(impedanz, type(impedanz))

print("Impedanzberechnung\n") #Zusätzlicher Zeilenvorschub
print("==================")

resistor = 1000         #Ohm
capacitor = 1e-6        #µF (Farad = As/V)
frequency = 50.0        #Hz

impedanz = complex(resistor, -1/(2*M_PI*frequency*capacitor))
tau = resistor * capacitor
print(f"Impetanz:       {impedanz/1000:<10.2f} kOhm")
# C - Alprint("Impedanz:   %10.2f kOhm") % (impedanz/1000)
print(f"Zeitkonstante: {1000* tau:<10.2f} ms")
print(f"Grenzfrequenz: {1/(2*M_PI*frequency*tau):<10.2f} Hz")

print(10/4)         #Ergebnis mit Komma
print(10//4)        #Schneidet den Rest ab Integer
print(2**3)         #Potenzieren 2^3 (zwei hoch drei)

#Collections: list, set tuple, dict
#muteable: veränderbar (list, dict, set)
#immutable: nicht veränderbar (list wie eine Konstante zu behandeln)->

# in einer Liste können verschiedene Datentypen gemischt werden
my_list = [1, 2, -5, 3, 14, "some text", [3, -2], (1+1j)]
print("Erstes Element:", my_list[0])
print("Letztes Element:", my_list[-1])
print("Liste in der Liste:", my_list[-2][0])
print("Slicing 1:", my_list[1:3]) #Ausgabe von Element 1 und 2 (ausschließlich 3)
print("Slicing 2:", my_list[-2:]) #Ausgabe der Letzten zwei Elemente
print("Slicing 3:", my_list[:5:2]) #Ausgabe von 0 bis 4 und da nur jedes zweite
print("Slicing 4:", my_list[::2]) #Gibt jedes zweite element aus

#Entpacken von Listen
a, b, c = my_list[:3]
print(f"a={a}b={b}c={c}")