import flet as ft

class TravelVarPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/travel_var', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"


    self.button = ft.Container(
      height=55,
      width = 260,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
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
          padding=ft.padding.only(20,20,20,20),
          content= 
          ft.Column(
            alignment = "spaceBetween",
            horizontal_alignment="center",
            controls = [
              ft.Container(           
                content = 
                  ft.Text("ВЫБЕРЕТЕ НАИБОЛЕЕ \nПОДХОДЯЩУЮ \nКАТЕГОРИЮ", 
                          size = 16, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
                margin=ft.margin.only(0,60,0,0)    
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
                    on_click= lambda e: go_and_select_0(e),
                    bgcolor="#7160B3",
                    width=245,
                    height=90,
                    border_radius=15,
                    padding=ft.Padding(0,15,0,0)
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment="center"
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
                    on_click= lambda e: go_and_select_1(e),
                    bgcolor="#7160B3",
                    width=245,
                    height=110,
                    border_radius=15,
                    padding=ft.Padding(0,15,0,0)
                  ),
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment="center"
              ),
              ft.Row(
              [
                ft.Image(
                src = "travel_var1.png",
                fit = ft.ImageFit.COVER,
                animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                height=160,
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

    def go_and_select_0(e):
      e.page.client_storage.set("travel_purpose", 0)
      print(e.page.client_storage.get("travel_purpose"))
      e.page.go('/travel_info')
      e.page.update()

    def go_and_select_1(e):
      e.page.client_storage.set("travel_purpose", 1)
      e.page.go('/travel_info')
      e.page.update()
