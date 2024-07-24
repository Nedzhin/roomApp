import flet as ft

class RentVarPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/rent_var', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
    print(page.client_storage.get("user_name"))
    self.button = ft.Container(
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=25, right=25, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,40),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/purpose')
    )

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="landing_back.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(40,40,40,40),
          content= 
          ft.Column(
            alignment = "spaceBetween",
            horizontal_alignment="center",
            controls = [
              ft.Column(
                alignment="center",
                controls = [
                  ft.Text("ДАВАЙТЕ УТОЧНИМ, \nЧТО ВАС ИНТЕРЕСУЕТ?", 
                          size = 16, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  )
                ],
                horizontal_alignment = "center"
              ),
              ft.Container(
                bgcolor = "#907CDC",
                border_radius = 15,
                content = ft.Column(
                  alignment=ft.MainAxisAlignment.SPACE_AROUND,
                  controls = [
                    ft.Container(
                      ft.Row([
                        ft.Text(
                          "Совместная аренда",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#FFFFFF", size=15, weight=ft.FontWeight(ft.FontWeight.BOLD)),
                          width=241,
                          height=76,
                          text_align="center"
                        ),
                        ],
                        alignment="center",
                      ),
                      padding=ft.Padding(0,20,0,0)
                    ),
                    ft.Container(
                      ft.Row(
                        [ 
                          ft.Container(
                            ft.Text(
                              "Долгосрочная",
                              font_family= "RussoOne-Regular",
                              style=ft.TextStyle(
                                color="#FFFFFF", 
                                size=13, 
                                weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                              text_align="center",
                            ),
                            on_click= lambda e: e.page.go("/rent_info"),
                            bgcolor="#7160B3",
                            width=159,
                            height=55,
                            border_radius=25,
                            padding=ft.Padding(0,10,0,0),
                            margin=ft.Margin(0,0,0,20),
                          ),
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                      ),
                    padding=ft.Padding(0,0,0,10),
                  ),

                  ft.Container(
                    ft.Row(
                      [ 
                        ft.Container(
                          ft.Text(
                            "Краткосрочная",
                            font_family= "RussoOne-Regular",
                            style=ft.TextStyle(
                              color="#FFFFFF", 
                              size=13, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                            ),
                            text_align="center",
                          ),
                          on_click= lambda e: e.page.go("/rent_info"),
                          bgcolor="#7160B3",
                          width=159,
                          height=55,
                          border_radius=25,
                          padding=ft.Padding(0,10,0,0)
                          ),
                      ],
                      alignment= ft.MainAxisAlignment.CENTER
                    ),
                    padding=ft.Padding(0,0,0,30),
                  ),
                ]
              ),
              margin=ft.Margin(50,10,50,10),
            ), 
              ft.Row(
                controls = [
                  self.button
                ],
                alignment = "center"
              )
            ]
          )
        )
      )
    ]