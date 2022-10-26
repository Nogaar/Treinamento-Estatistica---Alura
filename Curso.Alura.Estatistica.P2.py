#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando pandas e lendo o dataset do projeto


# In[2]:


import pandas as pd


# In[3]:


dados = pd.read_csv('dados.Estatistica-P2.csv')


# In[4]:


dados.head()


# In[ ]:


#Distribuição de probabilidade
#bibliotecas https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html


# In[6]:


from scipy.special import comb


# In[ ]:


#exemplo Mega Sena
#Em um volante de loteria da Mega Sena temos um total de 60 números para escolher onde a aposta mínima é de seis números.


# In[7]:


combinacoes = comb(60, 6)
combinacoes


# In[8]:


probabilidade = 1 / combinacoes
print('%0.15f' % probabilidade)


# In[ ]:


#Exemplo :Corcurso
#Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha com 3 alternativas possíveis** em cada questão. 
#Cada questão tem o mesmo valor. 
#Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. 
#Assumindo que a prova vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato acertar 5 questões e também a probabilidade deste candidato passar para a próxima etapa do processo seletivo.


# In[9]:


n = 10
n


# In[10]:


#qual a probabilidade de sucesso  (p)?


# In[11]:


numero_de_alternativas_por_questao = 3
p = 1 / numero_de_alternativas_por_questao
p


# In[12]:


#Qual a probabilidade de fracasso(q)?


# In[13]:


q = 1 - p
q


# In[14]:


#qual o total de eventos que se deseja obter sucesso(k)?


# In[15]:


k = 5
k


# In[16]:


#solução 1


# In[17]:


probabilidade = (comb(n, k)) * (p ** k) * (q ** (n - k))
print('%0.8f' % probabilidade)


# In[18]:


#importando biblioteca
from scipy.stats import binom


# In[19]:


#solução 2


# In[20]:


probabilidade = binom.pmf(k, n, p)
print('%0.8f' % probabilidade)


# In[21]:


#obtendo a probabilidade do candidato passar


# In[22]:


binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)


# In[23]:


binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()


# In[24]:


1 - binom.cdf(4, n, p)


# In[25]:


binom.sf(4, n, p)


# In[26]:


#exemplo:Gincana
#Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. 
#Na última gincana se sabe que a proporção de participantes do sexo feminino foi de 60%.
#O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30. 
#Com as informações acima responda: Quantas equipes deverão ser formadas por 8 mulheres?


# In[29]:


p = 0.6
p


# In[30]:


n = 12
n


# In[31]:


k = 8
k


# In[32]:


probabilidade = binom.pmf(k, n, p)
print('%0.8f' % probabilidade)


# In[33]:


equipes = 30 * probabilidade
equipes


# In[34]:


#Exemplo:Delivery
#Um restaurante recebe em média 20 pedidos por hora.
#Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?


# In[47]:


#solução 1


# In[43]:


import numpy as np


# In[44]:


media = 20
media


# In[45]:


k=15
k


# In[46]:



probabilidade = ((np.e ** (-media)) * (media ** k)) / (np.math.factorial(k))
print('%0.8f' % probabilidade)


# In[48]:


#solução 2


# In[49]:


from scipy.stats import poisson

probabilidade = poisson.pmf(k, media)
print('%0.8f' % probabilidade)


# In[50]:


#construindo tabela normal padronizada


# In[51]:


import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada


# In[52]:


#Exemplo:Qual sua altura?
#Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1.
#Com estas informações obtenha o seguinte conjunto de probabilidades:

# A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

# B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

# C. probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.


# In[53]:


#obtendo a variável padronizada Z


# In[56]:


media = 1.7


# In[57]:


desvio_padrao = 0.1


# In[58]:


Z= (1.8 - media) / desvio_padrao
Z


# In[60]:


#solução 1 -Utilizando a tabela
probabilidade = 0.8413
probabilidade


# In[61]:


#solução 2 - Utilizando Scipy
from scipy.stats import norm
norm.cdf(Z)


# In[62]:


#Problema B 


# In[65]:


#obtendo a variavel padronizada Z
Z_inferior = (1.6 - media) / desvio_padrao
round(Z_inferior, 2)


# In[66]:


Z_superior = (1.8 - media) / desvio_padrao
round(Z_superior, 2)


# In[68]:


#Solução 1 - usando a tabela
probabilidade = (0.8413 - 0.5) * 2
probabilidade


# In[69]:


probabilidade = 0.8413 - (1 - 0.8413)
probabilidade


# In[71]:


#Solução 2 - Utilizando Scipy
probabilidade = norm.cdf(Z_superior) - (1 - norm.cdf(Z_superior))
probabilidade


