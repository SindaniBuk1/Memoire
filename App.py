import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from math import *
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
#st.balloons()
def mc_moy(f,a,b,N):
    x=np.random.uniform(a,b,N)
    y=[]
    for k in range(N):
        y.append(f(x[k]))
    df=(x,y)
    return (b-a)*sum(y)/N,df
def montecarlo(f,a,b,N):
    n=0
    S=(b-a)*np.max(f(np.linspace(a,b,1000000)))
    x=np.random.uniform(a,b,N)
    y=np.random.uniform(0,np.max(f(np.linspace(a,b,N))),N)
    for i in range(N):
        if (y[i]<=f(x[i])):
            n=n+1
    return S*n/N
def mc_2d(f,N):
    x_1,x_2=np.random.uniform(0,1,N),np.random.uniform(0,1,N)
    z=[]
    for k in range(N):
        z.append(f(x_1[k],x_2[k]))
    df=x_1,x_2,z
    return sum(z)/N,df
def mc_3d(f,N):
    x_1,x_2,x_3=np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N)
    z=[]
    for k in range(N):
        z.append(f(x_1[k],x_2[k],x_3[k]))
    df=x_1,x_2,x_3,z
    return sum(z)/N,df
def mc_4d(f,N):
    x_1,x_2,x_3,x_4=np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N)
    z=[]
    for k in range(N):
        z.append(f(x_1[k],x_2[k],x_3[k],x_4[k]))
    df=x_1,x_2,x_3,x_4,z
    return sum(z)/N,df
def mc_5d(f,N):
    x_1,x_2,x_3,x_4,x_5=np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N),np.random.uniform(0,1,N)
    z=[]
    for k in range(N):
        z.append(f(x_1[k],x_2[k],x_3[k],x_4[k],x_5[k]))
    df=x_1,x_2,x_3,x_4,x_5,z
    return sum(z)/N,df
st.title("Calcul des intégrales par la méthode de montecarlo")
st.sidebar.title("Opérations")
dimension=st.sidebar.number_input("Dimension ",1)
x=Symbol('x')
y=Symbol("y")
z=Symbol("z")
t=Symbol("t")
u=Symbol("u")
if dimension==1:
	fct1d="f=lambda x :"
	fct=st.sidebar.text_input("f(x)",value="x")
	fonction=fct1d+fct.lower()
	exec((fonction))
	f_s=sympify(fct.lower())
	if st.checkbox("Voir la primitive"):
		txt="\int "+latex(sympify(fct.lower()))+"dx="+latex(integrate(f_s,x))
		st.latex(txt)
		#st.write(integrate(f_s,x))
	iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,100)
	a=st.sidebar.number_input('a',-1.000)
	b=st.sidebar.number_input('b',0.0000)
	f_s=sympify(fct)
	if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
		I,df=mc_moy(f,a,b,iterations)
		txt="\int_{"+str(a)+"}^{"+str(b)+"}"+latex(sympify(fct.lower()))+"dx="+str(I)
		st.latex(txt)
		fig, ax = plt.subplots()
		ax.scatter(df[0],df[1],lw=1,color='green')
		st.pyplot(fig)
elif dimension==2:
	fct2d="f=lambda x, y :"
	fct=st.sidebar.text_input("f(x,y)",value="x")
	fonction=fct2d+fct.lower()
	exec(fonction)
	iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,100)
	f_s=sympify(fct.lower())
	if st.checkbox("Voir la primitive"):
		txt="\iint ("+latex(sympify(fct.lower()))+")dxdy="+latex(integrate(f_s,x,y))
		st.latex(txt)
	if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
		I,df=mc_2d(f,iterations)
		txt="\iint_{[0,1]^{ "+str(dimension)+"}}"+"("+latex(sympify(fct.lower()))+")dxdy="+str(I)
		st.latex(txt)
		fig = px.scatter_3d(df, x=df[0], y=df[1], z=f(df[0],df[1]))
		st.write(fig)
