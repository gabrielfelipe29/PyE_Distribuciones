from scipy.stats import binom, geom, poisson
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Elimina aviso sobre cantidad de figuras generadas
plt.rcParams.update({'figure.max_open_warning': 0})

# Funcion para graficar los diagramas de caja
def diagrama_caja(datos, titulo, xlabel, ylabel, geometrica):
    fig, ax = plt.subplots()

    
    box = ax.boxplot(datos, patch_artist=True, vert=True, widths = 0.6)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks([1,2,3,4],["100","1.000","10.000","100.000"])
        
    colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    i=0
    for xtick in ax.get_xticks():
        median = np.median(datos[i])
        q1 = np.percentile(datos[i], 25)
        q3 = np.percentile(datos[i], 75)
        if(geometrica==True):        
            plt.ylim(0, 140)
            ax.text(xtick, median + 2, f'{median:.2f}',  horizontalalignment='left', va="top", size=5, color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
            ax.text(xtick, q1 - 2, f'{q1:.2f}', horizontalalignment='left', va="bottom", size=5,color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
            ax.text(xtick, q3 + 4, f'{q3:.2f}', horizontalalignment='left', va="top", size=5, color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
        else:
            ax.text(xtick, median, f'{median:.2f}',  horizontalalignment='left', va="top", size=5, color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
            ax.text(xtick, q1, f'{q1:.2f}', horizontalalignment='left', va="bottom", size=5,color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
            ax.text(xtick, q3, f'{q3:.2f}', horizontalalignment='left', va="top", size=5, color='k', weight='semibold', bbox=dict(facecolor='lightgray', pad=2))
        i+=1
    plt.savefig(f'{titulo}.png')

# Funcion para graficar el histograma
def histograma(datos, titulo, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.hist(datos, color='blue', bins=100, edgecolor='black')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f'Histograma {titulo}.png')

# Funcion para la distribucion binomial
def binomial(n, p, veces):
    print(f"Binomial {veces}: ")
    # Generar los datos
    b=binom.rvs(n,p,size=veces)

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
    return b

# Funcion para la distribucion geometrica
def geometrica(p, veces):
    print(f"Geométrica {veces}: ")
    # Generar los datos
    g=geom.rvs(p,size=veces)

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
    return g

# Funcion para la distribucion de poisson
def pois(l, veces):
    print(f"Poisson {veces}: ")
    # Generar los datos
    p=poisson.rvs(l,size=veces)

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
    return p

# Definicion de arreglos para guardar repeticiones
bin=[]
geo=[]
pos=[]


# Binomial
p=0.35
n=100

bin.append(binomial(n,p,100))
bin.append(binomial(n,p,1000))
bin.append(binomial(n,p,10000))
bin.append(binomial(n,p,100000))

diagrama_caja(bin,"Diagrama de caja Binomial", "Repeticiones", "Frecuencia absoluta", False)

# Geometrica
p=0.08
geo.append(geometrica(p,100))
geo.append(geometrica(p,1000))
geo.append(geometrica(p,10000))
geo.append(geometrica(p,100000))

diagrama_caja(geo,"Diagrama de caja Geométrica", "Repeticiones", "Frecuencia absoluta", True)


# Poisson
l=30
pos.append(pois(l,100))
pos.append(pois(l,1000))
pos.append(pois(l,10000))
pos.append(pois(l,100000))

diagrama_caja(pos,"Diagrama de caja Poisson", "Repeticiones", "Frecuencia absoluta", False)
