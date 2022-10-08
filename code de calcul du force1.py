P=float(input("etrez la valeur de pression:"))
D=float(input("entrez la valeur de diamétre:"))
try :
    pi=3.14
    S=(D/2)**2*pi
    F=P*S*10**6
    print("la valeur de la force est:",F,"N")
except:
    print("la valeur de pression et/ou de diamétre n'est pas correct")
