import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def N_Sturges(n):
    return 1+(np.log(n))/np.log(2)

# Grafico del histograma con Gaussiana, normalizado a 1. (Histograma de Frecuencias)
def GraficoHistGauss(Datos_X, CantBins, ColorBordeHist="black", ColorDentroHist="orange", ColorGauss="darkcyan", XLabel="Datos X", YLabel="Frencuencia"):
    # Histograma por frecuencias
    cuentas, bins = np.histogram(Datos_X, bins=CantBins)

    N = cuentas.sum()
    cuentas = cuentas / N  # normalizo a frecuencias
    plt.bar(bins[:-1], cuentas, width=np.diff(bins), align="edge", color=ColorDentroHist, edgecolor=ColorBordeHist)
    
    # Gaussiana "desnormalizada"
    t = np.linspace(min(Datos_X), max(Datos_X), 100)
    y = stats.norm(loc=np.mean(Datos_X), scale=np.std(Datos_X)).pdf(t)
    y = y * np.diff(bins)[0]
    plt.plot(t, y, color=ColorGauss)
    plt.xlabel(str(XLabel))
    plt.ylabel(str(YLabel))
    plt.show()

