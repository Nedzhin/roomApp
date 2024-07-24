import flet as ft


class EndRegPage(ft.View):

  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar) -> None:
    super().__init__(route = '/end_reg', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.navigation_bar = nav_bar
    self.navigation_bar.selected_index = 2
    
    self.lock = ft.Icon(
      name="lock", 
      scale = ft.Scale(2),
      color="black"
    )


    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="background_profile.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(40,40,40,40),
          content= 
          ft.Column(
            alignment = "spaceBetween",
            horizontal_alignment="center",
            controls = [
              ft.Container(
                bgcolor="#FFFFFF",
                border_radius=20,
                border= ft.border.all(1, ft.colors.GREY_100),
                content=ft.Column(
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
                                        hint_text="СФЕРА ДЕЯТЕЛЬНОСТИ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 30,
                                        text_align = "center", 
                                        border_radius=25, 
                                        bgcolor = "#FFFFFF",
                                        border_color = "#D9CAE0",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ОБРАЗОВАНИЯ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 30,
                                        text_align = "center", 
                                        border_radius=25, 
                                        bgcolor = "#FFFFFF",
                                        border_color = "#D9CAE0",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ХОББИ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 30,
                                        text_align = "center", 
                                        border_radius=25, 
                                        bgcolor = "#FFFFFF",
                                        border_color = "#D9CAE0",
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
                                        height = 120,
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                        text_align="center"
                                    ),
                                ],
                                alignment= "center"
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ИЗМЕНИТЬ ПРОФИЛЬ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)), 
                                        width=310,
                                        height = 30,
                                        text_align = "center", 
                                        border_radius=25, 
                                        bgcolor = "#FFFFFF",
                                        border_color = "#D9CAE0",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER,
                                
                            ),
                        ],
                        alignment="center",
                        horizontal_alignment="center"
                    ),
                    margin = ft.Margin(10,30,10,20),
                    padding=ft.Padding(0,10,0,20),
                )
            ]
          )
        )
      ),
      self.navigation_bar
    ]

  # def change_navigation_destination(self, e):
  #   if e.control.selected_index == 0:
  #     e.page.go('/blind')
  #   elif e.control.selected_index == 1:
  #     e.page.go('/ankets')
  #   elif e.control.selected_index == 2:
  #     e.page.go('/end_reg')
  
  #   self.update()
