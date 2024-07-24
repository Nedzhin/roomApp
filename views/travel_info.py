import flet as ft

class TravelInfoPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/travel_info', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
    self.rent_date = ft.TextField(
                      hint_text="Страна поездки",
                      hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),
                      width=130,
                      height = 40,
                      text_align = "center",
                      border_radius=25,
                      border_color = "#FFFFFF",
                      color = "black",
                      bgcolor="#FFFFFF"
                    )
    
    self.rent_city = ft.TextField(
                      hint_text="Город поездки",
                      hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                      width=130, 
                      height = 40,
                      text_align = "center",
                      border_radius=25,
                      border_color = "#FFFFFF", 
                      bgcolor = "#FFFFFF",
                    )
    
    self.rent_status = ft.TextField(
                        hint_text="Статус на выбор", 
                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),
                        width=130,
                        height = 40,
                        text_align = "center", 
                        border_radius=25,
                        border_color = "#FFFFFF", 
                        bgcolor = "#FFFFFF",
                      )
    
    self.rent_budget = ft.TextField(
                        hint_text="Бюджет",
                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                        width=130,
                        height = 40,
                        text_align = "center", 
                        border_radius=25,
                        border_color = "#FFFFFF", 
                        bgcolor = "#FFFFFF",
                      )
    
    self.rent_photos = ft.TextField(
                    hint_text="Фотографии недвижимости", 
                    hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),
                    width=130,
                    height = 40,
                    text_align = "center", 
                    border_radius=25,
                    border_color = "#FFFFFF", 
                    bgcolor = "#FFFFFF",
                    )
    
    self.rent_region = ft.TextField(
                      hint_text="Районы",
                      hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                      width=130,
                      height = 40,
                      text_align = "center", 
                      border_radius=25,
                      border_color = "#FFFFFF", 
                      bgcolor = "#FFFFFF",
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
            alignment = "spaceBetween",
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
                  self.rent_date,
                  self.rent_city
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.rent_status,
                  self.rent_budget
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.rent_photos,
                  self.rent_region
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
