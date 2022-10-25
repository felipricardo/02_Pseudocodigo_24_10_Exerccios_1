"""
1)	Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas. Calcule e mostre o salário a receber seguindo as regras abaixo:
a)	a hora trabalhada vale 1/8 do salário mínimo;
b)	a hora extra vale ¼ do salário mínimo;
c)	o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalha (apresente o valor para o usuário);
d)	a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra(apresente o valor para o usuário);
e)	o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras(apresente o valor para o usuário);

"""
#Entrada de dados
print("Digite o numero de horas trabalhadas")
horastrabalhadas = float(input())
print("Qual o valor do salario minimo")
salariominimo = float(input())
print("Digite o numero de horas extras trabalhadas")
#Processamento
horasextras = float(input())
valorhoratrabalhada = salariominimo / 8
valorhoraextra = salariominimo / 4
valorsalariobruto = horastrabalhadas * valorhoratrabalhada
valorquantiaareceber = horasextras * valorhoraextra
salarioareceber = valorsalariobruto + valorquantiaareceber
#saida
print("O valor da hora trabalhada é de R$ %.2f" % valorhoratrabalhada)
print("O valor do salario bruto é de R$ %.2f" % valorsalariobruto)
print("O valor da hora extra é de R$ %.2f" % valorhoraextra)
print("O valor em extra a receber é de R$ %.2f" % valorquantiaareceber)
print("O salario a receber é de R$ %.2f" % salarioareceber)