import flet as ft
 
class EnfermedadView:
 
    def __init__(self, page: ft.Page):
 
        self.page = page
 
        self.page.title = (
            "Dashboard Enfermedades"
        )
 
        self.page.window_width = 1200
        self.page.window_height = 800
 
        self.page.scroll = "auto"
 
        # ======================================
        # BOTONES
        # ======================================
 
        self.btn_estadisticas = (
            ft.ElevatedButton(
                "Estadísticas"
            )
        )
 
        self.btn_riesgo = (
            ft.ElevatedButton(
                "Pacientes Riesgo"
            )
        )
 
        self.btn_mayores = (
            ft.ElevatedButton(
                "Pacientes Mayores"
            )
        )
 
        self.btn_barras = (
            ft.ElevatedButton(
                "Gráfica Barras"
            )
        )
 
        # ======================================
        # RESULTADOS
        # ======================================
 
        self.resultado = ft.Text(
            size=18
        )
 
        # TABLA
        self.tabla = ft.DataTable(
 
            columns=[
 
                ft.DataColumn(
                    ft.Text("Glucosa")
                ),
 
                ft.DataColumn(
                    ft.Text("BMI")
                ),
 
                ft.DataColumn(
                    ft.Text("Edad")
                ),
 
                ft.DataColumn(
                    ft.Text("Resultado")
                )
 
            ],
 
            rows=[]
 
        )
 
    # ======================================
    # INTERFAZ
    # ======================================
 
    def construir(self):
 
        return ft.Column(
 
            controls=[
 
                ft.Text(
 
                    "Sistema de Visualización",
                    size=32,
                    weight="bold"
 
                ),
 
                ft.Row(
 
                    controls=[
 
                        self.btn_estadisticas,
                        self.btn_riesgo,
                        self.btn_mayores,
                        self.btn_barras
 
                    ]
 
                ),
 
                ft.Divider(),
 
                self.resultado,
 
                self.tabla
 
            ],
 
            spacing=20
 
        )