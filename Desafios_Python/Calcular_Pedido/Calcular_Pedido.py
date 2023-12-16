# Calcular o Preço Final de um Pedido

valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


totalHamburger = valorHamburguer * quantidadeHamburguer

totalBebida = valorBebida * quantidadeBebida

totalPagar = totalBebida + totalHamburger

troco = valorPago - totalPagar


print(f'O preço final do pedido é R$ {totalPagar:.2f}. Seu troco é R$ {troco:.2f}.')