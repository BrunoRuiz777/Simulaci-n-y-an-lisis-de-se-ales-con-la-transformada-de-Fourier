import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generación de señales en el tiempo ---

# Señal continua (usamos muchos puntos para simular la continuidad)
t_continuo = np.linspace(0, 1, 1000)
f0 = 5  # Frecuencia fundamental de 5 Hz
x_continuo = np.cos(2 * np.pi * f0 * t_continuo)

# Señal discreta (muestreada)
Fs = 20  # Frecuencia de muestreo baja para que se noten los puntos
T = 1 / Fs
n = np.arange(0, 1, T)
x_discreto = np.cos(2 * np.pi * f0 * n)

# Ventana de observación para las otras señales
t_vent = np.linspace(-1, 1, 1000)

# Señal periódica (onda senoidal pura)
x_periodica = np.sin(2 * np.pi * 3 * t_vent)

# Señal aperiódica (pulso rectangular de ancho 0.5)
tau = 0.5
x_aperiodica = np.where(np.abs(t_vent) <= tau / 2, 1, 0)

# Función escalón unitario (requerida por la rúbrica)
x_escalon = np.where(t_vent >= 0, 1, 0)


# --- 2. Gráficas del dominio del tiempo ---
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t_continuo, x_continuo, color='royalblue')
plt.title('Señal Continua')
plt.xlabel('Tiempo (s)')
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 2, 2)
plt.stem(n, x_discreto, basefmt='k-')
plt.title('Señal Discreta')
plt.xlabel('Muestras n')
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 2, 3)
plt.plot(t_vent, x_periodica, color='seagreen')
plt.title('Señal Periódica')
plt.xlabel('Tiempo (s)')
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 2, 4)
plt.plot(t_vent, x_aperiodica, color='darkorange')
plt.fill_between(t_vent, x_aperiodica, color='darkorange', alpha=0.3)
plt.title('Señal Aperiódica (Pulso Rectangular)')
plt.xlabel('Tiempo (s)')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()


# --- 3. Transformada de Fourier y propiedades ---

N = len(t_vent)
dt = t_vent[1] - t_vent[0]

# Generamos el eje X de frecuencias y lo centramos en cero
frecuencias = np.fft.fftshift(np.fft.fftfreq(N, dt))

# Calculamos FFT del pulso original y centramos el espectro
fft_aperiodica = np.fft.fftshift(np.fft.fft(x_aperiodica))
magnitud_aperiodica = np.abs(fft_aperiodica) / N

# Calculamos la fase, aplicando un filtro para limpiar el ruido numérico
# en las frecuencias donde la magnitud es prácticamente cero
fase_aperiodica = np.angle(fft_aperiodica)
fase_aperiodica[magnitud_aperiodica < 1e-6] = 0 

# Para verificar la propiedad de desplazamiento en el tiempo, 
# movemos el pulso 0.25 segundos a la derecha y le sacamos la FFT
x_desplazada = np.where(np.abs(t_vent - 0.25) <= tau / 2, 1, 0)
fft_desplazada = np.fft.fftshift(np.fft.fft(x_desplazada))
magnitud_desplazada = np.abs(fft_desplazada) / N

fase_desplazada = np.angle(fft_desplazada)
fase_desplazada[magnitud_desplazada < 1e-6] = 0 


# --- 4. Gráficas del dominio de la frecuencia ---
plt.figure(figsize=(12, 8))

# Magnitud y fase del pulso centrado
plt.subplot(2, 2, 1)
plt.plot(frecuencias, magnitud_aperiodica, color='purple')
plt.title('Magnitud (Pulso centrado)')
plt.xlim(-20, 20)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 2, 2)
plt.plot(frecuencias, fase_aperiodica, color='teal')
plt.title('Fase (Pulso centrado)')
plt.xlim(-20, 20)
plt.grid(True, linestyle='--', alpha=0.7)

# Magnitud y fase del pulso desplazado
plt.subplot(2, 2, 3)
plt.plot(frecuencias, magnitud_desplazada, color='purple')
plt.title('Magnitud (Pulso desplazado en t=0.25)')
plt.xlim(-20, 20)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 2, 4)
plt.plot(frecuencias, fase_desplazada, color='crimson')
plt.title('Fase (Pulso desplazado en t=0.25)')
plt.xlim(-20, 20)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

# Esto abrirá las dos figuras juntas
plt.show()