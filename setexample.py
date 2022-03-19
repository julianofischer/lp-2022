#!/usr/bin/python3

s = set()
x = int(input("Digite um número inteiro: "))
while x not in s:
    s.add(x)
    x = int(input('Digite um nro inteiro: '))

print(s)
