#!/usr/bin/env python
# coding: utf-8


#importando pandas e lendo o DataSet do projeto

import pandas as pd

dados= pd.read_csv("dados.Estatística_P1.csv")

dados.head()

#Variaveis qualitativas ordinais
# podem ser ordenadas ou hierarquizadas

sorted(dados['Anos de Estudo'].unique())

#Variáveis qualitativas nominais
#não podem ser ordenadas ou hirarquizadas

sorted(dados['UF'].unique())

sorted(dados['Sexo'].unique())

sorted(dados['Cor'].unique())

#Variaveis quatitativas discretas
#representam uma contagem onde os valores possiveis formam um conjunto finito ou enumerável

print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))

# a variavel idade pode ser classificada em três formas:
#discreta,continua e ordinal

print('De %s até %s metros ' % (dados['Altura'].min(), dados.Altura.max(
)))

#distribuição de frequências 

#metodo1 https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.Series.value_counts.html

dados['Sexo'].value_counts()

dados['Sexo'].value_counts(normalize = True) * 100

frequencia = dados['Sexo'].value_counts()

percentual = dados['Sexo'].value_counts(normalize = True) * 100

dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
dist_freq_qualitativas 


dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)
dist_freq_qualitativas.rename_axis('Sexo', axis= 'columns', inplace = True)
dist_freq_qualitativas 

#método 2 https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.crosstab.html

sexo = {0: 'Masculino', 
        1: 'Feminino'}

cor = {0: 'Indígena', 
       2: 'Branca', 
       4: 'Preta', 
       6: 'Amarela', 
       8: 'Parda', 
       9: 'Sem declaração'}

frequencia = pd.crosstab(dados.Sexo,
                         dados.Cor)
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
frequencia


percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         normalize = True) * 100
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual

percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         aggfunc = 'mean',
                         values = dados.Renda)
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual

#Distribuição de frequências para variáveis quantitativas

dados.Renda.min()


dados.Renda.max()


classes = [0, 1576, 3152, 7880, 15760, 200000]


labels = ['E', 'D', 'C', 'B', 'A']

#criar tabela de frequência https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.cut.html

frequencia = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True)
)
frequencia



percentual = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True),
  normalize = True
)
percentual

dist_freq_quantitativas_personalizadas = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativas_personalizadas


dist_freq_quantitativas_personalizadas.sort_index(ascending = False)

#Distribuição de frequências para variáveis quantitativas (classes de amplitude fixa)

import numpy as np
#biblioteca usada para calculos

#defininado o número de classes


n = dados.shape[0]
n


k = 1 + (10 /3) * np.log10(n)
k


k = int(k.round(0))
k

#criar a tabela de frequências 

frequencia = pd.value_counts(
  pd.cut(
    x = dados.Renda,
    bins = 17,
    include_lowest = True
  ),
  sort = False
)

percentual = pd.value_counts(
  pd.cut(
    x = dados.Renda,
    bins = 17,
    include_lowest = True
  ),
  sort = False,
  normalize = True
)
percentual


dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativas_amplitude_fixa


#HISTOGRAMA
#biblioteca seaborn https://seaborn.pydata.org/

import seaborn as sns

ax = sns.distplot(dados.Altura, kde = False)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

ax = sns.distplot(dados.Altura)


ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura - KDE', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

dados.Altura.hist(bins = 50, figsize=(12, 6))


req_quantitativas_personalizadas


dist_freq_quantitativas_personalizadas['Frequência'].plot.bar(width= 1, color = 'blue', alpha = 0.2, figsize=(12, 6))

#Medidas de tendência central


df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]}, 
                  index = ['Matemática', 
                           'Português', 
                           'Inglês', 
                           'Geografia', 
                           'História', 
                           'Física', 
                           'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
df

(8 + 10 + 4 + 8 + 6 + 10 + 8) / 7


df['Fulano'].mean()


dados.Renda.mean()


dados.groupby(['Sexo'])['Renda'].mean()

#Mediana 

#N impar

notas_fulano = df.Fulano
notas_fulano


notas_fulano = notas_fulano.sort_values()
notas_fulano

notas_fulano = notas_fulano.reset_index()
notas_fulano


n = notas_fulano.shape[0]
n


elemento_md = (n + 1) / 2
elemento_md

notas_fulano.loc[elemento_md - 1]


notas_fulano.median()


#N par


notas_beltrano = df.Beltrano.sample(6, random_state = 101)
notas_beltrano

notas_beltrano = notas_beltrano.sort_values()
notas_beltrano


notas_beltrano = notas_beltrano.reset_index()
notas_beltrano


n = notas_beltrano.shape[0]
n


elemento_md = n / 2
elemento_md


(notas_beltrano.Beltrano[elemento_md - 1] + notas_beltrano.Beltrano[elemento_md]) / 2


notas_beltrano.median()


#Obtendo a mediana em nosso dataset

dados.Renda.median()


dados.Renda.quantile()

#moda
# valor mais frequente de um conjunto de dados 


df.mode()

exemplo = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 7])
exemplo


