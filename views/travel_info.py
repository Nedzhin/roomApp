import flet as ft
import aiohttp
import asyncio
class TravelInfoPage(ft.View):
  def __init__(self, page: ft.Page, user_tid_back, BACK_URL) -> None:
    super().__init__(route = '/travel_info', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
    self.travel_country = ft.Container(
                    content = ft.Text(
                      value="Страна поездки",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.travel_country_popup)
    )
    
    self.travel_city = ft.Container(
                    content = ft.Text(
                      value="Город поездки",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.travel_city_popup)
    )
    
    self.travel_dates = ft.Container(
                    content = ft.Text(
                      value="Даты (от-до)",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.travel_dates_popup)
    )
    
    self.travel_longness = ft.Container(
                    content = ft.Text(
                      value="Длительность \nПоездки",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.travel_longness_popup)
    )
    
    self.travel_budget = ft.Container(
                    content = ft.Text(
                      value="Дневной Бюджет \n(от-до)",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.travel_budget_popup)
    )
    
    
    self.button_back = ft.Container(
      height=55,
      width = 260,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/travel_var')
    )

    self.button_forth = ft.Container(
      height=55,
      width = 260,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Далее", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: asyncio.run(end_registration(e,self, user_tid_back))
    )


    ### Country chosing

    def close_searchbar_country(e):
      e.page.close(self.travel_country_popup)
      self.travel_country.content.value = self.page.client_storage.get("user_travel_country")
      page.update()

    self.button_confirm_country = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar_country
      )

    self.fake_country = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe"]

    def get_value_country(e):
      print(e.control.value)
      e.page.client_storage.set("user_travel_country", e.control.value)


    self.result_search_country = ft.Container(
      visible=False,
      height=150,
      content=ft.RadioGroup(    
        content=ft.Column(
          height=100,
          scroll=True,
        ),
        on_change= get_value_country
      )
    )

    def show_results_country(e):
      if e.data:
        self.result_search_country.content.content.controls.clear()
        self.result_search_country.visible = True

        search_text = e.data.lower()
        matching_countries = [city for city in self.fake_country if search_text in city.lower()]

        for matched_country in matching_countries:
          self.result_search_country.content.content.controls.append(
            ft.Radio(
              label=matched_country,
              value=matched_country,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_country.visible = False
      
      page.update()

    self.search_bar_country = ft.Container(
      height=40,
      width = 284,
      bgcolor="white",
      border_radius=25,
      border=ft.border.all( 1, "#D9CAE0" ),
      content=ft.Row(
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls = [
          ft.VerticalDivider(width=2, color="transparent"),
          ft.Icon(ft.icons.SEARCH_ROUNDED, size=18, opacity=0.9, color="#362D56"),
          ft.TextField(
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=2,
            cursor_color="#362D56",
            cursor_width=1,
            color="#362D56",
            hint_text="ПОИСК",
            hint_style=ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
            on_change=show_results_country
          )
        ]
      )
    )

    self.travel_country_popup = ft.AlertDialog(
      #modal= True,
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 200,
        width = 310,
        content= ft.Column([
          self.search_bar_country,
          self.result_search_country,
          ]
        )
      ),
      actions=[
        self.button_confirm_country,
      ],

    )



    ### City chosing

    def close_searchbar_city(e):
      e.page.close(self.travel_city_popup)
      self.travel_city.content.value = self.page.client_storage.get("user_travel_city")
      page.update()

    self.button_confirm_city = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar_city
      )

    self.fake_city = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe"]

    def get_value_city(e):
      print(e.control.value)
      e.page.client_storage.set("user_travel_city", e.control.value)


    self.result_search_city = ft.Container(
      visible=False,
      height=150,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,

        ),
        on_change= get_value_city
      )
    )

    def show_results_city(e):
      if e.data:
        self.result_search_city.content.content.controls.clear()
        self.result_search_city.visible = True

        search_text = e.data.lower()
        matching_cities = [city for city in self.fake_city if search_text in city.lower()]

        for matched_city in matching_cities:
          self.result_search_city.content.content.controls.append(
            ft.Radio(
              label=matched_city,
              value=matched_city,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_city.visible = False
      
      page.update()

    self.search_bar_city = ft.Container(
      height=40,
      width = 284,
      bgcolor="white",
      border_radius=25,
      border=ft.border.all( 1, "#D9CAE0" ),
      content=ft.Row(
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls = [
          ft.VerticalDivider(width=2, color="transparent"),
          ft.Icon(ft.icons.SEARCH_ROUNDED, size=18, opacity=0.9, color="#362D56"),
          ft.TextField(
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=2,
            cursor_color="#362D56",
            cursor_width=1,
            color="#362D56",
            hint_text="ПОИСК",
            hint_style=ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
            on_change=show_results_city
          )
        ]
      )
    )

    self.travel_city_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 200,
        width = 310,
        content= ft.Column([
          self.search_bar_city,
          self.result_search_city,
          ]
        )
      ),
      actions=[
        self.button_confirm_city,
      ],

    )

    ### Budget chosing

    def close_budget_bar(e):
      e.page.close(self.travel_budget_popup)
      budget_picked_begin = self.travel_budget_popup.content.content.controls[2].controls[0].value
      budget_picked_end = self.travel_budget_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("user_travel_budget",  budget_picked_begin + " - " + budget_picked_end)

      self.travel_budget.content.value = self.page.client_storage.get("user_travel_budget")
      page.update()
      
    self.button_confirm_budget = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_budget_bar
      )

    self.travel_budget_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ЕЖЕДНЕВНЫЙ БЮДЖЕТ", 
                          size = 18, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=4, color="transparent" ),
          ft.Row(
            alignment="center",
            controls=[
              ft.TextField(
                            hint_text="ОТ (₽)",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),
              ft.TextField(
                            hint_text="ДО (₽)",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),

            ]
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_budget,
      ],

    )


    ### Dates Chosing

    def close_dates_bar(e):
      e.page.close(self.travel_dates_popup)
      dates_picked_begin = self.travel_dates_popup.content.content.controls[2].controls[0].value
      dates_picked_end = self.travel_dates_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("user_travel_dates",  dates_picked_begin + " - " + dates_picked_end)

      self.travel_dates.content.value = self.page.client_storage.get("user_travel_dates")
      page.update()
      
    self.button_confirm_dates = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_dates_bar
      )

    self.travel_dates_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ВЫБЕРИТЕ ДАТЫ ПОЕЗДКИ", 
                          size = 18, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=4, color="transparent" ),
          ft.Row(
            alignment="center",
            controls=[
              ft.TextField(
                            hint_text="ОТ",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),
              ft.TextField(
                            hint_text="ДО",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),

            ]
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_dates,
      ],

    )

    ### Longness Chosing

    def close_dates_bar(e):
      e.page.close(self.travel_longness_popup)
      dates_picked_begin = self.travel_longness_popup.content.content.controls[2].controls[0].value
      dates_picked_end = self.travel_longness_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("user_longness_dates",  dates_picked_begin + " - " + dates_picked_end)

      self.travel_longness.content.value = self.page.client_storage.get("user_longness_dates")
      page.update()
      
    self.button_confirm_dates = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_dates_bar
      )

    self.travel_longness_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("НА КАКОЙ СРОК ВЫ \nПЛАНИРУЕТЕ ПОЕЗДКУ?", 
                          size = 18, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=4, color="transparent" ),
          ft.Row(
            alignment="center",
            controls=[
              ft.TextField(
                            hint_text="МИН. ДНЕЙ",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),
              ft.TextField(
                            hint_text="МАКС. ДНЕЙ",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=134,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
              ),

            ]
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_dates,
      ],

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
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
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

    async def end_registration(e, self, user_tid):
      purpose_travel = str(self.page.client_storage.get("travel_purpose"))
      country = self.page.client_storage.get("user_travel_country")
      city = self.page.client_storage.get("user_travel_city")
      status = "random poka" #self.page.client_storage.get("user_travel_status")
      dates = self.page.client_storage.get("user_travel_dates")
      longness = self.page.client_storage.get("user_longness_dates")
      day_budget = self.page.client_storage.get("user_travel_budget")
      #user_tid = str(user_tid_back)
      print(type(purpose_travel))
      print(country)
      print(status)
      print(city)
      print(day_budget)
      print(longness)
      print(dates)

      e.page.go('/end_reg')
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          #print("information:",e.page.client_storage.get("user_name"))
          async with session.post(f'{BACK_URL}/purpose/travel/{user_tid}',
                               json={"purpose_travel": purpose_travel, "country": country,
        'city': city,
        'status': status,
        'dates': dates,
        'longness': longness,
        'day_budget': day_budget,
        }) as response:
                if response.status == 200:
                  print("user rent created")
                  #print(response.json())
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.reason}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}
