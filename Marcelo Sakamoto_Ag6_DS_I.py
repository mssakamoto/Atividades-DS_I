Total_Compra = float(input("Digite o valor total da compra (Ex: 100.50): R$"))
if Total_Compra < 200:
    Desconto = Total_Compra * 0.05
    ValorFinal = Total_Compra - Desconto
    print(f"Desconto aplicado: R${Desconto:.2f}")
    print(f"Valor final a pagar: R${ValorFinal:.2f}")
elif Total_Compra >= 200 and Total_Compra < 300:
    Desconto = Total_Compra * 0.1
    ValorFinal = Total_Compra - Desconto
    print(f"Desconto aplicado: R${Desconto:.2f}")
    print(f"Valor final a pagar: R${ValorFinal:.2f}")
elif Total_Compra >= 300:
    Desconto = Total_Compra * 0.15
    ValorFinal = Total_Compra - Desconto
    print(f"Desconto aplicado: R${Desconto:.2f}")
    print(f"Valor final a pagar: R${ValorFinal:.2f}")