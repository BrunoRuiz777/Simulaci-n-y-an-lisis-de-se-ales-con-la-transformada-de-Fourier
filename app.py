import numpy as np
import matplotlib.pyplot as plt

# 1. GENERACIÓN DE SEÑALES: CONTINUA VS DISCRETA
# Señal "Continua" (Simulada)
# Creamos un vector de tiempo con alta densidad de puntos para simular continuidad
t_continuo = np.linspace(0, 1, 1000) 
f0 = 5  # Frecuencia fundamental de 5 Hz [4]

# Señal senoidal matemática: x(t) = A * cos(2*pi*f0*t + phi) [4]
x_continuo = np.cos(2 * np.pi * f0 * t_continuo)

# Señal Discreta
# Para la secuencia discreta x[n], definimos una frecuencia de muestreo Fs baja [3]
Fs = 20  
T = 1 / Fs  # Intervalo de muestreo uniforme T [3]
n = np.arange(0, 1, T) # Vector de muestras discretas [3]

# Evaluamos la misma onda, pero solo en los instantes de muestreo
x_discreto = np.cos(2 * np.pi * f0 * n)

# ==============================================================================
# 2. GENERACIÓN DE SEÑALES: PERIÓDICA VS APERIÓDICA
# ==============================================================================

t_vent = np.linspace(-1, 1, 1000) # Ventana de observación temporal

# Señal Periódica
# Se modela usando una onda senoidal pura, la cual se repite teóricamente 
# hasta el infinito [4].
x_periodica = np.sin(2 * np.pi * 3 * t_vent)

# Señal Aperiódica (Pulso Rectangular)
# Es un pulso de duración finita tau. Se define como 1 para |t| <= tau/2, 
# y 0 en los bordes truncados [5, 6].
tau = 0.5  
x_aperiodica = np.where(np.abs(t_vent) <= tau / 2, 1, 0)

# ==============================================================================
# 3. VISUALIZACIÓN DE LOS RESULTADOS (MATPLOTLIB)
# ==============================================================================
plt.figure(figsize=(14, 10))

# -- Gráfico 1: Señal Continua --
plt.subplot(2, 2, 1)
plt.plot(t_continuo, x_continuo, color='royalblue', linewidth=2)
plt.title('1A. Señal Continua (Simulación de Alta Resolución)', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo $t$ (s)')
plt.ylabel('Amplitud $x(t)$')
plt.grid(True, linestyle='--', alpha=0.7)

# -- Gráfico 2: Señal Discreta --
plt.subplot(2, 2, 2)
# Utilizamos 'stem' porque es la forma estándar de visualizar secuencias x[n] [3]
plt.stem(n, x_discreto, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('1B. Señal Discreta (Secuencia Muestreada)', fontsize=12, fontweight='bold')
plt.xlabel('Muestras $n$ (Intervalo $T$)')
plt.ylabel('Amplitud $x[n]$')
plt.grid(True, linestyle='--', alpha=0.7)

# -- Gráfico 3: Señal Periódica --
plt.subplot(2, 2, 3)
plt.plot(t_vent, x_periodica, color='seagreen', linewidth=2)
plt.title('2A. Señal Periódica (Onda Senoidal Infinita)', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo $t$ (s)')
plt.ylabel('Amplitud')
plt.grid(True, linestyle='--', alpha=0.7)

# -- Gráfico 4: Señal Aperiódica --
plt.subplot(2, 2, 4)
plt.plot(t_vent, x_aperiodica, color='darkorange', linewidth=2)
plt.fill_between(t_vent, x_aperiodica, color='darkorange', alpha=0.3) # Sombreado para destacar la energía finita
plt.title('2B. Señal Aperiódica (Pulso Rectangular Finito)', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo $t$ (s)')
plt.ylabel('Amplitud')
plt.grid(True, linestyle='--', alpha=0.7)

# Ajustar márgenes para que no se superpongan los textos
plt.tight_layout()
plt.show()
