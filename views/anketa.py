import flet as ft
from controllers.user_add_data import add_new
#from controllers.user_read_data import read_data
# change (not important)
class AnketaPage(ft.View):
  
  
  def __init__(self, page) -> None:
    super().__init__(route = '/anketa', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"
    self.page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
    
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
      #e.page.close(self.experiment_container)

    self.anketa_image = ft.Image(
                    "women.jpg",
                    fit=ft.ImageFit.COVER,
                    width=120,
                    height=150,
                    border_radius=15,
                    )
    
   
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
                        cursor_color='white'
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
    
    self.user_gender = ft.Dropdown(
                        hint_text="ПОЛ",
                        hint_style= ft.TextStyle(color="#362D56", size=12, font_family= "RussoOne-Regular",),
                        height=40,
                        width=50,
                        bgcolor="#FFFFFF",
                        color="#362D56",
                        border_color="#FFFFFF",
                        #border_radius=25,
                        options=[
                          ft.dropdown.Option("Женщина", text_style=ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),),
                          ft.dropdown.Option("Mужчина", text_style=ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),),
                        ]
    )
    # self.user_gender = ft.TextField(
    #                     hint_text="ПОЛ",
    #                     hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",),
    #                     width=130,
    #                     height = 40,
    #                     text_align = "center",
    #                     border_radius=25,
    #                     border_color = "#FFFFFF",
    #                     color = "black",
    #                     bgcolor="#FFFFFF"
    #                   )
    
    #self.user_birthday = 
    self.user_birthday = ft.TextField(
                          hint_text="ДД.ММ.ГГ",
                          hint_style = ft.TextStyle(color="#362D56", size=12, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                          width=165, 
                          height = 40,
                          text_align = "center",
                          border_radius=25,
                          border_color = "#FFFFFF",
                          color = "black",
                          bgcolor = "#FFFFFF",
                          # on_focus= lambda e: self.page.open(ft.DatePicker(
                            
                          # ))
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
    
    self.user_university = ft.TextField(
                            hint_text="УНИВЕРСИТЕТ",
                             hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                            width=165,
                            height = 40,
                            text_align = "center", 
                            border_radius=25,
                            border_color = "#FFFFFF", 
                            bgcolor = "#FFFFFF",
                          )
    
    self.user_job = ft.TextField(
                      hint_text="СФЕРА ДЕЯТЕЛЬНОСТИ",
                      hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",), 
                      width=310,
                      height = 40,
                      text_align = "center", 
                      border_radius=25, 
                      bgcolor = "#FFFFFF",
                      border_color = "#FFFFFF",
                    )
    
      
    self.user_additional = ft.Container(
                          ft.TextField(
                            hint_text="ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ",
                            hint_style = ft.TextStyle(color="#362D56", size=11, weight=ft.FontWeight(ft.FontWeight.BOLD), font_family= "RussoOne-Regular",  ),
                            max_lines=6,
                            #expand=True,
                            width=310,
                            height=110,
                            color="black",
                            border_radius=25,
                            border_color = "#FFFFFF", 
                            bgcolor = "#FFFFFF",
                            text_align="center",
                            
                          ),
                          bgcolor="White",
                          height=110,
                          border_radius=25,
                          padding=ft.Padding(0, 25,0,0),
                          on_click = lambda _: self.change_additional(),
    )
    
    self.button = ft.Container(
        border_radius = 25,
        expand = True,
        bgcolor = "#B9A9FC",
        content = ft.Text("Продолжить заполнение", color = "white", size = 15, font_family= "RussoOne-Regular",),
        padding = ft.padding.only(left=0, right=0, top=10, bottom=10),
        margin= ft.margin.only(20, 0,20,40),
        alignment = ft.alignment.center,
        on_click = lambda e: self.on_add_new(e)
      )
    
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


    self.experiment_container = ft.AlertDialog(
      #modal= True,
      bgcolor="#FFFFFF",
      content=ft.Container(
        height= 300,
        content= ft.Column([
          ft.SearchBar(
            view_elevation=4,
            bar_overlay_color="white",
            bar_bgcolor="white",
            bar_leading=ft.IconButton(icon="search", icon_color="#362D56"),
            controls=[
              ft.Checkbox(label="bogie")
            ]
          ),
          self.anketa_image,
          ft.Text("Buirtsa bari bolad"),
          

          ]
        )
      ),
      actions=[
        self.button_confirm,
      ],

    )
    # self.button_check = ft.Container(
    #     border_radius = 25,
    #     expand = True,
    #     bgcolor = "#B9A9FC",
    #     content = ft.Text("Check database", color = "white", size = 15),
    #     padding = ft.padding.only(left=25, right=25, top=10, bottom=10),
    #     margin= ft.margin.only(40, 0,40,40),
    #     alignment = ft.alignment.center,
    #     on_click = lambda e: self.did_mount()
    #   )


    self.controls = [
      ft.SafeArea(
        expand = True,
        content = ft.Container(
          image_src="anketa_background.png", #if 1 else "women",
          expand=True,
          image_fit=ft.ImageFit.COVER,
          padding=ft.padding.only(40,40,40,40),
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
                  ft.Container(
                    self.user_gender,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    width=130,
                    height = 40,
                    padding=ft.Padding(25,5,0,0)
                  ),
                  
                  self.user_birthday,
                ],
                alignment= ft.MainAxisAlignment.CENTER
              ),
              ft.Row(
                [ 
                  self.user_city,
                  self.user_university,
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
  # def did_mount(self):
  #   self.load()

  # def load(self):
  #   data_json = read_data()
  #   print(data_json)

  def on_add_new(self, e):
    try:
      user_name = self.user_name.value
      user_surname = self.user_surname.value
      user_gender  = self.user_gender.value
      #print(user_name)
      e.page.client_storage.set("user_name", user_name)
      e.page.client_storage.set("user_surname", user_surname)
      # add_new(
      #   user_name = user_name
      # )
      self.reset_input()
      e.page.go('/purpose')
    except Exception as err:
      print(err)

  def reset_input(self):
    self.user_name = ""
    self.update()
  
  def change_additional(self,):
      self.user_additional.padding = ft.Padding(0,0,0,0)
      self.page.update()