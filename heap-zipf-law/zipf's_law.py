#zipf's law
import matplotlib.pyplot
import math
file = open("myfile.txt",'r')
numberofeachword = {}
for line in file:
    for word in line.split():
        if(word in numberofeachword):
            numberofeachword[word] = numberofeachword[word] + 1
        elif(word not in numberofeachword):
            numberofeachword[word] = 1
# r * f = k (rotbe * faravani = adadsabet)
# log r +log f = log k
faravani = list(numberofeachword.values())
#print(faravani)
faravani = sorted(faravani,reverse = True)
rotbe = []
for i in range(len(faravani)):
    rotbe.append(math.log(i+1))
    faravani[i] = math.log(faravani[i])
matplotlib.pyplot.plot(rotbe,faravani)
matplotlib.pyplot.show()
