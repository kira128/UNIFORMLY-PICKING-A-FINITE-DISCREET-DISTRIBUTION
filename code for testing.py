import random
import numpy as np
import math
import scipy.stats as stats
import csv
import os
print(os.getcwd())
lista =[]
G=100000
#array for counting the number of dots in the cubes
cat = np.zeros((8, 8, 8))
spec = 0 #special set

#generating the dots and categorising them into cat
for i in range(G):
    S=0 #that need to to updated from chapter 5 and 6
    triplets = [] #my dot
    for j in range(3):
        U = random.uniform(0,1) 
        X = (1-S)*(1-pow((1-U),(1/(4-j-1)))) #aplying inverse on uniform
        triplets.append(X) #adding the first component of the dot
        S = S + X # updating S
    '''
    triplets.append(1-sum(triplets)) #adding the last component of the dot
    uredjena_cetvorka = tuple(triplets) 
    lista.append(uredjena_cetvorka) #adding the dot to the list
    '''


    
    cat_temp = [math.floor(num * 10) for num in triplets] # prepering dots to put them into cat
    if sum(cat_temp) <= 7: #condition that dot is in one of the cubes I am considering (or in the special set)
        cat[cat_temp[0],cat_temp[1],cat_temp[2]] +=1 #updating cat
    else:
        spec += 1 #updating special set
'''
with open('uredjene_cetvorke.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
print("Uređene četvorke su uspešno zapisane u CSV datoteku!")
'''


theoretical = np.full((8, 8, 8),0.006*G) #theoretical value of distribution for the cubes
#calculating residuals for chi square
rez = cat - theoretical
rez = rez**2
rez = rez/theoretical

chi = ((spec-(1-(0.12*6))*G)**2)/((1-(0.12*6))*G) #firstly adding the residual of special set

#adding all residuals for chi square
for i in range (8):
    for j in range(8):
        for k in range(8):
            if i + j + k < 8:
                chi += rez[i,j,k]
print("p-val is: ")
print(stats.chi2.sf(chi, 120)) #calculating p-val

            

