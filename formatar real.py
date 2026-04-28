def formatar_real(valor):
    texto = f"R$ {valor: ,.2f}" # Padrão EUA: 1,234.56
    texto = texto.replace(",","X")
    texto = texto.replace(".",",")
    texto = texto.replace("X",".")
    return texto
#Uso: 
preco_hospedagem = 1234.5
print(formatar_real(preco_hospedagem)) #R$ 1.234,50