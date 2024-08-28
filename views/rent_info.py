import flet as ft

class RentInfoPage(ft.View):
  def __init__(self, page: ft.Page) -> None:
    super().__init__(route = '/rent_info', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"

    self.rent_country = ft.Container(
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    content = ft.Text(
                      value="Страна аренды",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )
    
    self.rent_city = ft.Container(
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    content = ft.Text(
                      value="Город аренды",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_city_popup)
    )
    
    self.rent_status = ft.Container(
                    content = ft.Text(
                      value="Статус на выбор",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_status_popup)
    )
    
    self.rent_budget = ft.Container(
                    content = ft.Text(
                      value="Месячный бюджет \n(макс. цена)",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_budget_popup)
    )
    
    self.rent_region = ft.Container(
                    content = ft.Text(
                      value="Районы \nстанции метро",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_region_popup)
    )
    
    self.rent_photos = ft.Container(
                    content = ft.Text(
                      value="Фотографии",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    visible=False,
                    on_click= lambda e: e.page.open(self.rent_budget_popup)
    )
    
    self.rent_dates = ft.Container(
                    content = ft.Text(
                      value="Даты аренды \n(от-до)",
                      style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    visible=False,
                    on_click= lambda e: e.page.open(self.rent_dates_popup)
    )
    
    self.button_back = ft.Container(
      border_radius = 25,
      height=55,
      width = 260,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/rent_var')
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
      on_click = lambda e: e.page.go('/end_reg')
    )

    ### Country chosing

    def close_searchbar_country(e):
      e.page.close(self.rent_country_popup)
      self.rent_country.content.value = self.page.client_storage.get("user_rent_country")
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
      e.page.client_storage.set("user_rent_country", e.control.value)


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

    self.rent_country_popup = ft.AlertDialog(
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
      e.page.close(self.rent_city_popup)
      self.rent_city.content.value = self.page.client_storage.get("user_rent_city")
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
      e.page.client_storage.set("user_rent_city", e.control.value)


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

    self.rent_city_popup = ft.AlertDialog(
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


    ### Status chosing

    def close_status_bar(e):
      e.page.close(self.rent_status_popup)
      status_now = self.page.client_storage.get("user_rent_status")
      self.rent_status.content.value = status_now
      if status_now == "ЕСТЬ ЖИЛЬЁ, ИЩУ СОСЕДА":
        self.rent_photos.visible = True
        self.rent_dates.visible = True
      else:
        self.rent_photos.visible = False
        self.rent_dates.visible = False
      page.update()
      
    self.button_confirm_status = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_status_bar
      )
    
    def get_value_status(e):
      print(e.control.value)
      e.page.client_storage.set("user_rent_status", e.control.value)

    self.rent_status_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          #ft.Divider(height=3, color="transparent" ),
          ft.RadioGroup(
            
            content=ft.Column(
              controls = [
                ft.Radio(
                  label="НЕТ ЖИЛЬЯ, ИЩУ СОСЕДА",
                  value = "НЕТ ЖИЛЬЯ, ИЩУ СОСЕДА",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
                ft.Radio(
                  label="ЕСТЬ ЖИЛЬЁ, ИЩУ СОСЕДА",
                  value = "ЕСТЬ ЖИЛЬЁ, ИЩУ СОСЕДА",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
              ],
              horizontal_alignment="center"
            ),
            on_change= get_value_status
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_status,
      ],

    )

    ### Budget chosing

    def close_budget_bar(e):
      e.page.close(self.rent_budget_popup)
      budget_picked_begin = self.rent_budget_popup.content.content.controls[2].controls[0].value
      budget_picked_end = self.rent_budget_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("user_rent_budget",  budget_picked_begin + " - " + budget_picked_end)

      self.rent_budget.content.value = self.page.client_storage.get("user_rent_budget")
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

    self.rent_budget_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ЕЖЕМЕСЯЧНЫЙ БЮДЖЕТ", 
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


    ### Region chosing
    def close_searchbar_region(e):
      e.page.close(self.rent_region_popup)
      self.rent_region.content.value = self.page.client_storage.get("user_rent_region")
      page.update()

    self.button_confirm_region = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar_region
      )

    self.fake_region = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe", "tipa region"]

    def get_value_region(e):
      print(e.control.value)
      e.page.client_storage.set("user_rent_region", e.control.value)


    self.result_search_region = ft.Container(
      visible=False,
      height=150,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,

        ),
        on_change= get_value_region
      )
    )

    def show_results_region(e):
      if e.data:
        self.result_search_region.content.content.controls.clear()
        self.result_search_region.visible = True

        search_text = e.data.lower()
        matching_regions = [city for city in self.fake_region if search_text in city.lower()]

        for matched_region in matching_regions:
          self.result_search_region.content.content.controls.append(
            ft.Radio(
              label=matched_region,
              value=matched_region,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_region.visible = False
      
      page.update()

    self.search_bar_region = ft.Container(
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
            on_change=show_results_region
          )
        ]
      )
    )

    self.rent_region_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 200,
        width = 310,
        content= ft.Column([
          self.search_bar_region,
          self.result_search_region,
          ]
        )
      ),
      actions=[
        self.button_confirm_region,
      ],

    )

    ### Dates Chosing

    def close_dates_bar(e):
      e.page.close(self.rent_dates_popup)
      dates_picked_begin = self.rent_dates_popup.content.content.controls[2].controls[0].value
      dates_picked_end = self.rent_dates_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("user_rent_dates",  dates_picked_begin + " - " + dates_picked_end)

      self.rent_dates.content.value = self.page.client_storage.get("user_rent_dates")
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

    self.rent_dates_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ВЫБЕРИТЕ ДАТЫ АРЕНДЫ", 
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

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="landing_back.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(20,0,20,0),
          content= 
          ft.Column(
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment="center",
            controls = [
              ft.Container(
                content = 
                  ft.Text("ЕЩЕ НЕМНОГО И НАЧНЕМ", 
                          size = 18, 
                          text_align = "center",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD),
                                               font_family= "RussoOne-Regular",
                                               ),
                  ),
                  margin=ft.margin.only(0,0,0,40)
              ),     
              ft.Row(
                [
                  self.rent_country,
                  self.rent_city
                ],
                alignment= ft.MainAxisAlignment.CENTER,
              
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
                  self.rent_region,
                  self.rent_photos,
                  
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.rent_dates,
                ],
                alignment="center"
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
