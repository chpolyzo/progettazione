
def ciao(n1):
    a = 3
    num = somma(a, n1)
    while num>0:
        print("Ciao")
        num -= 1

def somma(num1, num2):
    tot = num1+num2
    return tot

a = 1
b = 2
ciao(b)