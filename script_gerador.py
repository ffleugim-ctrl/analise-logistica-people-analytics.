import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Configurações Iniciais
n_registros = 1500
auditores = ['Miguel Dantas', 'Val', 'Equipe Dia', 'Equipe Noite']
produtos = ['Nike Ja 2', 'iPhone 15', 'Monitor Gamer', 'Mouse Gamer', 'Camiseta Meli', 'Notebook Samsung', 'Scanner Zebra', 'Fone JBL']
condicoes = ['Lacrado', 'Avariado', 'Embalagem Aberta', 'Item Errado']
setores = ['Recebimento', 'Expedição', 'Estoque', 'Separação']

dados = []

# 2. Geração da Massa de Dados
for i in range(1, n_registros + 1):
    # Gerando um código de pacote único (ex: ML-1234-A)
    cod_pacote = f"ML-{random.randint(1000, 9999)}-{random.choice(['A', 'B', 'C'])}"
    
    produto = random.choice(produtos)
    condicao = random.choice(condicoes)
    auditor = random.choice(auditores)
    setor = random.choice(setores)
    
    # Simulação de tempo (Segundos): Itens com problema demoram mais
    if condicao == 'Lacrado':
        tempo = random.randint(30, 120)
    else:
        tempo = random.randint(120, 300)
    
    # Gerando datas aleatórias nos últimos 7 dias
    data_base = datetime.now() - timedelta(days=random.randint(0, 7))
    data_final = data_base.replace(hour=random.randint(6, 23), minute=random.randint(0, 59))
    
    dados.append([i, cod_pacote, produto, condicao, auditor, setor, data_final, tempo])

# 3. Criação do DataFrame
df = pd.DataFrame(dados, columns=['ID', 'Codigo Pacote', 'Produto', 'Condicao', 'Auditor', 'Setor origem', 'Data auditoria', 'Tempo (segundos)'])

# 4. Exportação para CSV
df.to_csv('base_completa_cajamar.csv', index=False, sep=';', encoding='utf-8-sig')

print(f"🚀 Sucesso! Arquivo com {n_registros} linhas gerado para o Dashboard de Cajamar.")
