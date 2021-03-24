import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
#url = 'https://drive.google.com/file/d/11-Vikc67y348t3JsTi7IdV4raMTKZtBR/view?usp=sharing'
#path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
dadosDrive2018Partidos = pd.read_csv('https://raw.githubusercontent.com/gilvandrocesardemedeiros/DCA_UFRN_Data_Science/main/Data_To_Dashboard/Resumo_Eleitos_2018.csv')
#url2 = 'https://drive.google.com/file/d/1f1FCRUEOXmwY9c01ehC_ByK3cNIoeOdR/view?usp=sharing'
#path2 = 'https://drive.google.com/uc?export=download&id='+url2.split('/')[-2]
dadosDrive2018Sociais = pd.read_csv('https://raw.githubusercontent.com/gilvandrocesardemedeiros/DCA_UFRN_Data_Science/main/Data_To_Dashboard/Resumo_Perfil_Candidatos_2018.csv')
partidos = ["solidariedade", "pv", "avante", "cidadania", "dc", "dem", "mdb", "novo", "patriota", "pcb", "pcdob", "pco", "pdt", "phs", 
            "pl", "pmb", "pmn", "pode", "pp", "ppl", "pros", "prp", "prtb", "psb", "psc", "psd", "psdb", 
            "psl", "psol", "pstu", "pt", "ptb", "ptc", "rede", "republicanos", "up"]
partidos = [partido.upper() for partido in partidos]
ufs = ["ac","al","am","ap","ba","ce","df","es","go","ma","mg","ms","mt","pa","pb","pe","pi","pr","rj","rn",
     "ro","rr","rs","sc","se","sp","to","zz"]
ufs = [uf.upper() for uf in ufs]
Rd_Opcao = st.radio("Escolha uma opção:",["BRASIL","UF","PARTIDO"])
if Rd_Opcao == "BRASIL":#plot Geral do Pais
  Resumo_BRASIL = dadosDrive2018Partidos
  Res_BRASIL = go.Figure(go.Bar(y= Resumo_BRASIL['PARTIDO'], x=Resumo_BRASIL['DEPUTADO FEDERAL'], name='DEPUTADO FEDERAL', orientation='h'))
  Res_BRASIL.add_trace(go.Bar(y= Resumo_BRASIL['PARTIDO'], x=Resumo_BRASIL['DEPUTADO ESTADUAL'], name='DEPUTADO ESTADUAL', orientation='h'))
  Res_BRASIL.add_trace(go.Bar(y= Resumo_BRASIL['PARTIDO'], x = Resumo_BRASIL['GOVERNADOR'], name='GOVERNADOR', orientation='h'))
  Res_BRASIL.add_trace(go.Bar(y= Resumo_BRASIL['PARTIDO'], x = Resumo_BRASIL['SENADOR'], name='SENADOR', orientation='h'))
  Res_BRASIL.add_trace(go.Bar(y= Resumo_BRASIL['PARTIDO'], x = Resumo_BRASIL['PRESIDENTE'], name='PRESIDENTE', orientation='h'))
  Res_BRASIL.update_layout(barmode='stack',margin={"r":0.0,"t":0.0,"l":0,"b":0},yaxis={'categoryorder':'total ascending'})
  #Res_BRASIL.update_xaxes(categoryorder='category ascending',) 
  st.plotly_chart(Res_BRASIL)
  btnSocialBR = st.button("Caracteristicas Sociais")
  if btnSocialBR:#plot do perfil dos eleitos no Pais
    RES_Social = dadosDrive2018Sociais
    cor = RES_Social.DS_COR_RACA.value_counts()
    genero = RES_Social.DS_GENERO.value_counts()
    instrucao = RES_Social.DS_GRAU_INSTRUCAO.value_counts()
    figCor = px.pie(cor,cor.index,cor.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title="Etnia")
    st.plotly_chart(figCor)
    figGen = px.pie(genero,genero.index,genero.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title="Genero")
    st.plotly_chart(figGen)
    figInst = px.pie(instrucao,instrucao.index,instrucao.values,color_discrete_sequence=px.colors.sequential.Emrld,hole=0.5,title="Grau de instrução")
    st.plotly_chart(figInst)
