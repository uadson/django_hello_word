from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Olá Dev</h1>')

def nome(request, nome):
    return HttpResponse('<h1>Olá {}</h1>'.format(nome))

def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>A soma entre {} e {} é igual a {}</h1>'.format(
        num1, num2, soma
    ))

def sub(request, num1, num2):
    subt = num1 - num2
    return HttpResponse('<h1>A subtração entre {} e {} é igual a {}</h1>'.format(
        num1, num2, subt
    ))

def mult(request, num1, num2):
    mult = num1 * num2
    return HttpResponse('<h1>A multiplicação entre {} e {} é igual a {}</h1>'.format(
        num1, num2, mult
    ))

def dividir(request, num1, num2):
    divisao = num1 / num2
    return HttpResponse('<h1>A divisão entre {} e {} é igual a {}</h1>'.format(
        num1, num2, divisao
    ))