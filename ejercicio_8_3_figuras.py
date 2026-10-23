import math
import tkinter as tk
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

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

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (
            self.radio + self.altura)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        return 4 * math.pi * self.radio ** 3 / 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return self.base ** 2 * self.altura / 3

    def calcular_superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * self.lado ** 2


class Prisma(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_volumen(self):
        return self.base ** 2 * self.altura

    def calcular_superficie(self):
        return 2 * self.base ** 2 + 4 * self.base * self.altura


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras geométricas")

        tk.Label(
            root,
            text="Seleccione una figura"
        ).pack(pady=10)

        botones = tk.Frame(root)
        botones.pack()

        figuras = [
            ("Cilindro", self.ventana_cilindro),
            ("Esfera", self.ventana_esfera),
            ("Pirámide", self.ventana_piramide),
            ("Cubo", self.ventana_cubo),
            ("Prisma", self.ventana_prisma)
        ]

        for i, (nombre, funcion) in enumerate(figuras):
            tk.Button(
                botones,
                text=nombre,
                command=funcion
            ).grid(row=0, column=i, padx=3)

        self.resultado = tk.Label(root, text="")
        self.resultado.pack(pady=20)

    def mostrar_resultado(self, figura):
        self.resultado.config(
            text=(
                f"Volumen = {figura.calcular_volumen():.2f} cm³\n"
                f"Superficie = "
                f"{figura.calcular_superficie():.2f} cm²"
            )
        )

    def ventana_cilindro(self):
        self.mostrar_resultado(Cilindro(2, 5))

    def ventana_esfera(self):
        self.mostrar_resultado(Esfera(2))

    def ventana_piramide(self):
        self.mostrar_resultado(Piramide(4, 6, 5))

    def ventana_cubo(self):
        self.mostrar_resultado(Cubo(4))

    def ventana_prisma(self):
        self.mostrar_resultado(Prisma(4, 6))


def main():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
