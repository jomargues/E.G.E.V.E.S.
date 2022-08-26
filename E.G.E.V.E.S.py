######################################################################################################

# E.G.E.V.E.S. (Engenharia de Gap Eletrônico Via Excitações de Stoner)

######################################################################################################

# Importação de Módulos

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from math import pi

######################################################################################################

# Funções

def updateU_Off(val):

    Eup = -Off_slider.val + np.cos(a * kup + pi) + U_slider.val
    Edown = -Off_slider.val + np.cos(a * kdown + pi)

    Bup.set_ydata(Eup)
    Bdown.set_ydata(Edown)

    E = []
    Q = []

    for i in kup:
        iup = np.argwhere(kup == i)

        for j in kdown:
            idown = np.argwhere(kdown == j)

            if (Eup[iup] > Edown[idown]) and (Eup[iup] > 0):
                Q.append(i - j)
                E.append(Eup[iup] - Edown[idown])

    Enovo = [x[0] for x in E]

    ax2 = plt.subplot(222)
    ax2.set_xlabel('Vetor de Espalhamento (q)')
    ax2.set_ylabel('Energia')
    ax2.clear()
    T = ax2.scatter(Q, Enovo, s=1, alpha=0.3, color='black')
    plt.xlim(0, pi / a)
    plt.ylim(0, 3.5)
    ax2.set_title('Excitações')

    fig.canvas.draw_idle()

######################################################################################################

# Desenvolvimento

a = 1

Umin = 0
Uinit = 1
Umax = 5

Offmin = 0
Offinit = 1
Offmax = 3

kup = np.linspace(-pi / a, pi / a, 100)
kdown = np.linspace(-pi / a, pi / a, 100)

Eup = -Offinit + np.cos(a * kup + pi) + Uinit
Edown = -Offinit + np.cos(a * kdown + pi)

E = []
Q = []

for i in kup:
    iup = np.argwhere(kup == i)

    for j in kdown:
        idown = np.argwhere(kdown == j)

        if (Eup[iup] > Edown[idown]) and (Eup[iup] > 0):
            Q.append(i - j)
            E.append(Eup[iup] - Edown[idown])

E = [x[0] for x in E]

Fermi = np.zeros(len(kup))

fig = plt.figure()
fig.suptitle('Excitações de Stoner')

ax1 = plt.subplot(221)
ax1.set_xlabel('Vetor de Onda (k)')
ax1.set_ylabel('Energia')
EF, = ax1.plot(kup, Fermi, color='black')
Bup, = ax1.plot(kup, Eup, color='r')
Bdown, = ax1.plot(kdown, Edown, color='b')
ax1.grid()
ax1.set_title('Bandas Eletrônicas')

ax2 = plt.subplot(222)
ax2.set_xlabel('Vetor de Espalhamento (q)')
ax2.set_ylabel('Energia')
T = ax2.scatter(Q, E, s=1, alpha=0.3, color='black')
plt.xlim(0, pi / a)
plt.ylim(0, 3.5)
ax2.set_title('Excitações')

U_slider_ax = fig.add_axes([0.175, 0.15, 0.65, 0.03])
U_slider = Slider(U_slider_ax, 'U', valstep=0.01, valmin=Umin, valmax=Umax, valinit=Uinit)

Off_slider_ax = fig.add_axes([0.175, 0.1, 0.65, 0.03])
Off_slider = Slider(Off_slider_ax, 'Offset', valstep=0.01, valmin=Offmin, valmax=Offmax, valinit=Offinit)

U_slider.on_changed(updateU_Off)

Off_slider.on_changed(updateU_Off)

plt.show()

######################################################################################################
