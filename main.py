def multiplication(x, y):
    return float(x) * float(y)

def addition(x, y):
    return float(x) + float(y)

def soustraction(x, y):
    return float(x) - (y)

def division(x, y):
    if y != 0:
        return float(x) / float(y)
    else:
        return "Impossible de diviser par 0"
    
    
def operation(operateur,nombre1,nombre2):
    
    if operateur == "*":
        result = multiplication(nombre1, nombre2)
    
    elif operateur == "+":
        result = addition(nombre1, nombre2)
        
    elif operateur == "-":
        result = soustraction(nombre1, nombre2)
        
    elif operateur == "/":
        result = division(nombre1, nombre2)
        
    
    
def calculatrice():
    result = ""
    nombre1 = ""
    nombre2 = ""
    operateur = ""
    
    if result == "":
            nombre1 = input("Entrez un nombre/chiffre : ")
            operateur = input ("Entree un operateur(+,/,-,*) : ")
            nombre2 = input("Entrez un nombre/chiffre : " )
            result=operation(operateur, nombre1, nombre2)
            
calculatrice()
        