import flet as ft
import matplotlib.pyplot as plt

from Modelo.enfermedad_model import (
    EnfermedadModel
)

class EnfermedadController:

    def __init__(self, vista):

        self.vista = vista
        self.modelo = EnfermedadModel()

    # ======================================
    # ESTADÍSTICAS
    # ======================================
    def mostrar_estadisticas(self, e):

        total = (
            self.modelo.total_pacientes()
        )

        glucosa = (
            self.modelo.promedio_glucosa()
        )

        bmi = (
            self.modelo.promedio_bmi()
        )

        diabetes = (
            self.modelo.pacientes_diabetes()
        )

        sanos = (
            self.modelo.pacientes_sanos()
        )

        self.vista.resultado.value = f"""
Total pacientes: {total}

Promedio glucosa:
{glucosa:.2f}

Promedio BMI:
{bmi:.2f}

Pacientes con diabetes:
{diabetes}

Pacientes sanos:
{sanos}
"""

        self.vista.page.update()

        # ======================================
        # GRÁFICA
        # ======================================

        datos = [
            diabetes,
            sanos
        ]

        etiquetas = [
            "Diabetes",
            "Sanos"
        ]

        plt.pie(

            datos,

            labels=etiquetas,

            autopct="%1.1f%%"

        )

        plt.title(
            "Pacientes con y sin diabetes"
        )

        plt.show()

    # ======================================
    # TABLA PACIENTES RIESGO
    # ======================================
    def mostrar_riesgo(self, e):

        self.vista.tabla.rows.clear()

        datos = (
            self.modelo.pacientes_riesgo()
        )

        for _, fila in datos.iterrows():

            self.vista.tabla.rows.append(

                ft.DataRow(

                    cells=[

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Glucose"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["BMI"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Age"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Outcome"]
                                )
                            )
                        )

                    ]

                )

            )

        self.vista.page.update()

    # ======================================
    # TABLA PACIENTES MAYORES
    # ======================================
    def mostrar_mayores(self, e):

        self.vista.tabla.rows.clear()

        datos = (
            self.modelo.pacientes_mayores()
        )

        for _, fila in datos.iterrows():

            self.vista.tabla.rows.append(

                ft.DataRow(

                    cells=[

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Glucose"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["BMI"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Age"]
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Outcome"]
                                )
                            )
                        )

                    ]

                )

            )

        self.vista.page.update()

    # ======================================
    # GRÁFICA DE BARRAS
    # ======================================
    def mostrar_grafica_barras(self, e):

        diabetes = self.modelo.pacientes_diabetes()
        sanos    = self.modelo.pacientes_sanos()

        categorias = ["Con Diabetes", "Sanos"]
        valores    = [diabetes, sanos]
        colores    = ["#e74c3c", "#2ecc71"]

        plt.figure(figsize=(6, 4))
        plt.bar(categorias, valores, color=colores, width=0.5)

        plt.title("Pacientes con y sin Diabetes")
        plt.xlabel("Categoría")
        plt.ylabel("Número de Pacientes")

        for i, v in enumerate(valores):
            plt.text(i, v + 2, str(v), ha="center", fontweight="bold")

        plt.tight_layout()
        plt.show()