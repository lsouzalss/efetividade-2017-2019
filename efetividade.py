import streamlit as st
import numpy as np
import pandas as pd
import keras
from keras.models import load_model

model = load_model('rede.h5')

def welcome():
	return 'Welcome All'

def predict(resultados, produtos_e_servicos, contexto, planejamento, insumos, processos):
	
 
	previsao = model.predict([[resultados,produtos_e_servicos,contexto,planejamento,insumos,processos]])
	print(previsao)
	return previsao

def main():
	st.title('Previsão de Índice de Efetividade')
	html_temp = """
	<div style='background-color:green;padding:10px'>
	<h2 style='color:white;text-align:center;'>Sistema de Análise e Monitoramento de Gestão - SAMGe </h2>
	</div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	resultados = st.number_input('Indicador Resultados (digite um valor entre 0 e 1):')
	produtos_e_servicos = st.number_input('Indicador Produtos e Serviços (digite um valor entre 0 e 1):')
	contexto = st.number_input('Indicador Contexto (digite um valor entre 0 e 1):')
	planejamento = st.number_input('Indicador Planejamento (digite um valor entre 0 e 1):')
	insumos = st.number_input('Indicador Insumos (digite um valor entre 0 e 1):')
	processos = st.number_input('Indicador Processos (digite um valor entre 0 e 1):')
	result = ""
	if st.button('Prever'):
		result = predict(resultados, produtos_e_servicos, contexto, planejamento, insumos, processos).round(2) * 100
	st.success('O índice de efetividade previsto é de: {}'.format(result))
	if st.button('Algoritmo e Métricas'):
		st.write('Framework: Tensorflow/Keras')
		st.write('Mean Squared Error (MSE): 9,812592463715363e-05')
		st.write('Root Mean Squared Error (RMSE): 0,00990585304944272')
	if st.button('Sobre'):
		st.write('Desenvolvido por DMAG/COGEP/CGPLAN/DIPLAN/ICMBio. Visite http://samge.icmbio.gov.br/')

if __name__=='__main__':
	main()


