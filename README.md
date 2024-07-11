# Reconocimiento de Medicamentos con IA | IAMed

* Descripción del Proyecto
  Nuestro proyecto se trata de una app que permita a las personas conocer las indicaciones de las medicinas que deseen, a través de la cámara mostraran la caja
  de su medicamento, y la aplicación les mostrará su nombre, descripción, fórmula, dosis y si necesita o no receta médica.

  ![image](https://github.com/user-attachments/assets/a42b05ab-ae09-4188-be2a-5caa3573839a)

  ![image](https://github.com/user-attachments/assets/cccbfaf8-aaba-484e-bd3d-81532b4122e2)

  ![image](https://github.com/user-attachments/assets/7a4de4f7-35df-4ac5-af9e-cf6de8f60f1e)

* Arquitectura del proyecto
  Librerias:
  mysql.connector, torch, opencv, numpy, pathlib, tkinter, setuptools, Pillow, requests, pandas, pyttsx3 (Esta fue utilizada para la narración),
  threading.

  El modelo fue creado con Google Colab YoloV5.

  ![image](https://github.com/user-attachments/assets/f8d49fe8-0dff-48e7-8d65-a96c844774f9)


* Proceso de desarrollo:

-Fuente del dataset
 El dataset lo creamos nosotros mismos, descargando varias imágenes y creando sus etiquetas, lo pueden ver en nuestra carpeta Data en el repositorio.
 Por ahora nuestro dataset solo detecta 4 medicamentos:

 ![image](https://github.com/user-attachments/assets/b1a2f078-ef38-42c7-a974-ad8f2ac5c2c5)

 ![image](https://github.com/user-attachments/assets/0ca6690d-6ae7-4c8d-9868-d23e91a58cfb)

 ![image](https://github.com/user-attachments/assets/51ee3a4b-7da6-4d87-ab33-3a0acba47aa1)

 Ejemplo de imágenes:
 ![image](https://github.com/user-attachments/assets/6bc659e9-f50c-4322-bc2c-7965b07e5172)
 
-Manejo excepciones/control errores
 En el mismo programa se controlan diferentes errores, por ejemplo en caso de haber un error al cargar el modelo de IA o al tratar de mapear los datos
 de la Base de Datos en la aplicación.

-¿Qué modelo de Machine Learning están usando?
Estamos utilizando el modelo de machine learning YOLOv5 (You Only Look Once, versión 5) para la detección de objetos. 

-Estadística
Creando un escenario ficticio en el que nuestra aplicación sale al mercado, podriamos disminuir la cantidad de muertes causadas por la automedicación:

![image](https://github.com/user-attachments/assets/59a3ff04-e450-4c3d-81fa-78b5a54b3745)

-Nuestra aplicación proporciona información precisa sobre los medicamentos, incluyendo dosis y posibles interacciones, lo cual reduce significativamente los riesgos asociados con la automedicación.
-Utilizando el modelo YOLOv5, la aplicación puede identificar medicamentos de manera rápida y precisa, asegurando que los usuarios reciban información en tiempo real.
-Al reducir la probabilidad de consumir medicamentos incorrectos o en dosis incorrectas, la aplicación puede prevenir errores comunes que conducen a hospitalizaciones y muertes.

-Métricas de Evaluación del Modelo

![esta1](https://github.com/user-attachments/assets/1fdb6b75-a4c5-4c23-bab1-a7fa42a404c2)

![esta2](https://github.com/user-attachments/assets/8b0735a0-759e-41a5-a2c0-fd774a6bde23)

* Funcionalidades:
  
-Una de sus funciones es leer los datos que muestra la aplicación para tener una forma de escuchar las indicaciones.
-Su principal función es la de detectar medicamentos a través de la cámara, para posteriormente mostrar sus datos:

 ![image](https://github.com/user-attachments/assets/edac96a8-59ef-4d32-88c6-3cee4db4e34e)

 ![image](https://github.com/user-attachments/assets/ad2e42ea-a35d-4913-912f-0ee1fc04036d)




