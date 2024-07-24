import flet as ft

class PurposePage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/purpose', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"

    print(self.page.client_storage.get("user_name"))
    print(self.page.client_storage.get("user_surname"))
    self.button = ft.Container(
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular"),
      padding = ft.padding.only(left=25, right=25, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,40),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/anketa')
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
                                               weight=ft.FontWeight(ft.FontWeight.BOLD),
                                               font_family= "RussoOne-Regular",
                                               ),
                  )
                ],
                horizontal_alignment = "center"
              ),
              ft.Row(
                [ 
                  ft.Container(
                    ft.Text(
                      "Совместная аренда",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                              color="#FFFFFF", 
                              size=13, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                      text_align="center",
                    ),
                    on_click= lambda e: e.page.go("/rent_var"),
                    bgcolor="#907CDC",
                    width=241,
                    height=65,
                    border_radius=25,
                    padding=ft.Padding(0,20,0,0),
                    margin=ft.Margin(0,0,0,20),
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment="center"
              ),
              ft.Row(
                [ 
                  ft.Container(
                    ft.Text(
                      "Соместные поездки",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                              color="#FFFFFF", 
                              size=13, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                      text_align="center",
                    ),
                    on_click= lambda e: e.page.go("/travel_var"),
                    bgcolor="#907CDC",
                    width=241,
                    height=65,
                    border_radius=25,
                    padding=ft.Padding(0,20,0,0),
                    margin=ft.Margin(0,0,0,20),
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment="center"
              ),
              ft.Row(
              [
                ft.Image(
                src = "purpose1.png",
                fit = ft.ImageFit.COVER,
                animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                height=230,
                ),
              ],
              alignment= ft.MainAxisAlignment.CENTER,
            ),
              ft.Row(
                controls = [
                  self.button,
                ],
                alignment = "center"
              )
            ]
          )
        )
      )
    ]
