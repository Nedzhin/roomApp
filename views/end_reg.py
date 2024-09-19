import flet as ft
import aiohttp

class EndRegPage(ft.View):

  


  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar, infos: dict, aim) -> None:
    super().__init__(route = '/end_reg', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.navigation_bar = nav_bar
    self.navigation_bar.selected_index = 2

    self.profile_budget = ft.TextField(
                                        hint_text= "", #infos["purpose"][0]["month_budget"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
                                        width=165, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                    )
    
    if not aim:
      self.profile_budget.hint_text = infos["purpose"][0]["month_budget"]
    else:
      self.profile_budget.hint_text = infos["purpose"][0]["day_budget"]
    # self.user_infos = self.get_information
    # results = self.get_information()
    # print(results)
    # print(self.user_infos)

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="background_profile.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(20,30,20,20),
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
                    content = ft.Icon(ft.icons.SETTINGS_OUTLINED, color= "#786086" ),
                    bgcolor="white",
                    border_radius=25,
                    margin=ft.margin.only(0,0,10,0),
                    on_click= lambda e: e.page.go("/settings_sample")
                  ),
                
                ]
              ),
              
              ft.Container(
                bgcolor="#FFFFFF",
                width=350,
                border_radius=25,
                border= ft.border.all(1, ft.colors.GREY_100),
                content=ft.Column(
                   controls=[
                     ft.Row(
                       [
                        ft.Image(
                          src="women.jpg",
                          height=130,
                          fit=ft.ImageFit.COVER,
                          border_radius=15,
                        ), 
                        ft.Column(
                           controls=[
                             ft.Row(
                              controls=[
                                ft.Container(
                                  ft.Text(
                                    "26",
                                    style=ft.TextStyle(
                                            color="#786086", 
                                            size=15, 
                                            weight=ft.FontWeight(ft.FontWeight.BOLD),
                                            font_family="RussoOne-Regular",
                                            ),
                                  ),
                                  margin=ft.Margin(5,0,5,0),
                                ),
                                ft.Container(
                                  ft.Text(
                                    "ОТЗЫВЫ",
                                    style=ft.TextStyle(
                                            color="#FFFFFF", 
                                            size=10, 
                                            weight=ft.FontWeight(ft.FontWeight.BOLD),
                                            font_family="RussoOne-Regular",
                                            ),
                                    text_align="center",
                                  ),
                                  on_click= lambda e: e.page.go("/ankets"),
                                  bgcolor="#B9A9FC",
                                  width=64,
                                  height=18,
                                  border_radius=25,
                                  # padding=ft.Padding(0,0,0,0),
                                  margin=ft.Margin(5,0,5,0),
                                ),
                                ft.Container(
                                ft.Icon(
                                    ft.icons.STAR,
                                    color="#000000",
                                    size=25,
                                ),
                                margin=ft.Margin(5,0,5,0),
                              ), 
                              ],
                              alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                             ),
                            ft.Text(
                              value= infos["anketa"]["username"],
                              style=ft.TextStyle(
                                        color="#362D56", 
                                        size=15, 
                                        weight=ft.FontWeight(ft.FontWeight.BOLD),
                                        font_family="RussoOne-Regular",
                                      ),                          
                            ),
                            ft.Text(
                              value = infos["anketa"]["usersurname"],
                              style=ft.TextStyle(
                                color="#362D56", 
                                size=15, 
                                weight=ft.FontWeight(ft.FontWeight.BOLD),
                                font_family="RussoOne-Regular",
                                ),
                            ),
                            ft.Container(
                                    ft.Text(
                                    infos["purpose"][0]["status"],
                                    style=ft.TextStyle(
                                            color="#FFFFFF", 
                                            size=10, 
                                            weight=ft.FontWeight(ft.FontWeight.BOLD),
                                            font_family="RussoOne-Regular",
                                            ),
                                    text_align="center",
                                  ),
                                  bgcolor="#B9A9FC",
                                  width=160,
                                  height=40,
                                  border_radius=25,
                                  padding=ft.Padding(0,10,0,0),
                                  margin=ft.Margin(0,0,0,0),           
                            ),                      
                              ],
                              alignment= ft.MainAxisAlignment.CENTER
                            ),
                           ],
                           alignment=ft.MainAxisAlignment.SPACE_EVENLY
                         ),
                         ft.Row(
                                [
                                    ft.TextField(
                                        hint_text=infos["anketa"]["city"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",),
                                        width=130,
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0",
                                        color = "black",
                                        bgcolor="#FFFFFF"
                                    ),
                                    self.profile_budget,
                                 ],
                                 alignment= ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text=infos["purpose"][0]["dates"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
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
                                        hint_text=infos["anketa"]["job"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
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
                                        hint_text=infos["anketa"]["education"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
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
                                        hint_text=infos["anketa"]["info"],
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
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
                                        hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family="RussoOne-Regular",), 
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
                #         ],
                #         alignment="center",
                #         horizontal_alignment="center"
                #     ),

                  ]
                ),
                    margin = ft.Margin(0,0,0,10),
                    padding=ft.Padding(5,5,5,10),
              ),
            ]
          )
        )
      ),
      self.navigation_bar
    ]

