import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import trois_methodes as tm
import montecarlo as mc
#@st.cache

st.title("Calcul des intégrales par la méthode de montecarlo")
#coch=st.sidebar.checkbox("Opérations")
st.code("lambda x: input # input a fonction",language="python")#Code environnement
st.sidebar.title("Opérations")
fct=st.sidebar.text_input("Fonction",value="")
#fct=st.sidebar.text_area("Fonction",value="")
st.latex(fct)
dimension=st.sidebar.slider("Dimension ",1,100,1,1)


method=st.sidebar.radio("Méthodes",("empiriques","Montecarlo"),index=1)
if method=='empiriques':
	select_method=st.sidebar.radio('Méthode à utiliser',('rectangles',"Trapèzes","Simpson"))
iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,10)
# if dimension==1:
# 	f = lambda x : fct.getstr()
# 	born_inf=st.number_input("a ",0)
# 	born_sup=st.number_input("b ",0)
# 	st.write(tm.rectangles(f,born_inf,born_sup,iterations))
# elif dimmension==2:
# 	f= lambda x,y: fct
# else:
# 	f= lambda x,y,z: fct
code=st.sidebar.checkbox("Voir le Code source")
if code:
	st.write("see code?")
nb=st.text_input("nb",value=0)
resultat=0
if st.button("sin","sin"):
	resultat=st.write(np.sin(float(nb)))
if st.button("cos","cos"):
	resultat=st.write(np.cos(float(nb)))
if st.button("tan","tan"):
	resultat=st.write(np.tan(float(nb)))
st.text_area("resultats",resultat )
# if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
# 	st.latex(fct)
# else:
# 	st.latex("dimension:") 

st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale")
# if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
# 	st.latex(fct)
# else:
# 	st.latex("dimension:") 