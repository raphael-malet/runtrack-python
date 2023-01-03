def calcule(num1,operator,num2):
    if operator == "+" :
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "*":
        return(num1 * num2)
    elif operator == "/":
        return(num1 / num2)
    elif operator == "%":
        return(num1 % num2)
            
print(calcule(3,"+",3))
print(calcule(3,"-",3))
print(calcule(3,"*",3))
print(calcule(3,"/",3))
print(calcule(3,"%",3))

