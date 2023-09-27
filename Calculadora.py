#!/usr/bin/env python3.10

a = input("Digite o primeiro número e aperte o enter: ")
a = int(a)

print("Escolha a operação desejada")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = input("Digite o número referente a operação desejada e aperte o Enter: ")

b = input("Digite o segundo número e aperte o enter: ")
b = int(b)

def operacao(a, b, op):
    if (op == "1"):
        return a+b
    elif(op == "2"):
        return a-b
    elif(op == "3"):
        return a*b
    else:
        return a/b

resultado = operacao(a, b, op)

print("Resultado da operação: ", resultado)
