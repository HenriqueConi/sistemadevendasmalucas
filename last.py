import streamlit as st
import pandas as pd
import plotly.express as px


tabela_de_Vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

st.sidebar.write("## Cadastrar Vendas ")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto =st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step = 1)
valor = st.sidebar.number_input("Valor")
butao_cadastrar = st.sidebar.button("CADASTRAR")


if butao_cadastrar:
    
   if valor <= 0:
    st.sidebar.warning("Venda não cadastrada") 
   else:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_de_Vendas)
    tabela_de_Vendas.loc[ultima_linha] = nova_venda
    tabela_de_Vendas.to_csv("vendas.csv", index= False)
    st.sidebar.success("Venda cadastrada")


st.write("## Vendas Cadastradas")
st.dataframe(tabela_de_Vendas)


st.write("## Dashboard")
faturamento = tabela_de_Vendas["valor"].sum()
st.metric("## Faturamento Total", f"R${faturamento}")

grafico1 = px.bar(tabela_de_Vendas, x="vendedor", y="valor", color="produto")
grafico1.update_layout(bargap = 0.1)
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_de_Vendas, names="produto" , values="valor", hole = 0.4)
st.plotly_chart(grafico2)