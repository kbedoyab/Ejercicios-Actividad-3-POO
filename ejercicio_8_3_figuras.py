import math
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        self.volumen = volumen

    def get_superficie(self):
        return self.superficie

    def set_superficie(self, superficie):
        self.superficie = superficie

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_bases = 2 * math.pi * self.radio ** 2
        return area_lateral + area_bases


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        # Se conserva la aproximación utilizada en el ejercicio del libro.
        return 1.333 * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras geométricas")
        self.root.geometry("420x300")
        self.root.resizable(False, False)

        tk.Label(
            root, text="Seleccione una figura geométrica",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        botones = tk.Frame(root)
        botones.pack(pady=10)
        tk.Button(botones, text="Cilindro", width=12,
                  command=self.ventana_cilindro).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Esfera", width=12,
                  command=self.ventana_esfera).grid(row=0, column=1, padx=5)
        tk.Button(botones, text="Pirámide", width=12,
                  command=self.ventana_piramide).grid(row=0, column=2, padx=5)

        self.resultado = tk.Label(
            root, text="Seleccione una figura para calcular.", justify="left"
        )
        self.resultado.pack(pady=25)

    def mostrar_resultado(self, figura):
        self.resultado.config(
            text=(
                f"Volumen = {figura.get_volumen():.2f} cm³\n"
                f"Superficie = {figura.get_superficie():.2f} cm²"
            )
        )

    def crear_ventana(self, titulo, campos, funcion):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("300x230")
        ventana.resizable(False, False)
        entradas = {}

        for i, nombre in enumerate(campos):
            tk.Label(ventana, text=f"{nombre} (cm):").place(
                x=20, y=20 + i * 35, width=100, height=23
            )
            entrada = tk.Entry(ventana)
            entrada.place(x=125, y=20 + i * 35, width=140, height=23)
            entradas[nombre] = entrada

        def calcular():
            try:
                valores = []
                for nombre in campos:
                    texto = entradas[nombre].get().strip()
                    if not texto:
                        raise ValueError("Todos los campos son obligatorios.")
                    valor = float(texto)
                    if valor <= 0:
                        raise ValueError("Los valores deben ser mayores que cero.")
                    valores.append(valor)

                figura = funcion(*valores)
                self.mostrar_resultado(figura)
                ventana.destroy()
            except ValueError as error:
                messagebox.showerror("Error", str(error), parent=ventana)

        tk.Button(ventana, text="Calcular", command=calcular).place(
            x=100, y=145, width=100, height=28
        )

    def ventana_cilindro(self):
        self.crear_ventana("Cilindro", ["Radio", "Altura"], Cilindro)

    def ventana_esfera(self):
        self.crear_ventana("Esfera", ["Radio"], Esfera)

    def ventana_piramide(self):
        self.crear_ventana(
            "Pirámide", ["Base", "Altura", "Apotema"], Piramide
        )


def main():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
