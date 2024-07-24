import flet as ft

class AnketsPage(ft.View):

#   def change_navigation_destination(self, e):
#     if e.control.selected_index == 0:
#       e.page.go('/blind')
#     elif e.control.selected_index == 1:
#       e.page.go('/ankets')
#     elif e.control.selected_index == 2:
#       e.page.go('/end_reg')
  
#     self.update()

  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar) -> None:
    super().__init__(route = '/ankets', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
   
    self.navigation_bar = nav_bar

 

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment= ft.MainAxisAlignment.CENTER,
        #scroll=ft.ScrollMode.ALWAYS,
        scroll=ft.ScrollMode.ALWAYS,
        expand=1,

        auto_scroll=True,
        controls=[
            ft.Container(
                image_src="background_profile.png",
                #height=500,
                #width=300,
                padding=0,
                image_fit=ft.ImageFit.COVER,
                #expand=True,
                content=ft.Column(
                    
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls = [
                    ft.Container(
                    bgcolor="#FFFFFF",
                    border_radius=20,
                    border= ft.border.all(1, ft.colors.GREY_100),
                    #height=500,
                    content=ft.Column(
                        alignment= ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                [
                                   ft.Row(
                                       [
                                        ft.Image(
                                            src="women.jpg",
                                            height=130,
                                            fit=ft.ImageFit.COVER,
                                            border_radius=15,

                                        ), 
                                       ]
                                   ),
                                   ft.Column(
                                       controls=[
                                           ft.Row(
                                               controls=[
                                                   ft.Container(
                                                        ft.Text(
                                                            "ОТЗЫВЫ",
                                                            style=ft.TextStyle(
                                                                color="#FFFFFF", 
                                                                size=10, 
                                                                weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                            ),
                                                        text_align="center",
                                                        ),
                                                    on_click= lambda e: e.page.go("/arenda_2"),
                                                    bgcolor="#B9A9FC",
                                                    width=64,
                                                    height=18,
                                                    border_radius=25,
                                                    padding=ft.Padding(0,0,0,0),
                                                    margin=ft.Margin(0,0,0,20),
                                                ),
                                               ]
                                           ),
                                           ft.Text(
                                               value="Alena",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                                

                                           ),
                                           ft.Text(
                                               value = "Vaceikina",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                           ),
                                           ft.Container(
                                               
                                           )
                                       ],
                                       alignment="center",
                                   ) 
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ГОРОД",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)),
                                        width=130,
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0",
                                        color = "black",
                                        bgcolor="#FFFFFF"
                                    ),
                                    ft.TextField(
                                        hint_text="БЮДЖЕТ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=165, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="О СЕБЕ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 100,
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                        text_align="center"
                                    ),
                                ],
                                alignment= "center"
                            ),
                        ],
                        horizontal_alignment="center"
                    ),
                    margin = ft.Margin(10,30,10,5),
                    padding=ft.Padding(0,10,0,10),
                ),
                ft.Container(
                    bgcolor="#FFFFFF",
                    border_radius=20,
                    border= ft.border.all(1, ft.colors.GREY_100),
                    #height=500,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [
                                   ft.Row(
                                       [
                                        ft.Image(
                                            src="man.png",
                                            height=130,
                                            fit=ft.ImageFit.COVER,
                                            border_radius=15,

                                        ), 
                                       ]
                                   ),
                                   ft.Column(
                                       controls=[
                                           ft.Row(
                                               controls=[
                                                   ft.Container(
                                                        ft.Text(
                                                            "ОТЗЫВЫ",
                                                            style=ft.TextStyle(
                                                                color="#FFFFFF", 
                                                                size=10, 
                                                                weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                            ),
                                                        text_align="center",
                                                        ),
                                                    on_click= lambda e: e.page.go("/arenda_2"),
                                                    bgcolor="#B9A9FC",
                                                    width=64,
                                                    height=18,
                                                    border_radius=25,
                                                    padding=ft.Padding(0,0,0,0),
                                                    margin=ft.Margin(0,0,0,20),
                                                ),
                                               ]
                                           ),
                                           ft.Text(
                                               value="Alena",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                                

                                           ),
                                           ft.Text(
                                               value = "Vaceikina",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                           ),
                                           ft.Container(
                                               
                                           )
                                       ],
                                       alignment="center",
                                   ) 
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ГОРОД",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)),
                                        width=130,
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0",
                                        color = "black",
                                        bgcolor="#FFFFFF"
                                    ),
                                    ft.TextField(
                                        hint_text="БЮДЖЕТ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=165, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="О СЕБЕ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 100,
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                        text_align="center"
                                    ),
                                ],
                                alignment= "center"
                            ),
                        ],
                        alignment="center",
                        horizontal_alignment="center"
                    ),
                    margin = ft.Margin(10,5,10,5),
                    padding=ft.Padding(0,10,0,10),
                ),
                ft.Container(
                    bgcolor="#FFFFFF",
                    border_radius=20,
                    border= ft.border.all(1, ft.colors.GREY_100),
                    #height=500,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [
                                   ft.Row(
                                       [
                                        ft.Image(
                                            src="man.png",
                                            height=130,
                                            fit=ft.ImageFit.COVER,
                                            border_radius=15,

                                        ), 
                                       ]
                                   ),
                                   ft.Column(
                                       controls=[
                                           ft.Row(
                                               controls=[
                                                   ft.Container(
                                                        ft.Text(
                                                            "ОТЗЫВЫ",
                                                            style=ft.TextStyle(
                                                                color="#FFFFFF", 
                                                                size=10, 
                                                                weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                            ),
                                                        text_align="center",
                                                        ),
                                                    on_click= lambda e: e.page.go("/arenda_2"),
                                                    bgcolor="#B9A9FC",
                                                    width=64,
                                                    height=18,
                                                    border_radius=25,
                                                    padding=ft.Padding(0,0,0,0),
                                                    margin=ft.Margin(0,0,0,20),
                                                ),
                                               ]
                                           ),
                                           ft.Text(
                                               value="Alena",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                                

                                           ),
                                           ft.Text(
                                               value = "Vaceikina",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD)
                                                ),
                                           ),
                                           ft.Container(
                                               
                                           )
                                       ],
                                       alignment="center",
                                   ) 
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ГОРОД",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)),
                                        width=130,
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0",
                                        color = "black",
                                        bgcolor="#FFFFFF"
                                    ),
                                    ft.TextField(
                                        hint_text="БЮДЖЕТ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=165, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="О СЕБЕ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 100,
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                        text_align="center"
                                    ),
                                ],
                                alignment= "center"
                            ),
                        ],
                        alignment="center",
                        horizontal_alignment="center"
                    ),
                    margin = ft.Margin(10,5,10,5),
                    padding=ft.Padding(0,10,0,10),
                )
                
                ]
            )
            )
        ]
    )

      )
    ]
