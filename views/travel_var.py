import flet as ft

class TravelVarPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/travel_var', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"


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
                  ft.Text("ВЫБЕРЕТЕ НАИБОЛЕЕ \nПОДХОДЯЩУЮ \nКАТЕГОРИЮ", 
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
              ft.Row(
                [ 
                  ft.Container(
                    ft.Text(
                      "Собираюсь присоединиться к туристической группе",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                        color="#FFFFFF", 
                        size=13, 
                        weight=ft.FontWeight(ft.FontWeight.BOLD)
                      ),
                      text_align="center",
                      ),
                    on_click= lambda e: e.page.go("/travel_info"),
                    bgcolor="#907CDC",
                    width=241,
                    height=76,
                    border_radius=25,
                    padding=ft.Padding(0,15,0,0)
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [ 
                  ft.Container(
                    ft.Text(
                      "Являюсь частью уже\n собранной группы и ищу\n людей, готовых к нам присоединиться",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                        color="#FFFFFF", 
                        size=13, 
                        weight=ft.FontWeight(ft.FontWeight.BOLD)
                      ),
                      text_align="center",
                      ),
                    on_click= lambda e: e.page.go("/travel_info"),
                    bgcolor="#907CDC",
                    width=241,
                    height=76,
                    border_radius=25,
                    padding=ft.Padding(0,0,0,0)
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
              [
                ft.Image(
                src = "travel_var1.png",
                fit = ft.ImageFit.COVER,
                animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                height=230,
                ),
              ],
              alignment= ft.MainAxisAlignment.CENTER,
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
