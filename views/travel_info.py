import flet as ft

class TravelInfoPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/travel_info', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
    self.travel_country = ft.Container(
                    content = ft.Text(
                      value="Страна поездки",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    self.travel_city = ft.Container(
                    content = ft.Text(
                      value="Город поездки",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    self.travel_dates = ft.Container(
                    content = ft.Text(
                      value="Даты (от-до)",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    self.travel_longness = ft.Container(
                    content = ft.Text(
                      value="Длительность \nПоездки",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    self.travel_budget = ft.Container(
                    content = ft.Text(
                      value="Дневной Бюджет \n(от-до)",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    
    self.button_back = ft.Container(
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=25, right=25, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,40),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/travel_var')
    )

    self.button_forth = ft.Container(
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Далее", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=25, right=25, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,40),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/end_reg')
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
            alignment = "center",
            horizontal_alignment="center",
            controls = [
              ft.Column(
                alignment="center",
                controls = [
                  ft.Text("ЕЩЕ НЕМНОГО И НАЧНЕМ", 
                          size = 16, 
                          text_align = "center",
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
                  self.travel_country,
                  self.travel_city
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.travel_dates,
                  self.travel_longness
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.travel_budget
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
              [
                ft.Image(
                src = "info1.png",
                fit = ft.ImageFit.COVER,
                animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                height=230,
                ),
              ],
              alignment= ft.MainAxisAlignment.CENTER,
            ),
              ft.Row(
                controls = [
                  self.button_back
                ],
                alignment = "center"
              ),
              ft.Row(
                controls = [
                  self.button_forth
                ],
                alignment = "center"
              )
            ]
          )
        )
      )
    ]
