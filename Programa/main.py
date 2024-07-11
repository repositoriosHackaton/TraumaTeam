import torch
import cv2
import numpy as np
import pathlib
from tkinter import Tk, Button, Label, Text, Scrollbar, messagebox, END, Toplevel
from PIL import Image, ImageTk
from bd import traer_medicamentos

# Configurar pathlib para usar WindowsPath en lugar de PosixPath
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

class MedicamentoDetectorApp:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.root.title("Detección de Medicamentos")
        self.root.geometry("600x400")

        self.label = Label(root, text="Presiona el botón para detectar medicamentos, luego debes mostrar tu medicamento en cámara")
        self.label.pack(pady=10)

        self.detect_button = Button(root, text="Detectar Medicamento", command=self.detectar_medicamento)
        self.detect_button.pack(pady=10)

        self.result_text = Text(root, height=10, wrap='word')
        self.result_text.pack(padx=10, pady=10, fill='both', expand=True)

        scrollbar = Scrollbar(self.result_text)
        scrollbar.pack(side='right', fill='y')
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

    def detectar_medicamento(self):
        print("Iniciando detección de medicamentos...")

        # Borrar los datos anteriores en caso de haber leído un medicamento previamente
        self.result_text.delete(1.0, END)

        # Captura de video desde la cámara de la computadora
        cap = cv2.VideoCapture(0)
        detected_class = None

        while True:
            # Realizar la lectura de los frames
            ret, frame = cap.read()

            if ret:
                # Realizar las detecciones
                results = self.model(frame)

                # Obtener las predicciones
                predictions = results.pandas().xyxy[0]

                # Mostrar las detecciones en la ventana de OpenCV
                frame_with_detections = np.squeeze(results.render())
                cv2.imshow('Detected Objects', frame_with_detections)

                # Verificar si se ha detectado algún objeto
                if not predictions.empty:
                    detected_class = predictions['class'].iloc[0]  # Obtener la clase del primer objeto detectado
                    clase_mec = int(detected_class)  # Convertir a entero para usarlo como parámetro
                    detected_name = predictions['name'].iloc[0]
                    print(f"Clase detectada: {detected_class}")
                    print(f"Medicina detectada: {detected_name}")

                    # Guardar la imagen con el marco y la información de la predicción
                    cv2.imwrite('detected_medicine.png', frame_with_detections)

                    # Mostrar la imagen en la interfaz gráfica
                    self.mostrar_imagen_confirmacion(frame_with_detections, clase_mec)

                    print("Cerrando la cámara...")
                    cap.release()
                    cv2.destroyAllWindows()
                    return  # Salir del bucle y la función

                # Código para salir de la cámara presionando q
                key = cv2.waitKey(5)
                if key == ord('q') or cv2.getWindowProperty('Detected Objects', cv2.WND_PROP_VISIBLE) < 1:
                    break

        # Cerrar las ventanas de OpenCv
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Detección Completa", "La detección de medicamentos ha finalizado.")

    def mostrar_imagen_confirmacion(self, image, clase_mec):
        print("Mostrando imagen de confirmación...")

        # Crear una nueva ventana para mostrar la imagen y botones de confirmación
        self.confirm_window = Toplevel(self.root)
        self.confirm_window.title("Confirmar Medicina")
        self.confirm_window.geometry("600x400")

        # Convertir la imagen a un formato compatible con Tkinter
        img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(image=img)

        label = Label(self.confirm_window, image=img_tk)
        label.image = img_tk  # Guardar la referencia para que no sea recolectada por el GC
        label.pack(pady=10)

        confirm_button = Button(self.confirm_window, text="Confirmar Medicina", command=lambda: self.confirmar_medicina(clase_mec))
        confirm_button.pack(pady=5)

        detect_again_button = Button(self.confirm_window, text="Detectar Otra Medicina", command=self.detectar_otro)
        detect_again_button.pack(pady=5)

    def confirmar_medicina(self, clase_mec):
        print("Confirmando medicina...")

        # Cerrar la ventana de confirmación
        self.confirm_window.destroy()

        # Obtener resultado de la base de datos
        medicamento = traer_medicamentos(clase_mec)

        # Mostrar lo que se trajo de la Base de Datos
        if medicamento:
            self.result_text.insert(END, f"Nombre: {medicamento['nombre']}\n\n")
            self.result_text.insert(END, f"Descripción: {medicamento['descripcion']}\n\n\n")
            self.result_text.insert(END, f"Fórmula: {medicamento['formula']}\n\n\n")
            self.result_text.insert(END, f"Dosis: {medicamento['dosis']}\n\n\n")
            self.result_text.insert(END, f"Receta: {medicamento['receta']}\n\n\n")
            self.result_text.insert(END, "-" * 20 + "\n")

    def detectar_otro(self):
        print("Detectando otra medicina...")
        # Cerrar la ventana de confirmación y reiniciar la detección
        self.confirm_window.destroy()
        self.detectar_medicamento()

def cargar_modelo(model_path): #Función para cargar el modelo best.pt
    try:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
        print("Modelo cargado exitosamente.")
        return model
    except Exception as e:
        print(f"Error al cargar el modelo: {str(e)}")
        exit()

if __name__ == "__main__":
    model_path = 'model/best.pt'
    print(f"Versión de Torch: {torch.__version__}")
    print(f"Versión de OpenCV: {cv2.__version__}")

    # Cargar el modelo una sola vez
    modelo = cargar_modelo(model_path)

    # Crear la interfaz gráfica
    root = Tk()
    app = MedicamentoDetectorApp(root, modelo)
    root.mainloop()