elif dimension==3:
	fct3d="f=lambda x, y,z :"
	fct=st.sidebar.text_input("f(x,y,z)",value="x")
	fonction=fct3d+fct.lower()
	exec(fonction)
	f_s=sympify(fct.lower())
	if st.checkbox("Voir la primitive"):
		txt="\iiint ("+latex(sympify(fct.lower()))+")dxdydz="+latex(integrate(f_s,x,y,z))
		st.latex(txt)
	iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,100)
	if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
		I,df=mc_3d(f,iterations)
		txt="\iiint_{[0,1]^{ "+str(dimension)+"}}"+"("+latex(sympify(fct.lower()))+")dxdydz="+str(I)
		st.latex(txt)
elif dimension==4:
	fct4d="f=lambda x, y,z,t :"
	fct=st.sidebar.text_input("f(x,y,z,t)",value="x")
	fonction=fct4d+fct.lower()
	exec(fonction)
	f_s=sympify(fct.lower())
	if st.checkbox("Voir la primitive"):
		txt="\int ("+latex(sympify(fct.lower()))+")dxdydzdt="+latex(integrate(f_s,x,y,z,t))
		st.latex(txt)
	iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,100)
	if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
		I,df=mc_4d(f,iterations)
		txt="\int_{[0,1]^{ "+str(dimension)+"}}"+"("+latex(sympify(fct.lower()))+")dxdydzdt="+str(I)
		st.latex(txt)
elif dimension==5:
	fct5d="f=lambda x, y,z,t,u :"
	fct=st.sidebar.text_input("f(x,y,z,t,u)",value="x")
	fonction=fct5d+fct
	exec(fonction)
	f_s=sympify(fct)
	if st.checkbox("Voir la primitive"):
		txt="\int("+latex(sympify(fct.lower()))+")dxdydzdtdu="+latex(integrate(f_s,x,y,z,t,u))
		st.latex(txt)
	iterations=st.sidebar.number_input("Nombre d'itérations",3,1000000,100)
	if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
		I,df=mc_5d(f,iterations)
		txt="\int_{[0,1]^{ "+str(dimension)+"}}"+"("+latex(sympify(fct.lower()))+")dxdydzdtdu="+str(I)
		st.latex(txt)



		# x,y=df[0],df[1]
		# z=f(x,y)
		# x,y=np.meshgrid(x,y)
		# fig, ax = plt.subplots()
  #   	ax=plt.axes(projection='3d')
  #   	ax.plot_surface(x,y,z,cmap='plasma')
  #   	ax.scatter3D(x,y,z,color="green")
  #   	st.pyplot(fig)
		

		
# if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
# 	st.latex(fct)
# else:
# 	st.latex("dimension:") 
# if st.button("sin","sin"):
# 	resultat=st.write(np.sin(float(nb)))
# if st.button("cos","cos"):
# 	resultat=st.write(np.cos(float(nb)))
# if st.button("tan","tan"):
# 	resultat=st.write(np.tan(float(nb)))
# if st.button("Exp()","exp"):
# 	resultat=st.write(np.exp(float(nb)))
# if st.button("ln","ln"):
# 	resultat=st.write(np.log(float(nb)))
# if st.button("log_10","log"):
# 	resultat=st.write(np.log10(float(nb)))
# st.text_area("resultats",resultat )
# if st.button("Calculer","compute",help="Appuyez pour calculer l'intégrale"):
# 	st.latex(fct)
# else:
# 	st.latex("dimension:") 
# if dimension==1:
# 	f = lambda x : fct.getstr()
# 	born_inf=st.number_input("a ",0)
# 	born_sup=st.number_input("b ",0)
# 	st.write(tm.rectangles(f,born_inf,born_sup,iterations))
# elif dimmension==2:
# 	f= lambda x,y: fct
# else:
# 	f= lambda x,y,z: fct
#data=st.file_uploader("Browse xls",type="xlsx")
