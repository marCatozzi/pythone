#p.601 P.9.7

# Realizzate una classe Student che rappresenti uno studente.
# Uno studente ha un nome, un cognome e un punteggio totale(score)
# Definite, nella classe, un costruttore appropriato e i metodi getName(), addQuiz(score), getTotalScore() e getAverageScore.
# Per realizzare l'ultimo dei metodi richiesti, che calcola il punteggio medio per i questionari compilati dallo studente, è necessario memorizzare anche il numero di questionari compilati.


class Student:
    def __init__(self, nome, cognome):
         self._nome = nome
         self._cognome = cognome
         self._totScore = 0.0
         self._n0fQuiz = 0
    def getName(self):
         return f"{self._nome} {self._cognome}"
    def addQuiz(self, score):
         self._totScore += score
         self._n0fQuiz += 1
    def getTotalScore(self):
         return self._totScore
    def getAverageScore(self):
         return self._totScore / self._n0fQuiz
          

giovanni = Student("Giovanni", "Girolimetti")
tommaso = Student ("Tommaso", "Freddari")

print(giovanni.getName())
print(tommaso.addQuiz(30))
print(tommaso.addQuiz(18))
print(tommaso.getAverageScore())