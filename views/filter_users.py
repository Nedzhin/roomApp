import flet as ft
import aiohttp
import asyncio

class FilerUsersPage(ft.View):
  def __init__(self, page: ft.Page, request_id, BACK_URL) -> None:
    super().__init__(route = '/filter_users', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
    self.filter_gender = ft.Container(
                    content = ft.Text(
                      value="ПОЛ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.gender_popup_filter)
    )

    self.filter_age = ft.Container(
                    content = ft.Text(
                      value="ВОЗРАСТ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.age_popup_filter)
    )
    
    self.filter_city = ft.Container(
                    content = ft.Text(
                      value="ГОРОД",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.filter_city_popup)
    )
    
    self.filter_edu = ft.Container(
                    content = ft.Text(
                      value="УРОВЕНЬ \nОБРАЗОВАНИЕ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",         
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.edu_popup_filter)
    )

    self.filter_job = ft.Container(
                    content = ft.Text(
                      value="СФЕРА ДЕЯТЕЛЬНОСТИ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=310,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.job_popup_filter)
    )

    self.filter_status = ft.Container(
                    content = ft.Text(
                      value="СТАТУС ПОЛЬЗОВАТЕЛЯ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=310,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.status_popup_filter)
    )

    ### Rent appearing options

    self.filter_rent_country = ft.Container(
                    content = ft.Text(
                      value="СТРАНА АРЕНДЫ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    visible=False,
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_country_popup)
    )

    self.filter_rent_city = ft.Container(
                    content = ft.Text(
                      value="ГОРОД АРЕНДЫ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    visible=False,
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_city_popup)
    )

    self.filter_rent_budget = ft.Container(
                    content = ft.Text(
                      value="МЕСЯЧНЫЙ БЮДЖЕТ \n(ОТ-ДО)",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    visible=False,
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_budget_popup)
    )

    self.filter_rent_dates = ft.Container(
                    content = ft.Text(
                      value="ДАТЫ АРЕНДЫ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    visible=False,
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_dates_popup)
    )
    
    self.filter_rent_region = ft.Container(
                    content = ft.Text(
                      value="РАЙОНЫ/СТАНЦИИ \nМЕТРО",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    visible=False,
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_region_popup)
    )

    self.filter_rent_photo = ft.Container(
                    content = ft.Text(
                      value="ФОТОГРАФИИ \nНЕДВИЖИМОСТИ",
                      style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    shadow=ft.BoxShadow(color="grey", blur_radius=10),
                    visible=False,
                    height=57,
                    width=153,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.rent_budget_popup)
    )   
    
    ### Travel additional blocks

    # self.filter_travel_longness = ft.Container(
    #                 content = ft.Text(
    #                   value="Длительность \nПоездки",
    #                   style= ft.TextStyle(color="#362D56", size=13, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
    #                   text_align = "center",
                      
    #                 ),
    #                 shadow=ft.BoxShadow(color="grey", blur_radius=10),
    #                 height=57,
    #                 width=153,
    #                 bgcolor="#FFFFFF",
    #                 border_radius=25,
    #                 padding=ft.padding.only(0,15,0,0),
    #                 on_click= lambda e: e.page.open(self.travel_longness_popup)
    # )

    self.button_apply = ft.Container(
      height=55,
      width = 260,
      border_radius = 25,
      expand = True,
      bgcolor = "#A0CE72",
      content = ft.Text("ПРИМЕНИТЬ", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: asyncio.run(filter_ankets(e, self))
    )

    self.button_decline = ft.Container(
      height=55,
      width = 120,
      border_radius = 25,
      expand = True,
      bgcolor = "#FE6A6A",
      content = ft.Text("ОТМЕНА", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/ankets')
    )

    self.button_restart = ft.Container(
      height=55,
      width = 120,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("СБРОСИТЬ", color = "white", size = 15, font_family= "RussoOne-Regular",),
      padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
      margin= ft.margin.only(40, 0,40,20),
      alignment = ft.alignment.center,
      on_click = lambda e: e.page.go('/filter_users')
    )


    ####### Gender chosing
    def close_gender_bar(e):
      e.page.close(self.gender_popup_filter)
      self.filter_gender.content.value = self.page.client_storage.get("users_gender_filter")
      page.update()
      
    self.button_confirm_gender = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ВЫБРАТЬ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_gender_bar
      )
    
    def get_value_gender(e):
      print(e.control.value)
      e.page.client_storage.set("users_gender_filter", e.control.value)

    self.gender_popup_filter = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ВЫБЕРЕТЕ ПОЛ", 
                          size = 16, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=3, color="transparent" ),
          ft.RadioGroup(
            
            content=ft.Column(
              controls = [
                ft.Radio(
                  label="ЖЕНСКИЙ",
                  value = "ЖЕНСКИЙ",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
                ft.Radio(
                  label="МУЖСКОЙ",
                  value = "МУЖСКОЙ",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
              ],
              horizontal_alignment="center"
            ),
            on_change= get_value_gender
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_gender,
      ],

    )

    ### Age chosing

    def close_age_bar(e):
      e.page.close(self.age_popup_filter)
      age_picked = self.age_popup_filter.content.content.controls[2].value
      self.page.client_storage.set("users_age_filter",  age_picked)
      self.filter_age.content.value = self.page.client_storage.get("users_age_filter")
      page.update()
      
    self.button_confirm_age = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_age_bar
      )
    

    self.age_popup_filter = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("НАПИШИТЕ ВОЗРАСТ", 
                          size = 18, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=4, color="transparent" ),
          ft.TextField(
            hint_text="Введите данные...",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            max_lines=1,
                            #expand=True,
                            width=204,
                            height=34,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
          ),
          ]
        )
      ),
      actions=[
        self.button_confirm_age,
      ],

    )

    ### City chosing

    def close_searchbar_city(e):
      e.page.close(self.filter_city_popup)
      self.filter_city.content.value = self.page.client_storage.get("users_city_filter")
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
      e.page.client_storage.set("users_city_filter", e.control.value)


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

    self.filter_city_popup = ft.AlertDialog(
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

    ########### Education chosing

    def get_value_edu(e):
      print(e.control.value)
      e.page.client_storage.set("users_edu_filter", e.control.value)
    
    self.edu_options = ["УЧУСЬ В ШКОЛЕ", "ЗАКОНЧИЛ ШКОЛУ, НЕ УЧУСЬ", "УЧУСЬ В БАКАЛАВРИАТЕ", "ЗАКОНЧИЛ БАКАЛАВРИАТ, НЕ УЧУСЬ", "УЧУСЬ В СПЕЦИАЛИТЕТЕ", "ЗАКОНЧИЛ СПЕЦИАЛИТЕТ, НЕ УЧУСЬ", "УЧУСЬ В МАГИСТРАТУРЕ", "ЗАКОНЧИЛ МАГИСТРАТУРУ, НЕ УЧУСЬ", "УЧУСЬ В АСПИРАНТУРЕ", "ЗАКОНЧИЛ АСПИРАНТУРУ"]

    self.result_search_edu = ft.Container(
      visible=True,
      height=410,
      width = 300,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=300,
          width=250,
          scroll=True,
          controls =[
            ft.Radio(
              label="УЧУСЬ В ШКОЛЕ",
              value="УЧУСЬ В ШКОЛЕ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="ЗАКОНЧИЛ ШКОЛУ, НЕ УЧУСЬ",
              value="ЗАКОНЧИЛ ШКОЛУ, НЕ УЧУСЬ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="УЧУСЬ В БАКАЛАВРИАТЕ",
              value="УЧУСЬ В БАКАЛАВРИАТЕ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              width = 250,
              label="ЗАКОНЧИЛ БАКАЛАВРИАТ, НЕ УЧУСЬ",
              value="ЗАКОНЧИЛ БАКАЛАВРИАТ, НЕ УЧУСЬ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="УЧУСЬ В СПЕЦИАЛИТЕТЕ",
              value="УЧУСЬ В СПЕЦИАЛИТЕТЕ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="ЗАКОНЧИЛ СПЕЦИАЛИТЕТ, НЕ УЧУСЬ",
              value="ЗАКОНЧИЛ СПЕЦИАЛИТЕТ, НЕ УЧУСЬ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ), 
            ft.Radio(
              label="УЧУСЬ В МАГИСТРАТУРЕ",
              value="УЧУСЬ В МАГИСТРАТУРЕ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="ЗАКОНЧИЛ МАГИСТРАТУРУ, НЕ УЧУСЬ",
              value="ЗАКОНЧИЛ МАГИСТРАТУРУ, НЕ УЧУСЬ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="УЧУСЬ В АСПИРАНТУРЕ",
              value="УЧУСЬ В АСПИРАНТУРЕ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="ЗАКОНЧИЛ АСПИРАНТУРУ",
              value="ЗАКОНЧИЛ АСПИРАНТУРУ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
          ]
        ),
        on_change= get_value_edu
      )
    )
    def show_results_edu(e):
      if e.data:
        self.result_search_edu.content.content.controls.clear()
        self.result_search_edu.visible = True

        search_text = e.data.lower()
        matching_edus = [edu for edu in self.edu_options if search_text in edu.lower()]
        for matched_edu in matching_edus:
          self.result_search_edu.content.content.controls.append(
            ft.Radio(
              label=matched_edu,
              value=matched_edu,
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_edu.visible = False
      
      page.update()

    self.search_bar_edu = ft.Container(
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
            on_change=show_results_edu
          )
        ]
      )
    )

    def close_edu_bar(e):
      e.page.close(self.edu_popup_filter)
      self.filter_edu.content.value = self.page.client_storage.get("users_edu_filter")
      #print(self.page.client_storage.get("user_gender"))
      page.update()

    self.button_confirm_edu = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_edu_bar
      )
    
    self.edu_popup_filter = ft.AlertDialog(
      #modal= True,
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 450,
        width = 300,
        content= ft.Column([
          self.search_bar_edu,
          self.result_search_edu,
          ]
        )
      ),
      actions=[
        self.button_confirm_edu,
      ],

    )

    #### Job Chosing

    def get_value_job(e):
      print(e.control.value)
      e.page.client_storage.set("users_job_filter", e.control.value)
    
    self.job_options = job_names = [
    "ЭКОНОМИКА И ФИНАНСЫ",
    "ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ (IT)",
    "ИСКУССТВО И КУЛЬТУРА",
    "ОБРАЗОВАНИЕ И НАУКА",
    "МЕДИЦИНА И ЗДРАВООХРАНЕНИЕ",
    "ИНЖЕНЕРИЯ И ТЕХНОЛОГИИ",
    "ЮРИСПРУДЕНЦИЯ",
    "БИЗНЕС И ПРЕДПРИНИМАТЕЛЬСТВО",
    "МАРКЕТИНГ И РЕКЛАМА",
    "ЖУРНАЛИСТИКА И СМИ",
    "ПОЛИТИКА И ГОСУДАРСТВЕННОЕ УПРАВЛЕНИЕ",
    "СОЦИАЛЬНАЯ РАБОТА И БЛАГОТВОРИТЕЛЬНОСТЬ",
    "СЕЛЬСКОЕ ХОЗЯЙСТВО",
    "АРХИТЕКТУРА И СТРОИТЕЛЬСТВО",
    "ПСИХОЛОГИЯ И ПСИХОТЕРАПИЯ",
    "ФИЛОСОФИЯ И ГУМАНИТАРНЫЕ НАУКИ",
    "СПОРТ И ФИЗИЧЕСКАЯ КУЛЬТУРА",
    "ТУРИЗМ И ГОСТИНИЧНЫЙ БИЗНЕС",
    "ТРАНСПОРТ И ЛОГИСТИКА",
    "ХИМИЯ И БИОТЕХНОЛОГИИ",
    "ЭКОЛОГИЯ И ОХРАНА ОКРУЖАЮЩЕЙ СРЕДЫ",
    "ЭНЕРГЕТИКА И ПРИРОДНЫЕ РЕСУРСЫ",
    "АВИАЦИЯ И КОСМОНАВТИКА",
    "МОДА И ДИЗАЙН",
    "МУЗЫКА И ЗВУКОРЕЖИССУРА",
    "ТЕАТР И КИНО",
    "ФАРМАЦЕВТИКА",
    "ОБСЛУЖИВАНИЕ И РЕМОНТ ТЕХНИКИ",
    "СЕКРЕТАРИАТ И АДМИНИСТРАТИВНАЯ РАБОТА",
    "РЕМЕСЛА И РУЧНОЙ ТРУД"
]

    self.result_search_job = ft.Container(
      visible=False,
      height=250,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,
          controls = [
            ft.Radio(
              label= "",
              value= "",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "",
              value= "",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "",
              value= "",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "",
              value= "",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
          ]
        ),
        on_change= get_value_job
      )
    )
    def show_results_job(e):
      if e.data:
        self.result_search_job.content.content.controls.clear()
        self.result_search_job.visible = True

        search_text = e.data.lower()
        matching_jobs = [job for job in self.job_options if search_text in job.lower()]
        for matched_job in matching_jobs:
          self.result_search_job.content.content.controls.append(
            ft.Radio(
              label=matched_job,
              value=matched_job,
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_job.visible = False
      
      page.update()

    self.search_bar_job = ft.Container(
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
            on_change=show_results_job
          )
        ]
      )
    )

    def close_job_bar(e):
      e.page.close(self.job_popup_filter)
      self.filter_job.content.value = self.page.client_storage.get("users_job_filter")
      #print(self.page.client_storage.get("user_gender"))
      page.update()

    self.button_confirm_job = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_job_bar
      )
    
    self.job_popup_filter = ft.AlertDialog(
      #modal= True,
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 310,
        width = 310,
        content= ft.Column([
          self.search_bar_job,
          self.result_search_job,
          ]
        )
      ),
      actions=[
        self.button_confirm_job,
      ],

    )

    ### Status chosing

    def close_status_bar(e):
      e.page.close(self.status_popup_filter)
      status_now = self.page.client_storage.get("users_status_filter")
      self.filter_status.content.value = status_now
      if status_now == "ЕСТЬ ЖИЛЬЁ, ИЩУ КРАТКОСРОЧНО" or  status_now == "ЕСТЬ ЖИЛЬЁ, ИЩУ ДОЛГОСРОЧНО":
        self.filter_rent_country.visible = True
        self.filter_rent_city.visible = True
        self.filter_rent_budget.visible = True
        self.filter_rent_dates.visible = True
        self.filter_rent_region.visible = True
        self.filter_rent_photo.visible = True
      elif status_now == "НЕТ ЖИЛЬЯ, ИЩУ КРАТКОСРОЧНО" or  status_now == "НЕТ ЖИЛЬЯ, ИЩУ ДОЛГОСРОЧНО":
        self.filter_rent_country.visible = True
        self.filter_rent_city.visible = True
        self.filter_rent_budget.visible = True
        self.filter_rent_dates.visible = True
        self.filter_rent_region.visible = True
        self.filter_rent_photo.visible = False
      else:
        self.filter_rent_country.visible = False
        self.filter_rent_city.visible = False
        self.filter_rent_budget.visible = False
        self.filter_rent_dates.visible = False
        self.filter_rent_region.visible = False
        self.filter_rent_photo.visible = False
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
      e.page.client_storage.set("users_status_filter", e.control.value)

    self.status_popup_filter = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 250,
        width=310,
        content= ft.Column(
          height=150,
          alignment="center",
          scroll=True,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          #ft.Divider(height=3, color="transparent" ),
          ft.RadioGroup(
            
            content=ft.Column(
              controls = [
                ft.Radio(
                  label="НЕТ ЖИЛЬЯ, ИЩУ ДОЛГОСРОЧНО",
                  value = "НЕТ ЖИЛЬЯ, ИЩУ ДОЛГОСРОЧНО",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
                ft.Radio(
                  label="НЕТ ЖИЛЬЯ, ИЩУ КРАТКОСРОЧНО",
                  value = "НЕТ ЖИЛЬЯ, ИЩУ КРАТКОСРОЧНО",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                  width=300,
                ),
                ft.Radio(
                  label="ЕСТЬ ЖИЛЬЁ, ИЩУ \nДОЛГОСРОЧНО",
                  value = "ЕСТЬ ЖИЛЬЁ, ИЩУ ДОЛГОСРОЧНО",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
                ft.Radio(
                  label="ЕСТЬ ЖИЛЬЁ, ИЩУ \nКРАТКОСРОЧНО",
                  value = "ЕСТЬ ЖИЛЬЁ, ИЩУ КРАТКОСРОЧНО",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                ),
                ft.Radio(
                  label="ПРИСОЕДИНИТЬСЯ К \nТУРИСТИЧЕСКОЙ ГРУППЕ",
                  value = "ПРИСОЕДИНИТЬСЯ К ТУРИСТИЧЕСКОЙ ГРУППЕ",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                  width=300,
                ),
                ft.Radio(
                  label="ИЩУ ЛЮДЕЙ В СВОЮ \nТУРИСТИЧЕСКУЮ ГРУППУ",
                  value = "ИЩУ ЛЮДЕЙ В СВОЮ ТУРИСТИЧЕСКУЮ ГРУППУ",
                  label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                  active_color="#D2BAE1",
                  width=300,
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




    ### Rent buttons logics

    ### Country chosing

    def close_searchbar_country_rent(e):
      e.page.close(self.rent_country_popup)
      self.filter_rent_country.content.value = self.page.client_storage.get("users_rent_country_filter")
      page.update()

    self.button_confirm_country_rent = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar_country_rent
      )

    self.fake_country = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe"]

    def get_value_country_rent(e):
      print(e.control.value)
      e.page.client_storage.set("users_rent_country_filter", e.control.value)


    self.result_search_country_rent = ft.Container(
      visible=False,
      height=150,
      content=ft.RadioGroup(    
        content=ft.Column(
          height=100,
          scroll=True,
        ),
        on_change= get_value_country_rent
      )
    )

    def show_results_country_rent(e):
      if e.data:
        self.result_search_country_rent.content.content.controls.clear()
        self.result_search_country_rent.visible = True

        search_text = e.data.lower()
        matching_countries = [city for city in self.fake_country if search_text in city.lower()]

        for matched_country in matching_countries:
          self.result_search_country_rent.content.content.controls.append(
            ft.Radio(
              label=matched_country,
              value=matched_country,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_country_rent.visible = False
      
      page.update()

    self.search_bar_country_rent = ft.Container(
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
            on_change=show_results_country_rent
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
          self.search_bar_country_rent,
          self.result_search_country_rent,
          ]
        )
      ),
      actions=[
        self.button_confirm_country_rent,
      ],

    )

    ### City chosing

    def close_searchbar_city_rent(e):
      e.page.close(self.rent_city_popup)
      self.filter_rent_city.content.value = self.page.client_storage.get("users_rent_city_filter")
      page.update()

    self.button_confirm_city_rent = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar_city_rent
      )

    self.fake_city = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe"]

    def get_value_city_rent(e):
      print(e.control.value)
      e.page.client_storage.set("users_rent_city_filter", e.control.value)


    self.result_search_city_rent = ft.Container(
      visible=False,
      height=150,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,

        ),
        on_change= get_value_city_rent
      )
    )

    def show_results_city_rent(e):
      if e.data:
        self.result_search_city_rent.content.content.controls.clear()
        self.result_search_city_rent.visible = True

        search_text = e.data.lower()
        matching_cities = [city for city in self.fake_city if search_text in city.lower()]

        for matched_city in matching_cities:
          self.result_search_city_rent.content.content.controls.append(
            ft.Radio(
              label=matched_city,
              value=matched_city,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search_city_rent.visible = False
      
      page.update()

    self.search_bar_city_rent = ft.Container(
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
            on_change=show_results_city_rent
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
          self.search_bar_city_rent,
          self.result_search_city_rent,
          ]
        )
      ),
      actions=[
        self.button_confirm_city_rent,
      ],

    )

    ### Budget chosing

    def close_budget_bar_rent(e):
      e.page.close(self.rent_budget_popup)
      budget_picked_begin = self.rent_budget_popup.content.content.controls[2].controls[0].value
      budget_picked_end = self.rent_budget_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("users_rent_budget_filter",  budget_picked_begin + " - " + budget_picked_end)

      self.filter_rent_budget.content.value = self.page.client_storage.get("users_rent_budget_filter")
      page.update()
      
    self.button_confirm_budget_rent = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_budget_bar_rent
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
        self.button_confirm_budget_rent,
      ],

    )

    ### Dates Chosing

    def close_dates_bar_rent(e):
      e.page.close(self.rent_dates_popup)
      dates_picked_begin = self.rent_dates_popup.content.content.controls[2].controls[0].value
      dates_picked_end = self.rent_dates_popup.content.content.controls[2].controls[1].value
      self.page.client_storage.set("users_rent_dates_filter",  dates_picked_begin + " - " + dates_picked_end)

      self.filter_rent_dates.content.value = self.page.client_storage.get("users_rent_dates_filter")
      page.update()
      
    self.button_confirm_dates_rent = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_dates_bar_rent
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
        self.button_confirm_dates_rent,
      ],

    )

      ### Region chosing
    def close_searchbar_region(e):
      e.page.close(self.rent_region_popup)
      self.filter_rent_region.content.value = self.page.client_storage.get("users_rent_region_filter")
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
      e.page.client_storage.set("users_rent_region_filter", e.control.value)


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

    ### Travel logic block
    ### Budget chosing

    # def close_budget_bar(e):
    #   e.page.close(self.travel_budget_popup)
    #   budget_picked_begin = self.travel_budget_popup.content.content.controls[2].controls[0].value
    #   budget_picked_end = self.travel_budget_popup.content.content.controls[2].controls[1].value
    #   self.page.client_storage.set("user_travel_budget",  budget_picked_begin + " - " + budget_picked_end)

    #   self.travel_budget.content.value = self.page.client_storage.get("user_travel_budget")
    #   page.update()
      
    # self.button_confirm_budget = ft.Container(
    #     border_radius = 25,
    #     expand = True,
    #     bgcolor = "#B9A9FC",
    #     content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
    #     padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
    #     margin= ft.margin.only(20, 0,20,40),
    #     alignment = ft.alignment.center,
    #     on_click = close_budget_bar
    #   )

    # self.travel_budget_popup = ft.AlertDialog(
    #   bgcolor="#FFFFFF",
    #   content=ft.Container(
    #     height= 140,
    #     width=310,
    #     content= ft.Column(
    #       alignment="center",
    #       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #       controls=[
    #       ft.Text("ЕЖЕДНЕВНЫЙ БЮДЖЕТ", 
    #                       size = 18, 
    #                       text_align = "center",
    #                       font_family= "RussoOne-Regular",
    #                       style = ft.TextStyle(color="#362D56", 
    #                                            size=18, 
    #                                            weight=ft.FontWeight(ft.FontWeight.BOLD)
    #                                            ),
    #               ),
    #       ft.Divider(height=4, color="transparent" ),
    #       ft.Row(
    #         alignment="center",
    #         controls=[
    #           ft.TextField(
    #                         hint_text="ОТ (₽)",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),
    #           ft.TextField(
    #                         hint_text="ДО (₽)",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),

    #         ]
    #       ),
    #       ]
    #     )
    #   ),
    #   actions=[
    #     self.button_confirm_budget,
    #   ],

    # )


    # ### Dates Chosing

    # def close_dates_bar_travel(e):
    #   e.page.close(self.travel_dates_popup)
    #   dates_picked_begin = self.travel_dates_popup.content.content.controls[2].controls[0].value
    #   dates_picked_end = self.travel_dates_popup.content.content.controls[2].controls[1].value
    #   self.page.client_storage.set("user_travel_dates",  dates_picked_begin + " - " + dates_picked_end)

    #   self.travel_dates.content.value = self.page.client_storage.get("user_travel_dates")
    #   page.update()
      
    # self.button_confirm_dates_travel = ft.Container(
    #     border_radius = 25,
    #     expand = True,
    #     bgcolor = "#B9A9FC",
    #     content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
    #     padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
    #     margin= ft.margin.only(20, 0,20,40),
    #     alignment = ft.alignment.center,
    #     on_click = close_dates_bar_travel
    #   )

    # self.travel_dates_popup = ft.AlertDialog(
    #   bgcolor="#FFFFFF",
    #   content=ft.Container(
    #     height= 140,
    #     width=310,
    #     content= ft.Column(
    #       alignment="center",
    #       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #       controls=[
    #       ft.Text("ВЫБЕРИТЕ ДАТЫ ПОЕЗДКИ", 
    #                       size = 18, 
    #                       text_align = "center",
    #                       font_family= "RussoOne-Regular",
    #                       style = ft.TextStyle(color="#362D56", 
    #                                            size=18, 
    #                                            weight=ft.FontWeight(ft.FontWeight.BOLD)
    #                                            ),
    #               ),
    #       ft.Divider(height=4, color="transparent" ),
    #       ft.Row(
    #         alignment="center",
    #         controls=[
    #           ft.TextField(
    #                         hint_text="ОТ",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),
    #           ft.TextField(
    #                         hint_text="ДО",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),

    #         ]
    #       ),
    #       ]
    #     )
    #   ),
    #   actions=[
    #     self.button_confirm_dates_travel,
    #   ],

    # )

    # ### Longness Chosing

    # def close_dates_bar(e):
    #   e.page.close(self.travel_longness_popup)
    #   dates_picked_begin = self.travel_longness_popup.content.content.controls[2].controls[0].value
    #   dates_picked_end = self.travel_longness_popup.content.content.controls[2].controls[1].value
    #   self.page.client_storage.set("user_longness_dates",  dates_picked_begin + " - " + dates_picked_end)

    #   self.travel_longness.content.value = self.page.client_storage.get("user_longness_dates")
    #   page.update()
      
    # self.button_confirm_dates = ft.Container(
    #     border_radius = 25,
    #     expand = True,
    #     bgcolor = "#B9A9FC",
    #     content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
    #     padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
    #     margin= ft.margin.only(20, 0,20,40),
    #     alignment = ft.alignment.center,
    #     on_click = close_dates_bar
    #   )

    # self.travel_longness_popup = ft.AlertDialog(
    #   bgcolor="#FFFFFF",
    #   content=ft.Container(
    #     height= 140,
    #     width=310,
    #     content= ft.Column(
    #       alignment="center",
    #       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #       controls=[
    #       ft.Text("НА КАКОЙ СРОК ВЫ \nПЛАНИРУЕТЕ ПОЕЗДКУ?", 
    #                       size = 18, 
    #                       text_align = "center",
    #                       font_family= "RussoOne-Regular",
    #                       style = ft.TextStyle(color="#362D56", 
    #                                            size=18, 
    #                                            weight=ft.FontWeight(ft.FontWeight.BOLD)
    #                                            ),
    #               ),
    #       ft.Divider(height=4, color="transparent" ),
    #       ft.Row(
    #         alignment="center",
    #         controls=[
    #           ft.TextField(
    #                         hint_text="МИН. ДНЕЙ",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),
    #           ft.TextField(
    #                         hint_text="МАКС. ДНЕЙ",
    #                         hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
    #                         width=134,
    #                         height=34,
    #                         color="#000000",
    #                         border_radius=25,
    #                         border_color = "#D9CAE0", 
    #                         bgcolor = "#FFFFFF",
    #                         text_align="center",
    #           ),

    #         ]
    #       ),
    #       ]
    #     )
    #   ),
    #   actions=[
    #     self.button_confirm_dates,
    #   ],

    # )

    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="anketa_background.png",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(20,20,20,20),
          content= 
          ft.Column(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
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
                  #self.travel_country,
                  self.filter_gender,
                  self.filter_age
                  
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_city,
                  self.filter_edu
                  #self.travel_dates,
                  #self.travel_longness
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_job
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_status
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_rent_country,
                  self.filter_rent_city
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_rent_budget,
                  self.filter_rent_region
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [
                  self.filter_rent_dates,
                  self.filter_rent_photo
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=
                [
                  ft.Row(
                    controls = [
                      self.button_apply
                    ],
                    alignment = "center"
                  ),
                  ft.Row(
                    controls = [
                      self.button_restart,
                      self.button_decline
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                    #alignment = "center"
                  )
                ]
              )
              
            ]
          )
        )
      )
    ]
    async def filter_ankets(e, self):
      #gender = self.page.client_storage.get("users_gender_filter")
      city = self.page.client_storage.get("users_city_filter")
      #user_tid = str(user_tid_back)
      #print(type(gender))
      print(city)
      print(type(city))
      city = str(city)


      e.page.go('/ankets')
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          #print("information:",e.page.client_storage.get("user_name"))
          async with session.get(f'{BACK_URL}/filter_profiles/{request_id}',
                               params={'city': city}) as response:
                if response.status == 200:
                  print("users filter applied")
                  #print(response.json())
                  profiles = await response.json()
                  print(profiles)
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.status}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}
