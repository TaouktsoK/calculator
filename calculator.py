from mycalc import Mycalc

noumero = input()
for i, num in enumerate(noumero):  # or noumero correctly
    if num == "/" and noumero[i+1] == "0":
        noumero = input("Can't divide with zero, check your input and give the number again: ")


symbols = ("+", "-", "*", "/")
numbers = []
num = ""
calcul = []
summ = 0
prod = 1
for i in noumero:
    numbers.append(i)
for i in numbers:
    if i not in symbols:
        num += i
    else:
        calcul.append(float(num))
        calcul.append(i)
        num = ""
calcul.append(float(num))
print(calcul)


for i in range(2, len(calcul), 2):
    if i == 2:
        if calcul[i - 1] == "+":
            calc = Mycalc((calcul[i - 2]), calcul[i])
            summ = calc.add()
            print(summ)
        elif calcul[i - 1] == "-":
            calc = Mycalc((calcul[i - 2]), calcul[i])
            summ = calc.sub()
            print(summ)
        elif calcul[i - 1] == "/":
            calc = Mycalc((calcul[i - 2]), calcul[i])
            prod = calc.div()
            print(prod)
        elif calcul[i - 1] == "*":
            calc = Mycalc((calcul[i - 2]), calcul[i])
            prod = calc.mult()
            print(prod)
    else:
        if calcul[i - 1] == "+":
            if calcul[i-3] in "+-":
                calc = Mycalc(summ, calcul[i])
                summ = calc.add()
                print(summ)
            elif calcul[i-3] in "*/":
                calc = Mycalc(prod, calcul[i])
                summ = calc.add()
                print(summ)
        elif calcul[i - 1] == "-":
            if calcul[i - 3] in "+-":
                calc = Mycalc(summ, calcul[i])
                summ = calc.sub()
                print(summ)
            elif calcul[i - 3] in "*/":
                calc = Mycalc(prod, calcul[i])
                summ = calc.sub()
                print(summ)
        elif calcul[i - 1] == "/":
            if calcul[i - 3] in "+-":
                calc = Mycalc(summ, calcul[i])
                prod = calc.div()
                print(prod)
            elif calcul[i - 3] in "*/":
                calc = Mycalc(prod, calcul[i])
                prod = calc.div()
                print(prod)
        elif calcul[i - 1] == "*":
            if calcul[i - 3] in "+-":
                calc = Mycalc(summ, calcul[i])
                prod = calc.mult()
                print(prod)
            elif calcul[i - 3] in "*/":
                calc = Mycalc(prod, calcul[i])
                prod = calc.mult()
                print(prod)
