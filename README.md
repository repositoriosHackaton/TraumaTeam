# Reconocimiento de Medicamentos con IA | IAMed

## Descripción del Proyecto

Nuestro proyecto es una app que permite a las personas conocer las indicaciones de los medicamentos a través de la cámara. Al mostrar la caja del medicamento, la aplicación muestra su nombre, descripción, fórmula, dosis y si necesita receta médica.

![image](https://github.com/user-attachments/assets/a42b05ab-ae09-4188-be2a-5caa3573839a)
![image](https://github.com/user-attachments/assets/cccbfaf8-aaba-484e-bd3d-81532b4122e2)
![image](https://github.com/user-attachments/assets/7a4de4f7-35df-4ac5-af9e-cf6de8f60f1e)

## Arquitectura del Proyecto

- Este programa fue desarrollado con Python versión 3.12.
- Utilizamos como base de datos MySQL:

  ![image](https://github.com/user-attachments/assets/3358173b-920d-4db0-aa11-d70ffdd9069e)

- El modelo fue creado con Google Colab YoloV5:

  ![image](https://github.com/user-attachments/assets/f8d49fe8-0dff-48e7-8d65-a96c844774f9)

## Librerías Utilizadas

- **mysql.connector**: Proporciona una interfaz para conectarse y interactuar con bases de datos MySQL desde Python. Se utiliza para realizar operaciones como consultas, inserciones y actualizaciones en la base de datos.
- **torch**: Parte de PyTorch, una biblioteca de aprendizaje profundo que proporciona herramientas para crear y entrenar redes neuronales. Se utiliza para cargar y ejecutar el modelo YOLOv5 para la detección de objetos.
- **opencv**: Open Source Computer Vision Library es una biblioteca de visión por computadora que incluye diversas funciones para el procesamiento de imágenes y videos. Es utilizada para capturar imágenes de la cámara y procesar cuadros de video.
- **numpy**: Biblioteca fundamental para el cálculo numérico en Python. Proporciona soporte para arrays multidimensionales y funciones matemáticas de alto rendimiento. Se usa en combinación con otras bibliotecas para procesar datos y realizar cálculos numéricos.
- **pathlib**: Biblioteca estándar de Python para manipular rutas de archivos de manera más fácil y consistente. Proporciona clases para manejar rutas de archivos y directorios.
- **tkinter**: Biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI). Se utiliza para crear la interfaz de la aplicación, incluyendo botones, etiquetas y ventanas emergentes.
- **setuptools**: Herramienta de utilidad para facilitar la distribución de paquetes Python. Se utiliza para construir y distribuir paquetes de Python, permitiendo instalar dependencias y gestionar proyectos.
- **Pillow**: Biblioteca de procesamiento de imágenes que proporciona capacidades para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes. Se usa para convertir imágenes capturadas por OpenCV en un formato que Tkinter puede mostrar.
- **requests**: Biblioteca para realizar solicitudes HTTP de manera fácil y humana. Es utilizada para interactuar con servicios web, enviar datos y recibir respuestas desde servidores remotos.
- **pandas**: Biblioteca para la manipulación y análisis de datos, que proporciona estructuras de datos rápidas, flexibles y expresivas. Se utiliza para gestionar y analizar datos tabulares, como los resultados de las predicciones del modelo.
- **pyttsx3**: Biblioteca para la síntesis de voz en Python. Se utiliza para convertir texto en habla, permitiendo que la aplicación narre las indicaciones del medicamento detectado.
- **threading**: Biblioteca que permite la ejecución concurrente de tareas en diferentes hilos (threads). Se usa para ejecutar la narración de texto en un hilo separado, evitando que la interfaz de usuario se congele durante la narración.

## Proceso de Desarrollo

### Fuente del Dataset

El dataset fue creado descargando varias imágenes y creando sus etiquetas. Está disponible en nuestra carpeta Data en el repositorio. Actualmente, el dataset detecta 4 medicamentos:

![image](https://github.com/user-attachments/assets/b1a2f078-ef38-42c7-a974-ad8f2ac5c2c5)
![image](https://github.com/user-attachments/assets/0ca6690d-6ae7-4c8d-9868-d23e91a58cfb)
![image](https://github.com/user-attachments/assets/51ee3a4b-7da6-4d87-ab33-3a0acba47aa1)

### Ejemplo de Imágenes

![image](https://github.com/user-attachments/assets/6bc659e9-f50c-4322-bc2c-7965b07e5172)

### Manejo de Excepciones/Control de Errores

El programa controla diferentes errores, por ejemplo, errores al cargar el modelo de IA o al mapear los datos de la Base de Datos en la aplicación.

### Modelo de Machine Learning

Estamos utilizando el modelo de machine learning YOLOv5 (You Only Look Once, versión 5) para la detección de objetos.

### Estadísticas

Creando un escenario ficticio en el que nuestra aplicación sale al mercado, podríamos disminuir la cantidad de muertes causadas por la automedicación:

![image](https://github.com/user-attachments/assets/59a3ff04-e450-4c3d-81fa-78b5a54b3745)

- Nuestra aplicación proporciona información precisa sobre los medicamentos, incluyendo dosis y posibles interacciones, lo cual reduce significativamente los riesgos asociados con la automedicación.
- Utilizando el modelo YOLOv5, la aplicación puede identificar medicamentos de manera rápida y precisa, asegurando que los usuarios reciban información en tiempo real.
- Al reducir la probabilidad de consumir medicamentos incorrectos o en dosis incorrectas, la aplicación puede prevenir errores comunes que conducen a hospitalizaciones y muertes.

### Métricas de Evaluación del Modelo

![esta1](https://github.com/user-attachments/assets/1fdb6b75-a4c5-4c23-bab1-a7fa42a404c2)
![esta2](https://github.com/user-attachments/assets/8b0735a0-759e-41a5-a2c0-fd774a6bde23)

## Funcionalidades

- Leer los datos que muestra la aplicación para tener una forma de escuchar las indicaciones.
- Detectar medicamentos a través de la cámara y mostrar sus datos:

  ![image](https://github.com/user-attachments/assets/edac96a8-59ef-4d32-88c6-3cee4db4e34e)
  ![image](https://github.com/user-attachments/assets/ad2e42ea-a35d-4913-912f-0ee1fc04036d)

## Estado del Proyecto

- Consideramos que el proyecto está en una fase Alpha. Todavía podemos agregar más medicamentos al dataset y mejorar el modelo para que tenga mejor efectividad.
