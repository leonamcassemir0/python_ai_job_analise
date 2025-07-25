# -*- coding: utf-8 -*-
"""Ai_job_analise

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fM1WCbiuRHO97SIUsaDceeyzccHCDsSx

# Análise de IA nos trabalhos

## Importando as bibliotecas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ai_job_df = pd.read_csv('/content/ai_job_trends_dataset.csv')
ai_job_df.head()

"""## Analisando o DataFrame"""

ai_job_df.describe()

ai_job_df.info()

ai_job_df.columns

"""## Análise

A análise consiste em responder 6 perguntas:
1. Qual indústria tem maior risco de automação?
2. Quais os 10 empregos com maior e menor risco de automação?
3. Qual o número de vagas por impacto da IA?
4. Qual o salário médio por impacto da IA?
5. Qual a distribuição de risco por nível educacional?
6. Qual a correlação entre risco de automação e salário?

## 1. Qual indústria tem maior risco de automação?
"""

# Transformando a coluna para valores de ponto flutuante
ai_job_df['Automation Risk (%)'] = ai_job_df['Automation Risk (%)'].astype(float)

# Agrupando a média de 'Automation Risk (%)' para cada indústria
avg_automacao = ai_job_df.groupby('Industry')['Automation Risk (%)'].mean().round(2)
avg_automacao.head(3).sort_values(ascending=False)

"""Beseado na média da coluna 'Automation Risk (%)' para cada indústria, vê-se que o entretenimento tem o maior risco de automação, seguido por finanças e educação.

## 2. Quais os 10 empregos com maior e menor risco de automação?
"""

# Selecionar os 5 cargos com maior e menor risco
maior_risco = ai_job_df.nlargest(10, 'Automation Risk (%)')
menor_risco = ai_job_df.nsmallest(10, 'Automation Risk (%)')

import matplotlib.pyplot as plt
import seaborn as sns

# Criando a moldura para os gráficos
fig, ax = plt.subplots(1, 2, figsize=(20, 6))


# Gráfico do maior risco
ax1 = sns.barplot(data=maior_risco, x='Automation Risk (%)', y='Job Title', ax=ax[0])

# Função para adicionar rótulos nas barras
for container in ax1.containers:
  ax1.bar_label(container, fmt='%.2f', label_type='center', fontsize=16, padding=180, color='white')


# Gráfico do menor risco (assumindo que você tem essa variável)
ax2 = sns.barplot(data=menor_risco, x='Automation Risk (%)', y='Job Title', ax=ax[1])

# Função para adicionar rótulos nas barras
for container in ax2.containers:
  ax2.bar_label(container, fmt='%.2f', label_type='edge', fontsize=16, padding=20)


# Personalização dos gráficos

# Gráfico 1 (Maiores riscos)
ax1.set_title('10 Empregos Com Maiores Riscos de Automação', fontsize=16) # Título do gráfico
ax1.set_xlim(99.5, 100) # Definindo o limite do eixo x
ax1.set_xticks(np.arange(99.5, 100, 0.1)) # Determinando os pontos no gráfico no eixo x
ax1.tick_params(axis='y', labelrotation=25) # Rotacionando as labels do eixo y
ax1.spines[['top', 'right']].set_visible(False) # Retirando as linhas de cima e a direita do gráfico
ax1.set_xlabel('')
ax1.set_ylabel('')

# Gráfico 2 (Menores riscos)
ax2.set_title('10 Empregos Com Menores Riscos de Automação', fontsize=16) # Título do gráfico
ax2.set_xlim(0, 1) # Definindo o limite do eixo x
ax2.set_xticks(np.arange(0, 1, 0.1)) # Determinando os pontos no gráfico no eixo x
ax2.tick_params(axis='y', labelrotation=25) # Rotacionando as labels do eixo y
ax2.spines[['top', 'right']].set_visible(False) # Retirando as linhas de cima e a direita do gráfico
ax2.set_ylabel('')
ax2.set_xlabel('')


# Função para ajustar os gráficos na moldura
plt.tight_layout()
# Mostra os gráficos
plt.show()

"""## 3. Qual o número de vagas por impacto da IA?"""

# Agrupando a soma das vagas abertas por nível do impacto e resetando o índice
vagas_por_nivel = ai_job_df.groupby('AI Impact Level', as_index=False)['Job Openings (2024)'].sum()

# Renomeando as colunas
vagas_por_nivel.columns = ['Nível de Impacto', 'Total de Vagas Abertas']

# Formatando a coluna 'Total de Vagas Abertas' para milhar
vagas_por_nivel['Total de Vagas Abertas'] = vagas_por_nivel['Total de Vagas Abertas'].apply(lambda x: f"{x:,.0f}".replace(',', '.'))

vagas_por_nivel

"""## 4. Qual o salário médio por impacto da IA?"""

# Agrupando a média dos salários por impacto da IA
avg_salario_nivel = ai_job_df.groupby('AI Impact Level', as_index=False)['Median Salary (USD)'].mean()

# Renomeando as colunas
avg_salario_nivel.columns = ['Nível de Impacto', 'Salário Médio (USD)']

# Formatando os dados da coluna 'Salário Médio (USD)'
avg_salario_nivel['Salário Médio (USD)'] = avg_salario_nivel['Salário Médio (USD)'].apply(lambda x: f"{x:,.2f}".replace('.',',').replace(',','.',1))

avg_salario_nivel

"""## 5. Qual a distribuição de risco por nível educacional?"""

# Agrupando a média de risco por nível educacional a cada indústria
ai_job_df.groupby(['Industry', 'Required Education'])['Automation Risk (%)'].mean().round(2)

"""## 6. Qual a correlação entre risco de automação e salário?"""

ai_job_df.columns

# Criando análise
risco_por_salario = ai_job_df.groupby('Industry', as_index=False).agg({'Median Salary (USD)': 'mean',
                                                           'Automation Risk (%)': 'mean'})

# Formatando as colunas numéricas
risco_por_salario['Median Salary (USD)'] = risco_por_salario['Median Salary (USD)'].apply(lambda x: f'{x:,.2f}'.replace('.', ',').replace(',', '.', 1))
risco_por_salario['Automation Risk (%)'] = risco_por_salario['Automation Risk (%)'].apply(lambda x: f'{x:.2f}')

risco_por_salario.sort_values('Median Salary (USD)', ascending=False)