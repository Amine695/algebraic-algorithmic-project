﻿from matplotlib import pyplot as plt
import re

file1 = "benchmarks/NaiveInversion.txt"
file2 = "benchmarks/StrassenInversion.txt"
file3 = "benchmarks/StrassenMultiplication.txt"
file4 = "benchmarks/NaiveMultiplication.txt"
file5 = "benchmarks/StrassenInversionMultiplication.txt"

regextimeInv = '\d*?\.\d+'

plt.figure(figsize=(12,6))
with open(file1,"r") as f:
    timeNaiveInv = re.findall(regextimeInv, f.read())
    timeNaiveInv = [float(i) for i in timeNaiveInv]
    if timeNaiveInv:
        size = []
        for i in range(len(timeNaiveInv)):
            size.append(2**(i+1))
        plt.plot(size,timeNaiveInv,label = "Naive Inversion using LU decomposition")
    

with open(file2,"r") as f:
    timeStrassenInv = re.findall(regextimeInv, f.read())
    timeStrassenInv = [float(i) for i in timeStrassenInv]
    if timeStrassenInv:
        size = []
        for i in range(len(timeStrassenInv)):
            size.append(2**(i+1))
        plt.plot(size,timeStrassenInv,label = "Strassen Inversion using naive product")


with open(file3,"r") as f:
    timeStrassenMult = re.findall(regextimeInv, f.read())
    timeStrassenMult = [float(i) for i in timeStrassenMult]
    if timeStrassenMult:
        size = []
        for i in range(len(timeStrassenMult)):
            size.append(2**(i+1))
        plt.plot(size,timeStrassenMult,label = "Strassen Multiplication")



with open(file4,"r") as f:
    timeInvMult = re.findall(regextimeInv, f.read())
    timeInvMult = [float(i) for i in timeInvMult]
    if timeInvMult:
        size = []
        for i in range(len(timeInvMult)):
            size.append(2**(i+1))
        plt.plot(size,timeInvMult,label = "Naive Multiplication")



with open(file5,"r") as f:
    timeStrassenInvMult = re.findall(regextimeInv, f.read())
    timeStrassenInvMult = [float(i) for i in timeStrassenInvMult]
    if timeStrassenInvMult:
        size = []
        for i in range(len(timeStrassenInvMult)):
            size.append(2**(i+1))
        plt.plot(size,timeStrassenInvMult,label = "Strassen Inversion using strassen's multiplication")



plt.ylabel("Temps (s)",fontsize = 10,fontweight='bold')
plt.xlabel("Taille",fontsize = 10,fontweight='bold')
plt.title("Evolution of the computation time as a function of the size of the matrix",fontsize = 12,fontweight='bold')
plt.legend(loc="upper left")
plt.savefig("plots/ResultBenchmarks.png",bbox_inches='tight')
plt.show()



