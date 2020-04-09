import matplotlib.pyplot as plt
import numpy as np

def ChFile():
	file = raw_input("Entrer un fichier avec la sequence : ")
	
	return file

def InfoSeq(file):
	seq = open(file, "r")
	info = seq.readline()
	
	pos1 = info.find("|")
	pos2 = info.find("|", pos1+1)
	
	info = info[pos1 + 1 : pos2]
	
	return info

def RdSeq(file):
	seq = open(file, "r")
	sequence = ""
	
	inutile = seq.readline()
	
	while(1):
		ligne = seq.readline()
		sequence += ligne
		if not ligne:
			break
			
	return sequence

def size():
	fenetre = input("Taille de la fenetre : ")
	seuilId = input("Pourcentage du seuil d'identite : ")
	
	decalage = fenetre * (seuilId / 100.0)
	
	if(decalage < 1):
		decalage = 1
	
	return int(decalage)

def initMatrice(seq1, seq2, decalage):
	x = 0
	y = 0
	k = 0
	
	matrix = np.zeros((len(seq1), len(seq2)))
	
	while(x < len(seq1)):
		while(y < len(seq2)):
			if(seq1[x : x + decalage] == seq2[y : y + decalage]):
				if(x + decalage < len(seq1) and y + decalage < len(seq2)):
					while(k < decalage):
						matrix[x + k][y + k] = 1
						k += 1
			
			y += 1
			k = 0
		
		x += 1
		y = 0

	return matrix

def drawPoint(seq1, seq2, matrice):
	i = 0
	j = 0
	
	while(i<len(seq1)):
		while(j<len(seq2)):
			if(matrice[i][j] == 1):
				plt.scatter(i, j, c = "black", s=5)
				
			j+=1
			
		j=0
		i+=1

def initGraphique(seq1, infoSeq1, seq2, infoSeq2, matrice):
	plt.title("DotPlot")

	plt.xlabel(infoSeq1)
	plt.ylabel(infoSeq2)

	plt.xlim(0, len(seq1)) 
	plt.ylim(0, len(seq2)) 

	print("Creation du graphe en cours")

	drawPoint(seq1, seq2, matrice)

	choix = raw_input("Sauvegarder : [y/n]\n-> ")
	if(choix == "y"):
		name = raw_input("Nom pour la sauvegarde : ")
		plt.savefig(name, format = 'png')
	
	plt.show()


def main():
	nameFile1 = ChFile()
	nameFile2 = ChFile()
	
	seq1 	 = RdSeq(nameFile1)
	seq2 	 = RdSeq(nameFile2)
	
	matrice = initMatrice(seq1, seq2, size())
	
	initGraphique(seq1, InfoSeq(nameFile1), seq2, InfoSeq(nameFile2), matrice)

main()
