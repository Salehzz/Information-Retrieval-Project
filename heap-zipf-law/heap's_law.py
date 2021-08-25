#Heaps' law
import matplotlib.pyplot
import math
file = open("myfile.txt",'r')
wordkinds = 0
words = 0
# har 50 kalame
tedadkalamatmotefavet = {}
kalamat = []
for line in file:
    for word in line.split():
        words = words + 1
        if(word not in kalamat):
            kalamat.append(word)
            wordkinds = wordkinds + 1
        if(words%50 == 0):
            tedadkalamatmotefavet[math.log(words)] = math.log(wordkinds)
# kamtarshodan nesbat anvaee kalamat be tedad an ha ba afzayesh tol matn
kinds = list(tedadkalamatmotefavet.values())
faravani = list(tedadkalamatmotefavet.keys())
matplotlib.pyplot.plot(faravani,kinds)
matplotlib.pyplot.show()
