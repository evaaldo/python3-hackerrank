salarioMinimo =  1.291
salarioFamiliar = int(input('qual o salario familiar'))

mensalidade = 10000
desconto = 0

filhos = int(input('qual o numero de filhos'))
bolsa = 0

if salarioFamiliar <= 1000:
    desconto = 0.55*mensalidade
elif salarioFamiliar > 1000:
    desconto = 0.1*mensalidade

if filhos <= 2:
    bolsa = 1/4*salarioMinimo
elif filhos > 2:
    bolsa = 2/4*salarioMinimo

mensalidade -= desconto