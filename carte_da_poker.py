#carte_da_poker.py

#Identificare i caratteri Unicode che rappresentano i 4 semi del poker (cuori, quadri, fiori, picche) nella variante solo bordo.
#Creare una stringa con i quattro semi.

solo_bytes = b"	\xe2\x99\xa1\xe2\x99\xa2\xe2\x99\xa7\xe2\x99\xa4"
stringa = solo_bytes.decode()
print(stringa)
