# Caio Cesar
# BEE 1010

# Precisa do split() pois o input irá receber 3 valores numa mesma linha, separados pelo espaço
lista1 = input().split()
lista2 = input().split()

# Conversão do tipo de dado (string para int e float) e seu devido cálculo que a questão pediu
valor1 = int(lista1[1])*float(lista1[2])
valor2 = int(lista2[1])*float(lista2[2])

soma = valor1 + valor2

print(f'VALOR A PAGAR: R$ {soma:.2f}')