# In[72]:


probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
probabilidade


# In[ ]:


#Problema C 


# In[73]:


Z = (1.9 - media) / desvio_padrao
Z


# In[74]:


#Solução 1 - usando a tabela
probabilidade = 1 - 0.9772
probabilidade


# In[75]:


#Solução 2 - Utilizando Scipy
probabilidade = 1 - norm.cdf(Z)
probabilidade


# In[76]:


probabilidade = norm.cdf(-Z)
probabilidade


# In[77]:


#AMOSTRAGEM


# In[78]:


#Amostragem Aleatoria Simples:
#É uma das principais maneiras de se extrair uma amostra de uma população. 
#A exigência fundamental deste tipo de abordagem é que cada elemeto da população tenha as mesmas chances de ser selecionado para fazer parte da amostra.


# In[79]:


dados.shape[0]


# In[80]:


dados.Renda.mean()


# In[81]:


amostra = dados.sample(n = 1000, random_state = 101)


# In[82]:


amostra.shape[0]


# In[83]:


amostra.Renda.mean()


# In[84]:


dados.Sexo.value_counts(normalize = True)


# In[85]:


amostra.Sexo.value_counts(normalize = True)


# In[86]:


#Teorema do Limite Central


# In[94]:


n = 2000
total_de_amostras = 1500


# In[96]:


amostras = pd.DataFrame()
amostras


# In[ ]:


for i in range(total_de_amostras):
  _ = dados.Idade.sample(n)
  _.index = range(0, len(_))
  amostras['Amostra_' + str(i)] = _

amostras


# In[99]:



amostras.mean()


# In[100]:


amostras.mean().hist()


# In[101]:


dados.Idade.mean()


# In[102]:


amostras.mean().mean()


# In[103]:


amostras.mean().std()


# In[104]:


dados.Idade.std()


# In[105]:


dados.Idade.std() / np.sqrt(n)


# In[ ]:


#Exemplo
#Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150 g.
#Selecionada uma amostra aleatório de 20 sacos de um lote específico, obteve-se um peso médio de 5.050 g.
#Construa um intervalo de confiança para a média populacional assumindo um nível de significância de 5%.


# In[108]:


#Media amostral
media_amostra = 5050


# In[109]:


#nivel de significancia
significancia =0.05
significancia


# In[110]:


#Nivel de confiança 
confianca = 1 - significancia
confianca


# In[111]:


#Obtendo z
tabela_normal_padronizada[16:26]


# In[112]:


0.95/2


# 
# 

# In[113]:


0.5 + (0.95 / 2)


# In[114]:


1.9 + 0.06


# In[115]:


z = norm.ppf(0.975)
z


# In[116]:


desvio_padrao = 150
desvio_padrao


# In[117]:


n = 20
n


# In[118]:


raiz_de_n = np.sqrt(n)
raiz_de_n


# In[119]:


sigma = desvio_padrao / raiz_de_n
sigma


# In[120]:


#obtendo e
e = z* sigma
e


# In[121]:


#Solução 1 -calculando o intervalo de confiança para a média
intervalo = (
  media_amostra - e,
  media_amostra + e  
)
intervalo


# In[122]:


#Solução 2 -Calculando o intervaolo de confiança para a média
norm.interval(alpha = 0.95, loc = media_amostra, scale = sigma)


# In[ ]:


#Exemplo: Rendimento medio
#Estamos estudando o rendimento mensal dos chefes de domicílios no Brasil.
#Nosso supervisor determinou que o erro máximo em relação a média seja de R$\$$ 100,00. 
#Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$\$$ 3.323,39.
#Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo?


# In[123]:


0.95 / 2


# In[124]:


0.5 + (0.95 / 2)


# In[125]:


z = norm.ppf(0.975)
z


# In[126]:


sigma = 3323.39
sigma


# In[127]:


e = 100
e


# In[128]:


n = (z * (sigma / e)) ** 2
int(n.round())


# In[129]:


#Exemplo: Industria de refrigerantes.
#Em um lote de 10.000 latas de refrigerante foi realizada uma amostra aleatória simples de 100 latas e foi obtido o desvio padrão amostral do conteúdo das latas igual a 12 ml.
#O fabricante estipula um erro máximo sobre a média populacional de apenas 5 ml. 
#Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?


# In[130]:


N = 10000
N


# In[131]:


z = norm.ppf((0.5+(0.95 / 2)))
z


# In[132]:


s = 12
s


# In[133]:


e = 5
e


# In[134]:


n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N - 1)))
int(n.round())


# In[ ]:




