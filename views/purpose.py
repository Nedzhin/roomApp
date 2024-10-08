import flet as ft
import aiohttp
import asyncio
class PurposePage(ft.View):
  def __init__(self, page: ft.Page, user_tid_back, BACK_URL) -> None:
    super().__init__(route = '/purpose', padding = 0)

    self.page = page
    self.bgcolor = "#FFFFFF"

    #print(self.page.client_storage.get("user_city"))
    #print(self.page.client_storage.get("user_surname"))
    def goto(e,self):
      print("gotton value baby: ",self.page.client_storage.get("user_name"))
      e.page.go('/anketa')
    self.button = ft.Container(
      height=55,
      width = 260,
      border_radius = 25,
      expand = True,
      bgcolor = "#B9A9FC",
      content = ft.Text("Назад", color = "white", size = 15, font_family= "RussoOne-Regular"),
      padding = ft.padding.only(left=10, right=10, top=0, bottom=0),
      margin= ft.margin.only(40, 0,40, 20),
      alignment = ft.alignment.center,
      on_click = lambda e: goto(e,self)
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
              ft.Container(
                content = 
                  ft.Text("ДАВАЙТЕ УТОЧНИМ, \nЧТО ВАС ИНТЕРЕСУЕТ?", 
                          size = 16, 
                          text_align = "center",
                          font_family= "RussoOne-Regular",
                          style = ft.TextStyle(color="#362D56", 
                                               size=18, 
                                               weight=ft.FontWeight(ft.FontWeight.BOLD),
                                               font_family= "RussoOne-Regular",
                                               ),
                  ),
                margin = ft.margin.all(40)      
              ),
              ft.Container(
                    ft.Text(
                      "Совместная аренда",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                              color="#FFFFFF", 
                              size=13, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                      text_align="center",
                    ),
                    on_click= lambda e: asyncio.run(user_registration_rent(e,self)),#e.page.go(),
                    bgcolor="#907CDC",
                    width=241,
                    height=65,
                    border_radius=25,
                    padding=ft.Padding(0,20,0,0),
                    margin=ft.Margin(0,25,0,15),
              ),
              ft.Container(
                    ft.Text(
                      "Соместные поездки",
                      font_family= "RussoOne-Regular",
                      style=ft.TextStyle(
                              color="#FFFFFF", 
                              size=13, 
                              weight=ft.FontWeight(ft.FontWeight.BOLD)
                              ),
                      text_align="center",
                    ),
                    on_click= lambda e: asyncio.run( user_registration_travel(e, self) ),
                    bgcolor="#907CDC",
                    width=241,
                    height=65,
                    border_radius=25,
                    padding=ft.Padding(0,20,0,0),
                    margin=ft.Margin(0,0,0,20),
              ),
              ft.Row(
              [
                ft.Image(
                src = "purpose1.png",
                fit = ft.ImageFit.COVER,
                animate_scale = ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                height=180,
                ),
              ],
              alignment= ft.MainAxisAlignment.CENTER,
              ),
              ft.Row(
                [
                self.button,
                ]
              )
            
            ]
          )
        )
      )
    ]
    async def user_registration_rent(e, self):
      user_name = self.page.client_storage.get("user_name")
      user_surname = self.page.client_storage.get("user_surname")
      user_tid = str(user_tid_back)
      #user_gender = self.page.client_storage.get("user_gender")
      user_birthday = self.page.client_storage.get("user_birthday")
      user_city = self.page.client_storage.get("user_city")
      user_education = self.page.client_storage.get("user_edu")
      user_job = self.page.client_storage.get("user_job")
      user_additional = self.page.client_storage.get("user_additional")


      e.page.go("/rent_var")
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          #print("information:",e.page.client_storage.get("user_name"))
          async with session.post(f'{BACK_URL}/user',
                               json={"username": user_name, "usersurname": user_surname, 'user_tid': user_tid,
        'gender': "male",
        'birthday': user_birthday,
        'city': user_city,
        'education': user_education,
        'job': user_job,
        'info': user_additional,
        'subscription': False,
        'purpose': False}) as response:
                if response.status == 200:
                  print("user created")
                  #print(response.json())
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.status}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}
      
    async def user_registration_travel(e, self):
      user_name = self.page.client_storage.get("user_name")
      user_surname = self.page.client_storage.get("user_surname")
      user_tid = str(user_tid_back)
      user_gender = self.page.client_storage.get("user_gender")
      user_birthday = self.page.client_storage.get("user_birthday")
      user_city = self.page.client_storage.get("user_city")
      user_education = self.page.client_storage.get("user_edu")
      user_job = self.page.client_storage.get("user_job")
      user_additional = self.page.client_storage.get("user_additional")


      e.page.go("/travel_var")
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          #print("information:",e.page.client_storage.get("user_name"))
          async with session.post(f'{BACK_URL}/user',
                               json={"username": user_name, "usersurname": user_surname, 'user_tid': user_tid,
        'gender': user_gender,
        'birthday': user_birthday,
        'city': user_city,
        'education': user_education,
        'job': user_job,
        'info': user_additional,
        'subscription': False,
        'purpose': True}) as response:
                if response.status == 200:
                  print("user created")
                  #print(response.json())
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.status}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}
