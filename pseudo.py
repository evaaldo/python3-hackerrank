vendas = int(input("Quanto o funcionário vendeu?"))
valorFinal = 0
if vendas >= 55000 and vendas <= 100000:
    valorFinal += 0.02 * vendas
    print("A comissão do funcionário será", valorFinal)
elif vendas < 55000:
    valorFinal += 100
    print("O salário do funcionário é", valorFinal)
elif vendas > 100000:
    valorFinal += 5000
    print("A comissão do funcionário será", valorFinal)