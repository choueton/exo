# exo 1.1

n = int(input("Entrez un nombre : "))
def fac(fa):
    fa = 1
    for i in range(1, n + 1):
        fa = fa*i
    print( fa )
    return fa
fac(n)


# exo 1.2

def nombres_impairs(N):
    impairs = []
    i = 1  
    while i <= N:
        impairs.append(i)
        i += 2
    return impairs

N = int(input("Entrez un nombre : "))
resultat = nombres_impairs(N)
print(resultat)

# exo 1.3
liste =[17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste = liste + [12]
print(liste)
liste.reverse()
print(liste)
print(len(liste))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[:3])

def supprimeDoublon(lusto):
    p = []
    for i in lusto:
        if i not in p:
            p.append(i)
    return p

lusto = [1, 1, 2, 4, 9, 2, 5, 4]
resultat = supprimeDoublon(lusto)
print(resultat)
