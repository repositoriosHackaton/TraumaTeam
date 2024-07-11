import torch
import cv2
import numpy as np
import pathlib
from tkinter import Label, Tk, Text, messagebox, END, Toplevel
from tkinter import ttk
from PIL import Image, ImageTk
from bd import traer_medicamentos
import pyttsx3
import threading

# Configurar pathlib para usar WindowsPath en lugar de PosixPath
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

class MedicamentoDetectorApp:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.root.title("Detección de Medicamentos")
        self.root.geometry("1366x700")
        self.root.configure(bg='#2c3e50')

        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("TLabel", background='#2c3e50', foreground='#ecf0f1', font=('Helvetica', 12))
        style.configure("TButton", background='#3498db', foreground='#ecf0f1', font=('Helvetica', 12, 'bold'))
        style.map("TButton", background=[('active', '#2980b9')])
        style.configure("TText", background='#34495e', foreground='#ecf0f1', font=('Helvetica', 12))

        self.label = ttk.Label(root, text="Presiona el botón para detectar medicamentos, luego debes mostrar tu medicamento en cámara", wraplength=700)
        self.label.pack(pady=20)

        self.detect_button = ttk.Button(root, text="Detectar Medicamento", command=self.detectar_medicamento)
        self.detect_button.pack(pady=20)

        self.result_text = Text(root, height=10, wrap='word', bg='#34495e', fg='#ecf0f1', font=('Helvetica', 12))
        self.result_text.pack(padx=10, pady=10, fill='both', expand=True)

        scrollbar = ttk.Scrollbar(self.result_text)
        scrollbar.pack(side='right', fill='y')
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

        self.cap = None
        self.confirm_window = None
        self.engine = pyttsx3.init()
        self.voice_active = False
        self.paused = False
        self.activar_voz_button = None

    def detectar_medicamento(self):
        print("Iniciando detección de medicamentos...")

        self.result_text.delete(1.0, END)

        if self.activar_voz_button:
            self.activar_voz_button.destroy()

        self.cap = cv2.VideoCapture(0)
        detected_class = None

        while True:
            ret, frame = self.cap.read()

            if ret:
                frame_resized = cv2.resize(frame, (640, 480))

                results = self.model(frame_resized)

                predictions = results.pandas().xyxy[0]

                frame_with_detections = np.squeeze(results.render())
                cv2.imshow('Detected Objects', frame_with_detections)

                if not predictions.empty:
                    detected_class = int(predictions['class'].iloc[0])
                    detected_name = predictions['name'].iloc[0]
                    print(f"Clase detectada: {detected_class}")
                    print(f"Medicina detectada: {detected_name}")

                    cv2.imwrite('detected_medicine.png', frame_with_detections)

                    self.mostrar_imagen_confirmacion(frame_with_detections, detected_class)

                    print("Cerrando la cámara...")
                    self.cap.release()
                    cv2.destroyAllWindows()
                    return

                key = cv2.waitKey(5)
                if key == ord('q') or cv2.getWindowProperty('Detected Objects', cv2.WND_PROP_VISIBLE) < 1:
                    break

        self.cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Detección Completa", "La detección de medicamentos ha finalizado.")

    def mostrar_imagen_confirmacion(self, image, clase_mec):
        print("Mostrando imagen de confirmación...")

        self.confirm_window = Toplevel(self.root)
        self.confirm_window.title("Confirmar Medicina")
        self.confirm_window.geometry("1366x700")
        self.confirm_window.configure(bg='#2c3e50')

        img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(image=img)

        label = Label(self.confirm_window, image=img_tk, bg='#2c3e50')
        label.image = img_tk
        label.pack(pady=20)

        confirm_button = ttk.Button(self.confirm_window, text="Confirmar Medicina", command=lambda: self.confirmar_medicina(clase_mec))
        confirm_button.pack(pady=10)

        detect_again_button = ttk.Button(self.confirm_window, text="Detectar Otra Medicina", command=self.detectar_otro)
        detect_again_button.pack(pady=10)

    def confirmar_medicina(self, clase_mec):
        print("Confirmando medicina...")

        if self.confirm_window:
            self.confirm_window.destroy()

        medicamento = traer_medicamentos(clase_mec)

        if medicamento:
            self.result_text.insert(END, f"Nombre: {medicamento['nombre']}\n\n")
            self.result_text.insert(END, f"Descripción: {medicamento['descripcion']}\n\n\n")
            self.result_text.insert(END, f"Fórmula: {medicamento['formula']}\n\n\n")
            self.result_text.insert(END, f"Dosis: {medicamento['dosis']}\n\n\n")
            self.result_text.insert(END, f"Receta: {medicamento['receta']}\n\n\n")
            self.result_text.insert(END, "-" * 20 + "\n")

            self.activar_voz_button = ttk.Button(self.root, text="Escuchar Indicaciones", command=lambda: self.leer_indicaciones(medicamento))
            self.activar_voz_button.pack(pady=10)

    def detectar_otro(self):
        print("Detectando otra medicina...")

        if self.confirm_window:
            self.confirm_window.destroy()
        self.detectar_medicamento()

    def leer_indicaciones(self, medicamento):
        print("Leyendo indicaciones del medicamento...")

        nombre = medicamento.get('nombre', '')
        descripcion = medicamento.get('descripcion', '')
        formula = medicamento.get('formula', '')
        dosis = medicamento.get('dosis', '')
        receta = medicamento.get('receta', '')

        texto_completo = f"Medicamento: {nombre}. Descripción: {descripcion}. Fórmula: {formula}. Dosis: {dosis}. Receta: {receta}."

        # Ejecutar la narración en un hilo separado
        threading.Thread(target=self.narrar_texto, args=(texto_completo,), daemon=True).start()

    def narrar_texto(self, texto):
        self.paused = False
        self.engine.say(texto)
        self.engine.startLoop(False)

        # Monitorear el estado de la pausa
        while self.engine.isBusy() and not self.paused:
            self.engine.iterate()

    def toggle_pause(self):
        print("Toggle pause...")
        if self.paused:
            self.paused = False
            self.engine.resume()
        else:
            self.paused = True
            self.engine.pause()

    def cerrar_app(self):
        self.engine.stop()
        self.root.destroy()

def cargar_modelo(model_path):
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

    modelo = cargar_modelo(model_path)

    root = Tk()
    app = MedicamentoDetectorApp(root, modelo)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_app)
    root.mainloop()
