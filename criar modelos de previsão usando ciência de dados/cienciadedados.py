from IPython.display import display
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pandas as pd

tabela = pd.read_csv('advertising.csv')
# display(tabela)

display(tabela.corr())

#Criar o gráfico
sns.heatmap(tabela.corr(), cmap= 'Wistia', annot= True)

#exibir o gráfico
plt.show()

# y -> Quem você quer prever (Vendas)
# x -> é o resto todo (quem você vai usar pra fazer a previsão)

x = tabela[['TV', 'Radio', 'Jornal']]
y = tabela['Vendas']


x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size= 0.3)

#Cria a inteligencia artificial 
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#Treina a inteligencia artificial 
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


#Fazer previsão
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))

#Visualização Gráfica das Previsões 
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste 
tabela_auxiliar['arvore decisao'] = previsao_arvoredecisao 
tabela_auxiliar['regressao linear'] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data= tabela_auxiliar)
plt.show()


#Como fazer uma nova previsão? 
#O melhor modelo é a arvore de decisão
novos = pd.read_csv('novos.csv')
display(novos)

print(modelo_arvoredecisao.predict(novos))