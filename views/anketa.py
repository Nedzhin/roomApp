import flet as ft
import asyncio
#from controllers.user_read_data import read_data
# change (not important)
class AnketaPage(ft.View):
  
  
  def __init__(self, page) -> None:
    super().__init__(route = '/anketa', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}

    # if self.page.client_storage.contains_key("user_city"):
    #   print("kotoche anketadan aldm:", self.page.client_storage.contains_key("user_city"))

    def resup( e: ft.FilePickerResultEvent):
      print(e.data)
      print('entered')
      if e.files:
        self.anketa_image.src = e.files[0].path
        page.update()

    self.myfile = ft.FilePicker(on_result=resup)
    self.page.overlay.append(self.myfile)


    def close_searchbar(e):
      #self.experiment_container.open = False
      e.page.close(self.experiment_container)
      self.user_city.content.value = self.page.client_storage.get("user_city")
      #print(self.page.client_storage.get("user_city"))
      page.update()
      #e.page.close(self.experiment_container)

    self.anketa_image = ft.Image(
                    "women.jpg",
                    fit=ft.ImageFit.COVER,
                    width=120,
                    height=150,
                    border_radius=15,
                    )
    
    def check(e):
      print(self.user_name.value)

    self.user_name = ft.TextField(
                        hint_text = "Имя",
                        hint_style = ft.TextStyle(
                          color="#362D56", 
                          size=18, 
                          weight=ft.FontWeight(ft.FontWeight.BOLD),
                          font_family= "RussoOne-Regular"
                          ),
                        height = 20,
                        border= 'none',
                        color="black",
                        cursor_color='white',
                        on_submit=check
                      )
    
    self.user_surname = ft.TextField(
                        hint_text = "Фамилия",
                        hint_style = ft.TextStyle(
                          color="#362D56", 
                          size=18, 
                          weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),
                        height = 20,
                        border= 'none',
                        color="black",
                        cursor_color='white'
                      )
    
    self.user_gender = ft.Container(
                    content = ft.Text(
                      value="ПОЛ",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=40,
                    width=130,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.gender_popup)
    )

    self.user_birthday = ft.Container(
                    content = ft.Text(
                      value="ДАТА",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=40,
                    width=165,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.date_popup)
    )

    self.user_city = ft.Container(
                    content = ft.Text(
                      value="ГОРОД",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=40,
                    width=130,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.experiment_container)
    )
    
    self.user_edu = ft.Container(
                    content = ft.Text(
                      value="ОБРАЗОВАНИЕ",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",         
                    ),
                    height=40,
                    width=165,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.edu_popup)
    )
    
    self.user_job = ft.Container(
                    content = ft.Text(
                      value="СФЕРА ДЕЯТЕЛЬНОСТИ",
                      style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD),font_family= "RussoOne-Regular",),
                      text_align = "center",
                      
                    ),
                    height=40,
                    width=310,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=ft.padding.only(0,15,0,0),
                    on_click= lambda e: e.page.open(self.job_popup)
    )
    
      
    self.user_additional = ft.Container(
                          content= ft.Text(
                            value="ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ",
                            style= ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            width=310,
                            height=110,
                            color="#362D56",
                            bgcolor = "#FFFFFF",
                            text_align="center"
                          ),
                          bgcolor="White",
                          height=110,
                          border_radius=25,
                          padding=ft.Padding(0, 40,0,0),
                          on_click = lambda e: e.page.open(self.add_popup),
    )

    # def on_add_new(e, self):
      

    #   e.page.client_storage.set("user_name", self.user_name.value)
    #   e.page.client_storage.set("user_surname", self.user_surname.value)
    #   print("value of the field:", self.user_name.value)
    #   print("value in the client storage:", self.page.client_storage.get("user_name"))
    #   e.page.go('/purpose')

    self.button = ft.Container(
        height=55,
        width = 260,
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("Продолжить заполнение", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,20),
        alignment = ft.alignment.center,
        on_click = lambda e: asyncio.run(user_registration(e, self) )#lambda e: self.on_add_new(e)
      )
    
    ##################### Search bars with checkboxes ###################

    ##### City chosing 

    self.button_confirm = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ПОДТВЕРДИТЬ ВЫБОР", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_searchbar
      )

    self.fake_city = ["america", "canada", "belarus", "almaty", "astana", "taraz", "aktobe"]
    def get_value_city(e):
      #print(e.control.value)
      e.page.client_storage.set("user_city", e.control.value)


    self.result_search = ft.Container(
      visible=True,
      height=150,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,
          controls=[
          ft.Radio(
              label="САМАРА",
              value="САМАРА",
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ), 
            ft.Radio(
              label="САНКТ-ПЕТЕРБУРГ",
              value="САНКТ-ПЕТЕРБУРГ",
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="МОСКВА",
              value="МОСКВА",
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label="ЕКАТЕРИНБУРГ",
              value="ЕКАТЕРИНБУРГ",
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
          ]
        ),
        on_change= get_value_city
      )
    )

    def show_results(e):
      if e.data:
        #self.result_search.content.controls[0].controls.clear()
        self.result_search.content.content.controls.clear()
        self.result_search.visible = True

        search_text = e.data.lower()
        matching_cities = [city for city in self.fake_city if search_text in city.lower()]

        for matched_city in matching_cities:
          # self.result_search.content.controls[0].controls.append(
          #   ft.Checkbox(
          #     label=matched_city,
          #     label_style=ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
          #     shape=ft.RoundedRectangleBorder(radius=30),
          #     active_color="#D2BAE1",
          #     on_change = lambda e: e.page.client_storage.set("user_city", matched_city)
          #   )
          # )
          self.result_search.content.content.controls.append(
            ft.Radio(
              label=matched_city,
              value=matched_city,
              label_style= ft.TextStyle(color="#362D56", size=14, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            )
          )
      else:
        self.result_search.visible = False
      
      page.update()

    self.search_bar = ft.Container(
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
            on_change=show_results
          )
        ]
      )
    )

    self.experiment_container = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 200,
        width = 310,
        content= ft.Column([
          self.search_bar,
          self.result_search,
          ]
        )
      ),
      actions=[
        self.button_confirm,
      ],

    )


    ####### Gender chosing
    def close_gender_bar(e):
      e.page.close(self.gender_popup)
      self.user_gender.content.value = self.page.client_storage.get("user_gender")
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
      e.page.client_storage.set("user_gender", e.control.value)

    self.gender_popup = ft.AlertDialog(
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

    ########### Education chosing

    def get_value_edu(e):
      print(e.control.value)
      e.page.client_storage.set("user_edu", e.control.value)
    
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
      e.page.close(self.edu_popup)
      self.user_edu.content.value = self.page.client_storage.get("user_edu")
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
    
    self.edu_popup = ft.AlertDialog(
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
      e.page.client_storage.set("user_job", e.control.value)
    
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
      visible=True,
      height=250,
      content=ft.RadioGroup(
        
        content=ft.Column(
          height=100,
          scroll=True,
          controls = [
            ft.Radio(
              label= "МАРКЕТИНГ И РЕКЛАМА",
              value= "МАРКЕТИНГ И РЕКЛАМА",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "ИНЖЕНЕРИЯ И ТЕХНОЛОГИИ",
              value= "ИНЖЕНЕРИЯ И ТЕХНОЛОГИИ",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ (IT)",
              value= "ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ (IT)",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "АВИАЦИЯ И КОСМОНАВТИКА",
              value= "АВИАЦИЯ И КОСМОНАВТИКА",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "МОДА И ДИЗАЙН",
              value= "МОДА И ДИЗАЙН",
              label_style= ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
              active_color="#D2BAE1",
            ),
            ft.Radio(
              label= "ПОЛИТИКА И ГОСУДАРСТВЕННОЕ УПРАВЛЕНИЕ",
              value= "ПОЛИТИКА И ГОСУДАРСТВЕННОЕ УПРАВЛЕНИЕ",
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
      e.page.close(self.job_popup)
      self.user_job.content.value = self.page.client_storage.get("user_job")
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
    
    self.job_popup = ft.AlertDialog(
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


### Date chosing

    def close_date_bar(e):
      e.page.close(self.date_popup)
      date_picked = self.date_popup.content.content.controls[2].value
      self.page.client_storage.set("user_birthday",  date_picked)
      self.user_birthday.content.value = self.page.client_storage.get("user_birthday")
      page.update()
      
    self.button_confirm_date = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_date_bar
      )
    
    # def get_value_date(e):
    #   print(e.control.value)
    #   e.page.client_storage.set("user_gender", e.control.value)

    self.date_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 140,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ВАША ДАТА РОЖДЕНИЯ", 
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
        self.button_confirm_date,
      ],

    )


### Additional info chosing

    def close_add_bar(e):
      e.page.close(self.add_popup)
      add_picked = self.add_popup.content.content.controls[2].content.value
      self.page.client_storage.set("user_additional",  add_picked)
      self.user_additional.content.value = self.page.client_storage.get("user_additional")
      page.update()
      
    self.button_confirm_add = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("ДАЛЕЕ", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = close_add_bar
      )

    self.add_popup = ft.AlertDialog(
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 386,
        width=310,
        content= ft.Column(
          alignment="center",
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          controls=[
          ft.Text("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ", 
                          size = 13, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD)
                                               ),
                  ),
          ft.Divider(height=4, color="transparent" ),
          ft.Container(
            content = 
            ft.TextField(
            hint_text="Напишите \nинформацию о себе..",
                            hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            max_lines=6,
                            #expand=True,
                            width=250,
                            height=210,
                            color="#000000",
                            border_radius=25,
                            border_color = "#D9CAE0", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
          ),
          height=210,
          )
          
          ]
        )
      ),
      actions=[
        self.button_confirm_add,
      ],

    )

### The main content
    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="anketa_background.png", #if 1 else "women",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(20,20,20,20),
          content= 
          ft.Column(
            alignment = "spaceBetween",
            horizontal_alignment="center",
            controls = [
              ft.Row(
                [
                  ft.Text(
                    "Анкета", 
                    style="titleLarge", 
                    color="#786086",
                    text_align="center",
                    font_family= "RussoOne-Regular",
                  )
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                vertical_alignment="center",
                controls = [
                  ft.Container(
                    self.anketa_image,
                    on_click= lambda _: self.myfile.pick_files(),
                    margin=ft.margin.only(20,0,0,0)
                  ),
                  ft.VerticalDivider(
                    width=20,
                  ),
                  ft.Column(
                    alignment="center",
                    controls=[
                      self.user_name,
                      self.user_surname
                    ]
                  )
                ],
                alignment = "center"
              ),
              ft.Row(
                [ 
                  self.user_gender, 
                  self.user_birthday,
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [ 
                  self.user_city,
                  self.user_edu,
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [ 
                  self.user_job,
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [ 
                    self.user_additional,
                  
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment="center"
              ),
              ft.Row(
                controls = [
                  self.button,
                  #self.button_check,
                ],
                alignment = "center"
              )
            ]
          )
        )
      )
    ]

    async def user_registration(e, self):
      e.page.client_storage.set("user_name", self.user_name.value)
      e.page.client_storage.set("user_surname", self.user_surname.value)
      print("value of the field:", self.user_name.value)
      print("value in the client storage:", self.page.client_storage.get("user_name"))

      e.page.go('/purpose')
    

  # def did_mount(self):
  #   self.load()

  # def load(self):
  #   data_json = read_data()
  #   print(data_json)

  
    #try:
    #   # user_name = self.user_name.value
    #   # user_surname = self.user_surname.value
    #   #user_gender  = self.user_gender.value
    #   #print(user_name)
    #   # e.page.client_storage.set("user_name", user_name)
    #   # e.page.client_storage.set("user_surname", user_surname)
    #   # add_new(
    #   #   user_name = user_name
    #   # )
    #   # self.reset_input()
    #   e.page.go('/purpose')
    # except Exception as err:
    #   print(err)

  # def reset_input(self):
  #   self.user_name = ""
  #   self.update()