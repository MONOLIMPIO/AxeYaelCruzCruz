import flet as ft

from Vista.enfermedad_view import (
    EnfermedadView
)

from Controlador.enfermedad_controller import (
    EnfermedadController
)

def main(page: ft.Page):

    vista = EnfermedadView(page)

    controlador = (
        EnfermedadController(vista)
    )

    # ======================================
    # EVENTOS
    # ======================================

    vista.btn_estadisticas.on_click = (
        controlador.mostrar_estadisticas
    )

    vista.btn_riesgo.on_click = (
        controlador.mostrar_riesgo
    )

    vista.btn_mayores.on_click = (
        controlador.mostrar_mayores
    )

    vista.btn_barras.on_click = controlador.mostrar_grafica_barras

    # ======================================
    # MOSTRAR APP
    # ======================================

    page.add(
        vista.construir()
    )

ft.app(target=main)
