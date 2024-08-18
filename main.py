import flet as ft

import aiohttp
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from handlers.get_user import get_user
import requests

from views.landing import LandingPage
from views.anketa import AnketaPage
from views.purpose import PurposePage
from views.rent_var import RentVarPage
from views.travel_var import TravelVarPage
from views.rent_info import RentInfoPage
#from views.rent_info_short import RentInfoShortPage
from views.travel_info import TravelInfoPage
from views.end_reg import EndRegPage
from views.blind import BlindPage
from views.ankets import AnketsPage

def main(page: ft.Page):
  page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
  page.window.max_height = 820
  page.window.max_width = 390
  page.window.width = 390
  page.window.height = 790

  def change_navigation_destination(e: ft.TapEvent) -> None:
    if int(e.data) == 0:
      print("entered to blind")
      page.go('/blind')
    elif int(e.data) == 1:
      page.go('/ankets')
    elif int(e.data) == 2:
      page.go('/end_reg')
  
    page.update()

  nav_bar = ft.NavigationBar(
              destinations=[
            
                ft.NavigationBarDestination(
							  icon=ft.icons.PERSON_SEARCH_ROUNDED,
							  label="Слепой мэтч",
							  ),
                ft.NavigationBarDestination(
							  icon=ft.icons.PEOPLE_ALT_ROUNDED, 
							  label="Лента анкет",
							  ),
                ft.NavigationBarDestination(
                icon=ft.icons.PERSON_ROUNDED,
                label= "Мой профиль",
                #bgcolor="#786086",
                ),
              ],
				    bgcolor="#F5E5FF",
            adaptive=True,
				    height=65,
            on_change= change_navigation_destination
            )
  
  async def fetch_user_data():
    async with aiohttp.ClientSession() as session:
      print(session)
      async with session.get('http://127.0.0.1:8000/get-user', headers={'Content-Type': 'application/json'}) as response:
                try:
                    print("response:", response)
                    response = await response.json()
                    print(response)
                    user_id = response['user_id']
                    username = response['username']
                    return [user_id, username]
                except:
                    print('Invalid JSON data')
                    print(response)
                    raise HTTPException(status_code=400, detail='Invalid JSON data')
                finally:
                    await session.close()

  def router(route)->None:
    page.views.clear()
    if page.route == "/":
       page.go("/landing")
       #user_data = fetch_user_data()
       #print(user_data)

       
    if page.route == "/landing":
      landing = LandingPage(page)
      page.views.append(landing)

    if page.route == "/anketa":
      anketa = AnketaPage(page)
      page.views.append(anketa)
    
    if page.route == "/purpose":
      purpose = PurposePage(page)
      page.views.append(purpose)
    
    if page.route == "/rent_var":
      rent_var = RentVarPage(page)
      page.views.append(rent_var)

    if page.route == "/travel_var":
      travel_var = TravelVarPage(page)
      page.views.append(travel_var)
    
    if page.route == "/rent_info":
      rent_info = RentInfoPage(page)
      page.views.append(rent_info)
    
    # if page.route == "/rent_info_short":
    #   rent_info = RentInfoShortPage(page)
    #   page.views.append(rent_info)

    if page.route == "/travel_info":
      travel_info = TravelInfoPage(page)
      page.views.append(travel_info)

    if page.route == "/end_reg":
      end_reg = EndRegPage(page, nav_bar)
      page.views.append(end_reg)

    if page.route == "/blind":
      blind = BlindPage(page, nav_bar)
      page.views.append(blind)

    if page.route == "/ankets":
      ankets = AnketsPage(page, nav_bar)
      page.views.append(ankets)
    
    page.update()
    

  page.on_route_change = router
  print(page.route)
  page.go("/")
  page.update()


if __name__ == '__main__':
    try:
        text = 'App started'
        print(f'{text:*^30}')
        ft.app(target=main, view=None, port=8000)
    except:
        text = 'App not started'
        print(f'{text:*^30}')

