import math
import tkinter as tk
from tkinter import messagebox


class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def establecer_nota(self, indice, nota):
        self.lista_notas[indice] = nota

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = sum((nota - promedio) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x330")
        self.root.resizable(False, False)
        self.campos = []

        for i in range(5):
            tk.Label(root, text=f"Nota {i + 1}:").place(
                x=20, y=20 + i * 30, width=70, height=23
            )
            campo = tk.Entry(root)
            campo.place(x=100, y=20 + i * 30, width=150, height=23)
            self.campos.append(campo)

        tk.Button(root, text="Calcular", command=self.calcular).place(
            x=20, y=175, width=100, height=28
        )
        tk.Button(root, text="Limpiar", command=self.limpiar).place(
            x=130, y=175, width=100, height=28
        )

        self.promedio = tk.Label(root, text="Promedio =")
        self.promedio.place(x=20, y=220, anchor="w")
        self.desviacion = tk.Label(root, text="Desviación estándar =")
        self.desviacion.place(x=20, y=245, anchor="w")
        self.mayor = tk.Label(root, text="Valor mayor =")
        self.mayor.place(x=20, y=270, anchor="w")
        self.menor = tk.Label(root, text="Valor menor =")
        self.menor.place(x=20, y=295, anchor="w")

    def calcular(self):
        try:
            notas = Notas()
            for i, campo in enumerate(self.campos):
                texto = campo.get().strip()
                if not texto:
                    raise ValueError("Debe ingresar las cinco notas.")
                nota = float(texto)
                if not 0 <= nota <= 5:
                    raise ValueError("Las notas deben estar entre 0 y 5.")
                notas.establecer_nota(i, nota)

            self.promedio.config(text=f"Promedio = {notas.calcular_promedio():.2f}")
            self.desviacion.config(
                text=f"Desviación estándar = {notas.calcular_desviacion():.2f}"
            )
            self.mayor.config(text=f"Valor mayor = {notas.calcular_mayor():.2f}")
            self.menor.config(text=f"Valor menor = {notas.calcular_menor():.2f}")
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.promedio.config(text="Promedio =")
        self.desviacion.config(text="Desviación estándar =")
        self.mayor.config(text="Valor mayor =")
        self.menor.config(text="Valor menor =")


def main():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
