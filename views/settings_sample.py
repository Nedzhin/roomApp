import flet as ft

class SettingsSamplePage(ft.View):
  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar) -> None:
    super().__init__(route = '/settings_sample', padding = 0)
  
    self.page = page
    self.bgcolor = "#FFFFFF"
    self.navigation_bar = nav_bar
    self.navigation_bar.selected_index = 2

    self.profile_avatar = ft.Container(
                            ft.CircleAvatar(
                            foreground_image_src="women.jpg",
                            radius=60,
                          ),
                        )
    
    self.profile_fullname = ft.Container(
                ft.Text(
                  "АЛЁНА ВАЦЕЙКИНА",
                  font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                              color="#362D56", 
                              size=15, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                      text_align="center"
                
                )
              )
    
    # self.button = ft.Container(
    #   height=55,
    #   width = 260,
    #   border_radius = 25,
    #   expand = True,
    #   bgcolor = "#B9A9FC",
    #   content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular"),
    #   padding = ft.padding.only(left=10, right=10, top=0, bottom=0),
    #   margin= ft.margin.only(40, 0,40, 20),
    #   alignment = ft.alignment.center,
    #   on_click = lambda e: e.page.go('/anketa')
    # )

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="landing_back.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(10,30,10,20),
          content= 
          ft.Column(
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment="center",
            
            controls = [
              ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls = [
                  ft.Container(
                    height=33,
                    width = 33,
                    content = ft.Icon(ft.icons.CLOSE_ROUNDED, color= "#786086", scale=ft.Scale(2)),
                    margin=ft.margin.only(0,10,20,10),
                    on_click= lambda e: e.page.go("/end_reg")
                  ),
                
                ]
              ),
              self.profile_avatar,
              self.profile_fullname,
              ft.Container(
                content=ft.Column(
                  alignment=ft.MainAxisAlignment.CENTER,
                  controls=[
                    ft.Container(
                      bgcolor="#9488C6",
                      height=13
                    ),
                    ft.Container(
                      height=54,
                      content =
                      ft.Row(
                        controls = [
                          ft.Icon(ft.icons.WALLET, color= "#786086"),
                          ft.Text(
                                "ОФОРМИТЬ ПОДПИСКУ",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                                ),
                                text_align="center"
                          ),
                          ft.Container(
                            # height=33,
                            # width = 33,
                            content = ft.Icon(ft.icons.ARROW_FORWARD, color= "white"),
                            bgcolor="#9488C6",
                            border_radius=25,
                          ),
                          
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                      ),
                      margin=ft.margin.only(20,0,15,0)
                    )

                  ]
                ),
                border_radius=15,
                bgcolor="white",
                width=310,
                margin=ft.margin.only(0,20,0,20),
              ),
              ft.Container(
                    content = ft.Column(
                      controls = [
                        ft.Container(
                          url="https://t.me/roomapp",
                          height=35,
                          border=ft.border.only(bottom=ft.border.BorderSide(2, "#D9CAE0")),
                          content=ft.Row(
                            controls=[
                              ft.Text(
                                "НАПИСАТЬ В ПОДДЕРЖКУ",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                                ),
                                text_align="center"
                              ),
                              ft.Icon(ft.icons.OPEN_IN_NEW, color= "#786086", scale=ft.Scale(1))
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                          ),
                          padding=ft.padding.only(40,0,20,0)
                        ),

                        ft.Container(
                          height=35,
                          border=ft.border.only(bottom=ft.border.BorderSide(2, "#D9CAE0")),
                          content=ft.Row(
                            controls=[
                              ft.Text(
                                "ЯЗЫКИ",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                                ),
                                text_align="center"
                              ),
                              ft.Icon(ft.icons.LANGUAGE, color= "#786086", scale=ft.Scale(1))
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                          ),
                          padding=ft.padding.only(40,0,20,0)
                        ),

                        ft.Container(
                          height=35,
                          border=ft.border.only(bottom=ft.border.BorderSide(2, "#D9CAE0")),
                          content=ft.Row(
                            controls=[
                              ft.Text(
                                "ВВЕСТИ ПРОМОКОД",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                                ),
                                text_align="center"
                              ),
                              ft.Icon(ft.icons.PERCENT, color= "#786086", scale=ft.Scale(1))
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                          ),
                          padding=ft.padding.only(40,0,20,0)
                        ),

                        ft.Container(
                          height=35,
                          border=ft.border.only(bottom=ft.border.BorderSide(2, "#D9CAE0")),
                          content=ft.Row(
                            controls=[
                              ft.Text(
                                "ВЫЙТИ ИЗ АККАУНТА",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD)
                                ),
                                text_align="center"
                              ),
                              ft.Icon(ft.icons.ARROW_BACK, color= "#786086", scale=ft.Scale(1))
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                          ),
                          padding=ft.padding.only(40,0,20,0)
                        ),

                        ft.Container(
                          height=35,
                          content=ft.Row(
                            controls=[
                              ft.Text(
                                "УДАЛИТЬ АККАУНТ",
                                font_family= "RussoOne-Regular",
                                style=ft.TextStyle(
                                      color="#362D56", 
                                      size=15, 
                                      weight=ft.FontWeight(ft.FontWeight.BOLD),
                                ),
                                text_align="center",
                                color="#DD2D22",
                              )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                          ),
                          padding=ft.padding.only(40,0,20,0)
                        ),

                      ]
                    ),
                    bgcolor="white",
                    border=ft.border.all(2, "#D9CAE0"),
                    width=330,
                    border_radius=25,
                    padding=ft.Padding(0,10,0,0),
                    margin=ft.Margin(0,20,0,20),
              ),

              
            ]
          )
        )
      )
    ]
