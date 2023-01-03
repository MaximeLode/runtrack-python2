def calcul(n1, operateur, n2):
    if operateur == "+":
        result = n1 + n2
    elif operateur == "-":
        result = n1 - n2
    elif operateur == "%":
        result = n1 % n2
    elif operateur == "*":
        result = n1 * n2
    elif operateur == "/":
        result = n1 / n2
    else: 
        result = "operateur inconnu "
    print(result)
calcul(12,"*",5)
