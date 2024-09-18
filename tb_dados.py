import pandas as pd

dados = []

while True:
    funcionario = input("Digite o nome do Funcionário que realizou a venda (ou 'sair' pra encerrar): ")
    if funcionario.lower() == 'sair':
        break
    data_venda = input('Digite a data em que realizou a venda (ex: DD/MM/AAAA): ')
    produto = input('Digite o nome do produto que vendeu: ')
    valor_produto = float(input('Digite o valor do produto que vendeu: '))
    loja = input('Digite a loja onde trabalha: ')
    dados.append({
        'Funcionário': funcionario,
        'Data': data_venda,
        'Produto': produto,
        'Valor Produto': valor_produto,
        'Loja': loja
    })
    
df = pd.DataFrame(dados)

print("\nDados coletados:")
print(df)

df.to_excel('tb_dados.xlsx', index=False)

print("\nDados salvos em 'tb_dados.xlsx'.")