exemplo.mode()

#Obtendo a moda pelo dataset

dados.Renda.mode()


dados.Altura.mode()


#Relação entre média,mediana e moda


#Avaliando a variável RENDA



ax = sns.distplot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)
ax


Moda = dados.Renda.mode()[0]
Moda


Mediana = dados.Renda.median()
Mediana


Media = dados.Renda.mean()
Media


Moda < Mediana < Media


#Avaliando a variavel Altura

ax = sns.distplot(dados.Altura)
ax.figure.set_size_inches(12, 6)
ax


Moda = dados.Altura.mode()
Moda


Mediana = dados.Altura.median()
Mediana


Media = dados.Altura.mean()
Media

#Avaliando a variável ANOS DE ESTUDO


ax = sns.distplot(dados['Anos de Estudo'], bins = 17)
ax.figure.set_size_inches(12, 6)
ax

Moda = dados['Anos de Estudo'].mode()[0]
Moda

Mediana = dados['Anos de Estudo'].median()
Mediana

Media = dados['Anos de Estudo'].mean()
Media

Moda > Mediana > Media


#MEDIDAS SEPARATRIZES


#Quartis, decis e percentis
#Há uma série de medidas de posição semelhantes na sua concepção à mediana, embora não sejam medidas de tendência central. 
#Como se sabe, a mediana divide a distribuição em duas partes iguais quanto ao número de elementos de cada parte. 
#Já os quartis permitem dividir a distribuição em quatro partes iguais quanto ao número de elementos de cada uma;
#os decis em dez partes e os centis em cem partes iguais.

dados.Renda.quantile([0.25, 0.5, 0.75])

[i / 10 for i in range(1, 10)]


dados.Renda.quantile([i / 10 for i in range(1, 10)])

dados.Renda.quantile([i / 100 for i in range(1, 100)])

ax = sns.distplot(dados.Idade, 
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True},
                  bins = 10)
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
ax

dados.Idade.quantile([i / 10 for i in range(1, 10)])

#Box-Plot
#(O box plot dá uma idéia da posição, dispersão, assimetria, caudas e dados discrepantes (outliers).
#A posição central é dada pela mediana e a 
#dispersão por $IIQ$. As posições relativas de $Q1$, $Mediana$ e $Q3$ dão uma noção da simetria da distribuição.
#Os comprimentos das cauda são dados pelas linhas que vão do retângulo aos valores remotos e pelos valores atípicos.

ax = sns.boxplot(x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

ax = sns.boxplot(x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

ax = sns.boxplot(x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax

ax = sns.boxplot(x = 'Renda', y = 'Sexo', data = dados.query('Renda < 10000'), orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


ax = sns.boxplot(x = 'Anos de Estudo', data = dados, orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


ax = sns.boxplot(x = 'Anos de Estudo', y = 'Sexo', data = dados, orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


#Medidas de dispersão

#Desvio médio absoluto

notas_fulano = df[['Fulano']]
notas_fulano

nota_media_fulano = notas_fulano.mean()[0]
nota_media_fulano

notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano

notas_fulano['Desvio'].sum()

notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano

ax = notas_fulano['Fulano'].plot(style = 'o')
ax.figure.set_size_inches(14, 6)
ax.hlines(y = nota_media_fulano, xmin = 0, xmax = notas_fulano.shape[0] - 1, colors='red')
for i in range(notas_fulano.shape[0]):
    ax.vlines(x = i, ymin = nota_media_fulano, ymax = notas_fulano['Fulano'][i], linestyles='dashed')
ax

notas_fulano['|Desvio|'].mean()


desvio_medio_absoluto = notas_fulano['Fulano'].mad()
desvio_medio_absoluto


#Variância

notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)
notas_fulano

notas_fulano['(Desvio)^2'].sum() / (len(notas_fulano) - 1)


variancia = notas_fulano['Fulano'].var()
variancia

#Desvio padrão


np.sqrt(variancia)

desvio_padrao = notas_fulano['Fulano'].std()
desvio_padrao

df

df.mean()

df.median()

df.mode()


df.std()





