from IPython.display import display
import plotly.express as px 
import pandas as pd 

df = pd.read_csv("telecom_users.csv")
display(df)
df = df.drop('Unnamed: 0', axis=1)
display(df)
print(df.info())
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors= 'coerce')
print(df.info())
df = df.dropna(how= 'all', axis= 1)
df = df.dropna()
display(df['Churn'].value_counts())
display(df['Churn'].value_counts(normalize= True))
display(df['Churn'].value_counts(normalize= True).map('{:.1%}'.format))
for coluna in df:
    if coluna != 'customerID':
        fig = px.histogram(df, x=coluna, color= 'Churn',text_auto=True)
        fig.show()
        # display(df.pivot_table(index= 'Churn', columns= coluna, aggfunc='count')['customerID'])

""" 
- CLientes que estão há pouco tempo estão cancelando muito
    - Pode tá fazendo alguma promoção que tá dando o 18 mes de graça
    - O início do servico pro cliente tá sendo muito confuso
    - A 1ª experiencia do cliente tá ruim
    - Podemos criar incentivos nos primeiros meses - primeiro ano mais barato

- Boleto eletrônico tem MUITO mais cancelamento do que as outras formas de pagamento
    - Ofercer desconto nas outras formas de pagamento

- Clientes com contrato mensal tem MUITO mais chance de cancelar
    - Dá desconto pra pagar a anuidade

- Quanto mais servicos o cliente tem, menor a chance dele cancelar
    - Pode oferecer serviços extras quase de graça

- Clientes com mais linhas com família maior tem menos chance de cancelar
    - 2ª linha de graça ou com desconto
"""
