from csv import reader
from random import shuffle
from math import log10

positivedictionary = {}
negativedictionary = {}

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			else:
				dataset.append(row)
	return dataset
def train_data_test_data(dataset):
	meanaccuracy = 0
	for k in range(9):
		accuracy = 0
		positiveitems=0
		negativeitems=0
		negativedictionary.clear()
		positivedictionary.clear()
		for i in range(10):
			for j in range(100):
				if(i != k and i*100+j < len(dataset)):
					x = dataset[i*100+j][1].split()
					if(dataset[i*100+j][0] == '0'):
						for y in x:
							if(y in negativedictionary):
								negativedictionary[y]+=1
								negativeitems+=1
							else:
								negativedictionary[y]=1
								negativeitems+=2
					else:
						for y in x:
							if(y in positivedictionary):
								positivedictionary[y]+=1
								positiveitems+=1
							else:
								positivedictionary[y]=1
								positiveitems+=2
		for j in range(100):
			score = 0
			x = dataset[k*100+j][1].split()
			for y in x:
				if(y in positivedictionary):
					score -= log10((positivedictionary[y]+1)/positiveitems)
				if(y in negativedictionary):
					score += log10((negativedictionary[y]+1)/negativeitems)
			if(score < 0 and dataset[k*100+j][0] == '0'):
				accuracy +=1
			elif(score >= 0 and dataset[k*100+j][0] == '4'):
				accuracy +=1
		meanaccuracy += accuracy
	meanaccuracy /= 9
	return meanaccuracy

# Test Naive Bayes on StrictOMD Dataset
filename = 'StrictOMD.csv'
dataset = load_csv(filename)
meanaccuracy = 0
# Getting Mean for 20 Shuffles of Dataset
for i in range(20):
	shuffle(dataset)
	meanaccuracy += train_data_test_data(dataset)
meanaccuracy /=20
print("Mean Accuracy:",meanaccuracy)