elif Rd_Opcao == "PARTIDO":#plot Especifico de um partido 
  partido = st.selectbox("Escolha um partido? ",partidos)
  HPartido = st.header("Eleitos do partido "+partido)
  RES_partido = dadosDrive2018Partidos.loc[dadosDrive2018Partidos["PARTIDO"]==partido]
  Resumo_Partido = go.Figure(go.Bar(x= RES_partido['UF'], y=RES_partido['DEPUTADO FEDERAL'], name='DEPUTADO FEDERAL'))
  Resumo_Partido.add_trace(go.Bar(x= RES_partido['UF'], y=RES_partido['DEPUTADO ESTADUAL'], name='DEPUTADO ESTADUAL'))
  Resumo_Partido.add_trace(go.Bar(x= RES_partido['UF'], y = RES_partido['GOVERNADOR'], name='GOVERNADOR'))
  Resumo_Partido.add_trace(go.Bar(x= RES_partido['UF'], y = RES_partido['SENADOR'], name='SENADOR'))
  Resumo_Partido.add_trace(go.Bar(x= RES_partido['UF'], y = RES_partido['PRESIDENTE'], name='PRESIDENTE'))
  Resumo_Partido.update_layout(barmode='stack',xaxis={'categoryorder':'total descending'})
  #Resumo_Partido.update_xaxes(categoryorder='category ascending')

  st.plotly_chart(Resumo_Partido)
  btnDetalhar = st.button("Detalhar")
  btnSocialPartido = st.button("Caracteristicas Sociais")
  if btnDetalhar:
    figFed = px.bar(RES_partido,x = RES_partido['UF'],y = RES_partido['DEPUTADO FEDERAL'])
    figFed.update_layout(barmode='stack',xaxis={'categoryorder':'total descending'})
    st.plotly_chart(figFed)
    figEst = px.bar(RES_partido,x = RES_partido['UF'],y = RES_partido['DEPUTADO ESTADUAL'])
    figEst.update_layout(barmode='stack',xaxis={'categoryorder':'total descending'})    
    st.plotly_chart(figEst)
    figGov = px.bar(RES_partido,x = RES_partido['UF'],y = RES_partido['GOVERNADOR'])
    figGov.update_layout(barmode='stack',xaxis={'categoryorder':'total descending'})
    st.plotly_chart(figGov)
    figSen = px.bar(RES_partido,x = RES_partido['UF'],y = RES_partido['SENADOR'])
    figSen.update_layout(barmode='stack',xaxis={'categoryorder':'total descending'})
    st.plotly_chart(figSen)
  if btnSocialPartido:
    H_S_Partido = st.header("Caracteristicas sociais do partido "+partido)
    RES_SocialPartido = dadosDrive2018Sociais.loc[dadosDrive2018Sociais["SG_PARTIDO"]==partido]
    corPartido = RES_SocialPartido.DS_COR_RACA.value_counts()
    generoPartido = RES_SocialPartido.DS_GENERO.value_counts()
    instrucaoPartido = RES_SocialPartido.DS_GRAU_INSTRUCAO.value_counts()
    figCorPartido = px.pie(corPartido,corPartido.index,corPartido.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title='Etnia')
    st.plotly_chart(figCorPartido)
    figGenPartido = px.pie(generoPartido,generoPartido.index,generoPartido.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title='Genero')
    st.plotly_chart(figGenPartido)
    figInstPartido = px.pie(instrucaoPartido,instrucaoPartido.index,instrucaoPartido.values,color_discrete_sequence=px.colors.sequential.Emrld,hole=0.5,title='Grau de instrução')
    st.plotly_chart(figInstPartido)
elif Rd_Opcao == "UF":
  uf = st.selectbox("Escolha uma UF? ",ufs)
  RES_UF = dadosDrive2018Partidos.loc[dadosDrive2018Partidos["UF"]==uf]
  Resumo_UF = go.Figure(go.Bar(y= RES_UF['PARTIDO'], x=RES_UF['DEPUTADO FEDERAL'], name='DEPUTADO FEDERAL', orientation='h'))
  Resumo_UF.add_trace(go.Bar(y= RES_UF['PARTIDO'], x=RES_UF['DEPUTADO ESTADUAL'], name='DEPUTADO ESTADUAL', orientation='h'))
  Resumo_UF.add_trace(go.Bar(y= RES_UF['PARTIDO'], x = RES_UF['GOVERNADOR'], name='GOVERNADOR', orientation='h'))
  Resumo_UF.add_trace(go.Bar(y= RES_UF['PARTIDO'], x = RES_UF['SENADOR'], name='SENADOR', orientation='h'))
  #Resumo_UF.add_trace(go.Bar(y= RES_UF['PARTIDO'], x = RES_UF['PRESIDENTE'], name='PRESIDENTE', orientation='h'))
  Resumo_UF.update_layout(barmode='stack',margin={"r":0.0,"t":0.0,"l":0,"b":0},yaxis={'categoryorder':'total ascending'})
  #Resumo_UF.update_xaxes(categoryorder='category ascending') 
  st.plotly_chart(Resumo_UF)
  btnSocialUF = st.button("Ver caracteristicas Sociais")
  if btnSocialUF:
    H_S_Uf = st.header("Caracteristicas sociais do estado "+uf)
    RES_SocialUf = dadosDrive2018Sociais.loc[dadosDrive2018Sociais["SG_UF"]==uf]
    corUf = RES_SocialUf.DS_COR_RACA.value_counts()
    generoUf = RES_SocialUf.DS_GENERO.value_counts()
    instrucaoUf = RES_SocialUf.DS_GRAU_INSTRUCAO.value_counts()
    figCorUf = px.pie(corUf,corUf.index,corUf.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title='Etnia')
    st.plotly_chart(figCorUf)
    figGenUf = px.pie(generoUf,generoUf.index,generoUf.values,color_discrete_sequence=px.colors.sequential.RdBu,hole=0.5,title='Genero')
    st.plotly_chart(figGenUf)
    figInstUf = px.pie(instrucaoUf,instrucaoUf.index,instrucaoUf.values,color_discrete_sequence=px.colors.sequential.Emrld,hole=0.5,title='Grau de instrução')
    st.plotly_chart(figInstUf)
    

