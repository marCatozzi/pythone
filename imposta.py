#Realizzare un programma che chieda a video il reddito complessivo, al netto degli oneri deducibili, e restituisa l'imposta lorda.

reddito_complessivo = input("Dimmi il tuo reddito: ")
v1 = int(reddito_complessivo)

oneri = input("Indicami gli oneri deducibili: ")
v2 = int(oneri)

reddito_imponibile = v1 - v2

v3 = reddito_imponibile

imposta_lorda = 0

if v3 <= 28000:
   imposta_lorda = v3 * 0.23
else:
    if v3 > 28000 and v3 <= 50000:
       imposta_lorda = ((50000 - 28000) * 0.35)
    else:
       if v3 >= 50000:
          imposta_lorda = ((50000 - v3) * 0.43)

print("La tua imposta lorda è", (imposta_lorda))
