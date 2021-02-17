def incomodam(n):
    if n <= 0:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n, x = 2):
    if n < 1:
        return ""
    else:
        if x == 2:
            return "Um elefante incomoda muita gente\n" + str(x) + " elefantes " + incomodam(x) + "muito mais\n" + elefantes(n-1, x+1)
        else:
            num = x-1
            return str(num) + " elefantes incomodam muita gente\n" + str(x) + " elefantes " + incomodam(x) + "muito mais\n" + elefantes(n-1, x+1)
