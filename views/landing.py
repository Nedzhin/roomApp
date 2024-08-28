import flet as ft
import asyncio

class LandingPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/landing', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.lock = ft.Icon(
      name="lock", 
      scale = ft.Scale(2),
      color="black"
    )


    self.button = ft.Container(
      height=55,
      width=260,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Перейти к анкете", color = "white", size = 15, font_family="RussoOne-Regular"),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go("/anketa")
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
              ft.Row(
                controls = [
                  ft.Image(
                  src = "landing1.png",
                  fit = ft.ImageFit.COVER,
                  animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                   width=350,
                   height=280
                  ),
                ],
                alignment = "center"
              ),
              ft.Column(
                alignment="center",
                controls = [
                  ft.Text("Мы рады \nприветствовать вас \nв нашем приложении", 
                          size = 22, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=15, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  )
                ],
                horizontal_alignment = "center"
              ),
              ft.Column(
                alignment="center",
                controls = [
                  ft.Text("Давайте познакомимся поближе. \nДля этого предлагаем заполнить \nнебольшую анкету", 
                          size = 15, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=15, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  )
                ],
                horizontal_alignment = "center"
              ),
              ft.Row(
                controls=[
                  self.lock
                ],
                alignment = "center"
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
