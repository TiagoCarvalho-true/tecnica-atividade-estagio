import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Extrair os valores de faturamento, ignorando os dias com faturamento zero
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor e maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

# Contar o número de dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibir os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
