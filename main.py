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
from views.travel_info import TravelInfoPage
from views.end_reg import EndRegPage
from views.blind import BlindPage
from views.ankets import AnketsPage
from views.settings_sample import SettingsSamplePage
from views.filter_users import FilerUsersPage

import time
from dotenv import load_dotenv
import os


def main(page: ft.Page):
  load_dotenv()
  BACK_URL = os.environ["BACK_URL"]
  print("URL in main:", BACK_URL)
  page.fonts = {"RussoOne-Regular":"fonts/RussoOne-Regular.ttf"}
  page.window.max_height = 820
  page.window.max_width = 410
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
                #bgcolor="black",
                ),
              ],
				    bgcolor="#F5E5FF",
            #shadow_color= "black",
            #indicator_color="black",
            shadow_color="blue",
            #overlay_color= {ft.ControlState.FOCUSED: ft.colors.GREEN, ft.ControlState.HOVERED: "grey", ft.ControlState.SELECTED: "white"},
            adaptive=True,
				    height=65,
            on_change= change_navigation_destination
            )
  
  async def fetch_user_data():
    async with aiohttp.ClientSession() as session:
      print(session)
      async with session.get(f'{BACK_URL}/get-user', headers={'Content-Type': 'application/json'}) as response:
                try:
                    #print("response:", response)
                    response = await response.json()
                    print("response from fetch: ",response)
                    user_id = response['user_id']
                    username = response['username']
                    print("get from database:", user_id, username)
                    return [user_id, username]
                except:
                    print('Invalid JSON data')
                    print(response)
                    raise HTTPException(status_code=400, detail='Invalid JSON data')
                finally:
                    await session.close()

  async def get_information(user_tid):
      #print(user_tid)
      #print('https://abf7-109-239-43-7.ngrok-free.app/user/{user_tid}')
      url = f'{BACK_URL}/user/{user_tid}'
      #print(url)
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          async with session.get(url,
                               ) as response:
                if response.status == 200:
                  print("user created")
                  #print(response.json())
                  response_got = await response.json()
                  print("checking:", response_got)
                  # user_id = response_got['user_tid']
                  # username = response_got['username']
                  # print("get from database:", user_id, username)
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.status}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}

  async def get_filtered_profiles(request_id):
      try:
        async with aiohttp.ClientSession() as session:
          print(session)
          #print("information:",e.page.client_storage.get("user_name"))
          async with session.get(f'{BACK_URL}/get_filtered_profiles/{request_id}',
                               ) as response:
                if response.status == 200:
                  print("users filter applied")
                  #print(response.json())
                  profiles = await response.json()
                  #print(profiles)
                  print("from ankets, shynymen saqtaldmeken",profiles)
                  return await response.json()
                else:
                  return {"error": f"Failed to create user, status code: {response.status}"}
        
      except aiohttp.ClientError as e:
        return {"error": str(e)}
  async def router(route)->None:
    global user_tele_data
    page.views.clear()
    if page.route == "/":
       page.go("/landing")
       user_tele_data = await fetch_user_data()
       #user_tele_data[0] = 123456756
      #  print(user_data)

       
    if page.route == "/landing":
      landing = LandingPage(page)
      page.views.append(landing)

    if page.route == "/anketa":
      print("from anketa page: ",user_tele_data)
      anketa = AnketaPage(page)
      page.views.append(anketa)
    
    if page.route == "/purpose":
      user_tid = str(user_tele_data[0])
      purpose = PurposePage(page, user_tid, BACK_URL)
      page.views.append(purpose)
    
    if page.route == "/rent_var":
      rent_var = RentVarPage(page)
      page.views.append(rent_var)

    if page.route == "/travel_var":
      travel_var = TravelVarPage(page)
      page.views.append(travel_var)
    
    if page.route == "/rent_info":
      user_tid = str(user_tele_data[0])
      #user_tid = str(123456780)
      print("user telegram id from rent info:", user_tid)
      rent_info = RentInfoPage(page, user_tid, BACK_URL)
      page.views.append(rent_info)
    
    if page.route == "/travel_info":
      user_tid = str(user_tele_data[0])
      #user_tid = str(123456780)
      travel_info = TravelInfoPage(page, user_tid, BACK_URL)
      page.views.append(travel_info)

    if page.route == "/end_reg":
      time.sleep(1)
      print("accessed from endreg",user_tele_data[0])
      request_id  = str(user_tele_data[0])
      #request_id = str(123456780)
      userdata = await get_information(request_id)
      print("I got from main page:", userdata)

      if userdata["anketa"]["purpose"] == "True":
         aim = 1
      else:
         aim = 0
         
      end_reg = EndRegPage(page, nav_bar, userdata, aim)
      page.views.append(end_reg)

    if page.route == "/blind":
      blind = BlindPage(page, nav_bar)
      page.views.append(blind)

    if page.route == "/ankets":
      request_id  = str(user_tele_data[0])
      results_profiles = await get_filtered_profiles(request_id)
      print(results_profiles)
      #results_profiles = results_profiles["filtered_profiles"]['found_profiles']
      ankets = AnketsPage(page, nav_bar, results_profiles)
      page.views.append(ankets)
    
    if page.route =="/settings_sample":
       settings_sample = SettingsSamplePage(page, nav_bar)
       page.views.append(settings_sample)
    
    if page.route == "/filter_users":
      request_id  = str(user_tele_data[0])
      print("maindag request id", request_id)
      filter_users = FilerUsersPage(page, request_id,BACK_URL)
      page.views.append(filter_users)

    page.update()
    

  page.on_route_change = router
  print(page.route)
  page.go("/")

  page.update()


if __name__ == '__main__':
    try:
        text = 'App started'
        print(f'{text:*^30}')
        ft.app(target=main, view=None, port=4000)
    except:
        text = 'App not started'
        print(f'{text:*^30}')

