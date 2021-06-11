#Radosław Budek 310798
#Jelizawieta Micewicz 311063
https://github.com/masterlu12/21L_WFIT_Budek_Micewicz
import matplotlib.pyplot as plt
import numpy as np

def calculating(r, t):
    x = r[0]
    y = r[1]
    fxd = x * (a - b * y)
    fyd = y * (d * x - c)
    result = np.array([fxd, fyd])
    return result

def rungekutta(r, t, h):
    k1 = h * calculating(r, t)
    k2 = h * calculating(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * calculating(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * calculating(r + k3, t + h)
    kf = (k1 + 2 * k2 + 2 * k3 + k4)/6
    return kf



a = float(input("Przyrost ofiar "))
b = float(input("Polowania "))
c = float(input("Wymieranie drapieznikow "))
d = float(input("Przyrost drapieznikow "))
tf = float(input("Zakres czasu "))
h = float(input("Krok czasu "))
x0 = float(input("Startowe ofiary "))
y0 = float(input("Startowi drapieżnicy "))

#tworzymy przestrzen czasu i punkt początkowy
r = np.array([x0, y0], float)
tline = np.arange(0,tf,h)

#tablice na wartości do rysowania
xlist = []
ylist = []
for i in tline:
    xlist.append(r[0])
    ylist.append(r[1])
    r += rungekutta(r, i, h)

plt.plot(tline, xlist, "m-", label = "Ofiary")
plt.plot(tline, ylist, "r-",label = "Drapieżnicy")
plt.grid()
plt.legend(loc='best')
plt.xlabel("Czas")
plt.ylabel("Populacje")
plt.title("Ofiary - Drapieżnicy")
plt.show()


plt.plot(ylist, xlist, "b-")
plt.xlabel("Drapieżnicy")
plt.ylabel("Ofiary")
plt.title("Ofiary - Drapieżnicy")
plt.grid()
plt.show()


