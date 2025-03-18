#Scrivete un programma per tradurre i numeri da 1 a 7 nei nomi dei giorni della settimana corrispondenti in Italiano.

giorni=(
"lunedì   " 
"martedì  " 
"mercoledì" 
"giovedì  " 
"venerdì  " 
"sabato   " 
"domenica "  
)

giorno = int(input("Indica giorno: "))
p = (giorno - 1) * 9
print("%-7.9s" % giorni[p:])
