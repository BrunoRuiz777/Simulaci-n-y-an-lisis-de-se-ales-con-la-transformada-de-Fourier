Análisis de Señales mediante la Transformada de Fourier
Propósito del Proyecto
Este repositorio contiene la simulación numérica y la verificación matemática de las propiedades de la Transformada Discreta de Fourier utilizando los ecosistemas de MATLAB y Python. Además de analizar señales elementales en los dominios del tiempo y de la frecuencia, el repositorio incluye demostraciones gráficas orientadas a videos educativos para ilustrar las diferencias entre señales continuas, discretas, periódicas y aperiódicas.

Estructura del Código
El proyecto cuenta con los siguientes archivos fundamentales:

analisis_espectral.m: Código principal implementado en MATLAB.

analisis_espectral.py: Código equivalente desarrollado en Python aprovechando la eficiencia de NumPy.

demo_senales_video.py: Script de Python (usando NumPy y Matplotlib) diseñado para renderizar los cuatro subgráficos comparativos (Continua vs Discreta y Periódica vs Aperiódica) explicados en la demostración en video.

Requisitos de Ejecución
Para garantizar la reproducibilidad y la correcta ejecución del código de este proyecto, se requiere la siguiente configuración del entorno de desarrollo:

MATLAB: Versión R2022a o superior.

Python: Versión 3.9 o superior.

Dependencias de Python: Los paquetes requeridos están listados en el archivo requirements.txt, siendo indispensables NumPy, Matplotlib y SciPy.

Modelamiento Numérico de Señales Elementales
Dentro del alcance del proyecto, el estudio espectral requiere la simulación de señales de prueba clásicas en el procesamiento digital:

Pulso Rectangular: Una señal aperiódica de duración finita en el tiempo. Al aplicar la Transformada de Fourier, su energía espectral se distribuye en forma de una función continua tipo Sinc (con un lóbulo central principal y múltiples lóbulos secundarios).

Señal Senoidal: Representa una onda periódica pura que matemáticamente se extiende al infinito. Su transformada analítica resulta en dos impulsos de Dirac situados de forma simétrica en el eje de frecuencias.

Función Escalón Unitario: Un salto repentino en el tiempo cuyo espectro combina un impulso a frecuencia cero (DC) y un decaimiento inversamente proporcional a la frecuencia.

Consideraciones sobre la Implementación de FFT y Fase
En los scripts de análisis de frecuencia, se implementan rutinas específicas para asegurar la consistencia algorítmica:

Centrado del espectro: Se emplea la función fftshift (tanto en MATLAB como np.fft.fftshift en Python) para aplicar una rotación circular que permite visualizar el espectro simétrico bilateral centrado correctamente en 0 Hz.

Corrección de ruido numérico en la fase: Debido a los límites de precisión del formato de doble punto flotante en las computadoras, el cálculo algorítmico de la fase puede arrojar resultados inestables en frecuencias donde la magnitud es casi nula. Para mitigar esto, se aplica una técnica de umbralización por amplitud (típicamente 10⁻⁶), forzando a cero el valor complejo si no supera dicho umbral crítico.