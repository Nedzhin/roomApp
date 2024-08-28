import flet as ft

class AnketsPage(ft.View):

#   def change_navigation_destination(self, e):
#     if e.control.selected_index == 0:
#       e.page.go('/blind')
#     elif e.control.selected_index == 1:
#       e.page.go('/ankets')
#     elif e.control.selected_index == 2:
#       e.page.go('/end_reg')
  
#     self.update()

  def __init__(self, page: ft.Page, nav_bar: ft.NavigationBar) -> None:
    super().__init__(route = '/ankets', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
   
    self.navigation_bar = nav_bar

    self.example_profile = ft.Container(
                    bgcolor="#FFFFFF",
                    border_radius=20,
                    border= ft.border.all(1, ft.colors.GREY_100),
                    #height=500,
                    content=ft.Column(
                        alignment= ft.MainAxisAlignment.START,
                        controls=[
                            ft.Row(
                                [
                                   ft.Container(      
                                        ft.Image(
                                            src="women.jpg",
                                            height=130,
                                            fit=ft.ImageFit.COVER,
                                            border_radius=15,

                                        ), 
                                   ),
                                   ft.Column(
                                       controls=[
                                         ft.Row(
                                           controls = [
                                            ft.Container(
                                                ft.Text(
                                                    "26",
                                                    style=ft.TextStyle(
                                                                color="#FFFFFF", 
                                                                size=15, 
                                                                weight=ft.FontWeight(ft.FontWeight.BOLD),
                                                                font_family="RussoOne-Regular",
                                                    ),
                                                    text_align="center",
                                                    color="#786086"
                                                ),
                                                height=24,
                                                border_radius=25,
                                                padding=ft.Padding(0,0,0,0),
                                                margin=ft.Margin(0,0,0,0),
                                            ),
                                            ft.Container(
                                              ft.Icon(ft.icons.STAR, color="black"),
                                            )
                                           ],
                                           alignment=ft.MainAxisAlignment.END,
                                         ),
                                         ft.Container(
                                            ft.Text(
                                               value="Name",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD),
                                                   font_family="RussoOne-Regular",
                                                ),
                                                
                                           ),
                                         ),
                                         ft.Container(
                                           ft.Text(
                                               value = "Surname",
                                               style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD),
                                                   font_family="RussoOne-Regular",
                                                ),
                                           ),
                                         ),
                                         ft.Container(
                                           height = 45,
                                           width = 135,
                                           content=ft.Text(
                                             "Status",
                                             style=ft.TextStyle(
                                                   color="#362D56", 
                                                   size=15, 
                                                   weight=ft.FontWeight(ft.FontWeight.BOLD),
                                                   font_family="RussoOne-Regular",
                                                ),
                                            text_align="center",
                                           ),
                                           bgcolor="#B9A9FC",
                                           border_radius=25,
                                           padding=ft.padding.only(0,10,0,0)
                                         )
                                       ],
                                       alignment=ft.MainAxisAlignment.START,
                                   ) 
                                ],
                                alignment= ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="ГОРОД",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family="RussoOne-Regular",),
                                        width=130,
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0",
                                        color = "black",
                                        bgcolor="#FFFFFF",
                                        read_only=True,
                                    ),
                                    ft.TextField(
                                        hint_text="БЮДЖЕТ",
                                        hint_style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family="RussoOne-Regular",), 
                                        width=165, 
                                        height = 30,
                                        text_align = "center",
                                        border_radius=25,
                                        border_color = "#D9CAE0", 
                                        bgcolor = "#FFFFFF",
                                        read_only=True,
                                    ),
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            ),
                              
                            ft.Container(
                                    ft.Column(
                                      controls=[
                                        ft.Text(
                                            "О СЕБЕ",
                                            style = ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family="RussoOne-Regular",),
                                            text_align="center",
                                        ),
                                        ft.Icon(ft.icons.KEYBOARD_ARROW_DOWN, color = "#D9CAE0")
                                      ],
                                      alignment="center",
                                      horizontal_alignment="center"
                                    ),
                                    
                                    bgcolor="white",
                                    border_radius=25,
                                    height=120,
                                    width = 290,
                                    border= ft.border.all(5, "#D9CAE0"),
                                    padding=ft.padding.only(0, 45, 0, 0)
                            ),
                            ft.Container(
                              width = 230,
                              height = 30,
                              content=ft.Text(
                                "ПЕРЕЙТИ В ПРОФИЛЬ",
                                style=ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family="RussoOne-Regular",),
                                text_align="center",
                                color="white"
                              ),
                              bgcolor="#B9A9FC",
                              border_radius=25,
                              padding=ft.padding.only(0,5,0,0)
                            )
                        ],
                        horizontal_alignment="center"
                    ),
                    margin = ft.Margin(10,10,10,5),
                    padding=ft.Padding(0,10,0,10),
                )
 

    self.controls = [
      ft.SafeArea(
        expand = True,
        # alignment=ft.MainAxisAlignment.START,
        # horizontal_alignment= ft.MainAxisAlignment.CENTER,
        # scroll=ft.ScrollMode.ALWAYS,
        # expand=1,
        #auto_scroll=True,
        content= ft.Container(
                image_src="background_profile.png",
                #height=500,
                #width=300,
                padding=ft.padding.only(20,30,20,20),
                image_fit=ft.ImageFit.COVER,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.ALWAYS,
                    controls = [
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls = [
                                ft.Container(
                                height=33,
                                width = 33,
                                content = ft.Icon(ft.icons.FILTER_1, color= "#786086" ),
                                bgcolor="white",
                                border_radius=25,
                                margin=ft.margin.only(0,0,10,0),
                                on_click= lambda e: e.page.go("/settings_sample")
                                ),
                                ft.Container(
                                height=33,
                                width = 33,
                                content = ft.Icon(ft.icons.SEARCH, color= "#786086" ),
                                bgcolor="white",
                                border_radius=25,
                                margin=ft.margin.only(0,0,10,0),
                                on_click= lambda e: e.page.go("/settings_sample")
                                ),
                            ]
                        ),
                       self.example_profile,
                       self.example_profile,
                       self.example_profile,
                    ]
                )
            )
        )
    ]