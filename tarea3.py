from scipy.stats import binom, geom, poisson
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


# Funcion para graficar los diagramas de caja
def diagrama_caja(datos, titulo, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.boxplot(datos, vert = True)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f'Diagrama de caja {titulo}.png')

# Funcion para graficar el histograma
def histograma(datos, titulo, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.hist(datos, color='blue', edgecolor='black')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f'Histograma {titulo}.png')

# Funcion para la distribucion binomial
def binomial(n, p, veces):
    print(f"Binomial {veces}: ")
    # Generar los datos
    b=binom.rvs(n,p,size=veces)
    # Generar diagrama de caja
    diagrama_caja(b, f"Binomial {veces}", "", "Frecuencia absoluta")
    # Generar histograma
    histograma(b, f"Binomial {veces}", "Cantidad de éxitos", "Frecuencia absoluta")

    # Calcular moda y mediana
    moda = stats.mode(b)[0]
    print("Moda: ", moda)
    mediana=np.median(b)
    print("Mediana: ", mediana)

    # Calcular media empirica y esperanza
    media_empirica= np.mean(b)
    esperanza =  binom.mean(n,p)
    print("Media empirica :", media_empirica)
    print("Esperanza: ", esperanza)

    # Calcular varianza empirica y teorica
    varianza_empirica=np.var(b)
    varianza_teorica = binom.var(n,p)
    print("Varianza empirica: ", varianza_empirica)
    print("Varianza teórica: ", varianza_teorica)
    print("\n")

# Funcion para la distribucion geometrica
def geometrica(p, veces):
    print(f"Geométrica {veces}: ")
    # Generar los datos
    g=geom.rvs(p,size=veces)

    # Generar diagrama de caja
    diagrama_caja(g, f"Geométrica {veces}", "", "Frecuencia absoluta")
    # Generar histograma
    histograma(g, f"Geométrica {veces}", "Cantidad de éxitos", "Frecuencia absoluta")

    # Calcular moda y mediana
    moda = stats.mode(g)[0]
    print("Moda: ", moda)
    mediana=np.median(g)
    print("Mediana: ", mediana)

    # Calcular media empirica y esperanza
    media_empirica= np.mean(g)
    esperanza =  geom.mean(p)
    print("Media empirica :", media_empirica)
    print("Esperanza: ", esperanza)

    # Calcular varianza empirica y teorica
    varianza_empirica=np.var(g)
    varianza_teorica = geom.var(p)
    print("Varianza empirica: ", varianza_empirica)
    print("Varianza teórica: ", varianza_teorica)
    print("\n")

# Funcion para la distribucion de poisson
def pois(l, veces):
    print(f"Poisson {veces}: ")
    # Generar los datos
    p=poisson.rvs(l,size=veces)

    # Generar diagrama de caja
    diagrama_caja(p, f"Poisson {veces}", "", "Frecuencia absoluta")
    # Generar histograma
    histograma(p, f"Poisson {veces}", "Cantidad de éxitos", "Frecuencia absoluta")

    # Calcular moda y mediana
    moda = stats.mode(p)[0]
    print("Moda: ", moda)
    mediana=np.median(p)
    print("Mediana: ", mediana)

    # Calcular media empirica y esperanza
    media_empirica= np.mean(p)
    esperanza =  poisson.mean(l)
    print("Media empirica :", media_empirica)
    print("Esperanza: ", esperanza)

    # Calcular varianza empirica y teorica
    varianza_empirica=np.var(p)
    varianza_teorica = poisson.var(l)
    print("Varianza empirica: ", varianza_empirica)
    print("Varianza teórica: ", varianza_teorica)
    print("\n")

# Binomial
p=0.35
n=100
binomial(n,p,100)
binomial(n,p,1000)
binomial(n,p,10000)
binomial(n,p,100000)

# Geometrica
p=0.08
geometrica(p,100)
geometrica(p,1000)
geometrica(p,10000)
geometrica(p,100000)

# Poisson
l=30
pois(l,100)
pois(l,1000)
pois(l,10000)
pois(l,100000)