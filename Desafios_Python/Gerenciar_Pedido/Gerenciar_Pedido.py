def main():
    n = int(input())

    total = 0

    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    cupom_escolhido = input()  # solicita o cupom de desconto escolhido pelo usuário

    # define o cupom de desconto com base no valor digitado pelo usuário
    if cupom_escolhido == "10%":
        cupom = 0.1  # define o cupom de desconto como 10%
    elif cupom_escolhido == "20%":
        cupom = 0.2  # define o cupom de desconto como 20%
    else:
        cupom = 0  # nenhum cupom de desconto será aplicado

    # calcula o total com desconto e exibe na tela
    total_com_desconto = total * (1 - cupom)
    print(f"Valor total: {total_com_desconto:.2f}")

if __name__ == "__main__":
    main()