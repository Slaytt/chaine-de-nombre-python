import random
x = int(input("taille de la liste : "))
tab1 = [random.randint(0,100) for i in range(x)]
cont = []
temp = []
log = 0
print(tab1)
for i in range(len(tab1)):
    
    if tab1[i] == tab1[i-1]+1 :
        temp.append(tab1[i-1])
        temp.append(tab1[i])
        log += 1
    else:
        if len(cont) < len(temp):
            cont = temp
            print(cont)
        temp = []

print("la suite de nombre consécutifs la plus grande est",list(set(cont)),"mais il existe aussi",log-1,"autres suites consécutives différente mais moins longues ou égales")
