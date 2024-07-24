import flet as ft


class BlindPage(ft.View):
  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar) -> None:
    super().__init__(route = '/blind', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"

    self.navigation_bar = nav_bar
    self.navigation_bar.selected_index = 0


    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Column(
      [
        ft.Container(
          image_src="background_profile.png",
          image_fit=ft.ImageFit.COVER,
          content=ft.Container(
              bgcolor="#FFFFFF",
              border_radius=20,
              border= ft.border.all(1, ft.colors.GREY_100),
              margin = ft.Margin(25,40,25,20),
              padding=ft.Padding(15,30,15,20),
              content=ft.Column(
                  controls=[
                      ft.Row(
                          controls=[
                              ft.Container(
                                  ft.Text(
                                      "МИХАИЛ ДОЛИН,",
                                      style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD),
                                  )
                              )
                            ),
                            ft.Container(
                                  ft.Text(
                                      "26",
                                      style=ft.TextStyle(
                                                   color="#786086", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD),
                                  )
                              )
                            ),
                            ft.Container(
                                ft.Icon(
                                    ft.icons.STAR,
                                    color="#000000",
                                    size=25,
                                )
                            ),
                          ],
                          alignment= ft.MainAxisAlignment.CENTER
                      ),
                      ft.Row(
                        [
                          ft.Image(
                          src = "man.png",
                          border_radius=20,
                          height=300,
                          ),
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                      ),
                      ft.Row(
                          [
                            ft.Container(
                                ft.Text(
                                  "ЕСТЬ ЖИЛЬЕ, ИЩУ СОСЕДА",
                                  style=ft.TextStyle(
                                          color="#FFFFFF", 
                                          size=15, 
                                          weight=ft.FontWeight(ft.FontWeight.BOLD)
                                          ),
                                  text_align="center",
                                ),
                                on_click= lambda e: e.page.go("/arenda_2"),
                                bgcolor="#B9A9FC",
                                width=280,
                                height=30,
                                border_radius=25,
                                padding=ft.Padding(0,5,0,0),
                                margin=ft.Margin(0,0,0,10),
                                ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                      ),
                      ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ГОРОД",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD)),
                                        width=120,
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
                                        width=155, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                      ),
                  ]
              )
          )
        ),
        ft.Row(
          [
            ft.Container(
              bgcolor="#A0CE72", 
              width = 82,
              height = 62,
              border_radius=25,
              padding=ft.Padding(0,10,0,0),
              content=ft.Text(
                  "ДА",
                  style=ft.TextStyle(
                          color="#FFFFFF", 
                          size=25, 
                          weight=ft.FontWeight(ft.FontWeight.BOLD)
                        ),
                  text_align="center",

              )        
            ),
            ft.Container(
              animate= True,
              animate_scale=2,
              content= ft.Text(
                "Перейти в профиль",
                style=ft.TextStyle(
                      color="#FFFFFF", 
                      size=13, 
                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                      ),
                text_align="center",
              ),
              on_click= lambda e: e.page.go("/arenda_2"),
              bgcolor="#B9A9FC",
              width=159,
              height=45,
              border_radius=25,
              padding=ft.Padding(0,10,0,0)
            ),
            # ft.ElevatedButton(
            #   text="Перейти в профиль",
            #   width=170,
            #   height=46,
            #   color="#FFFFFF",
            #   bgcolor="#B9A9FC",
            #   on_click= lambda e: e.page.go("/reg_matrix"),
            # ),
            ft.Container(
              bgcolor="#FE6A6A", 
              width = 82,
              height = 62,
              border_radius=25,
              padding=ft.Padding(0,10,0,0),
              content=ft.Text(
                  "НЕТ",
                  style=ft.TextStyle(
                          color="#FFFFFF", 
                          size=25, 
                          weight=ft.FontWeight(ft.FontWeight.BOLD)
                        ),
                  text_align="center",

              )        
            ),
          ],
          alignment=ft.MainAxisAlignment.CENTER
        )
      ],
      horizontal_alignment="center",
    )
      )
    ]
  # def change_navigation_destination(self, e):
  #   if e.control.selected_index == 0:
  #     e.page.go('/blind')
  #   elif e.control.selected_index == 1:
  #     e.page.go('/ankets')
  #   elif e.control.selected_index == 2:
  #     e.page.go('/end_reg')
  
  #   self.update()

