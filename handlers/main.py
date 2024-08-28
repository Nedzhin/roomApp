# from handlers.router import router
# from fastapi import FastAPI
# import firebase_admin
# from handlers.config import get_settings


# app = FastAPI()
# app.include_router(router)
# firebase_admin.initialize_app()

# settings = get_settings()
# origins = [settings.frontend_url]
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TELEGRAM_TOKEN"]
BACK_URL = os.environ["BACK_URL"]
REACT_URL = os.environ["FRONT_URL"]

WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = BACK_URL + WEBHOOK_PATH

#print(WEBHOOK_URL)
import json
from json import JSONDecodeError
import logging
from datetime import datetime
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, Update, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from fastapi import FastAPI
from aiogram.utils.keyboard import InlineKeyboardBuilder


from fastapi.requests import Request
import uvicorn
from contextlib import asynccontextmanager
from typing import Any
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url=WEBHOOK_URL,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)
# app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="templates")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

user_id = ""
username = ""

def webapp_builder(username) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Open the Room app",
        #url = "https://medium.com/@ustsl/telegram-mini-applications-8a2602d6d4b8",
        web_app=WebAppInfo(
             url= REACT_URL
             )
    )
    return builder.as_markup()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    #await message.answer('Привет!')

    print(message.from_user.username)
    await message.reply(
        "Let's go!",
        reply_markup=webapp_builder(message.from_user.username)
        )


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.on_event("startup")
async def on_startup() -> None:
    webhook_url = WEBHOOK_URL
    webhook_info = await bot.get_webhook_info()
    print(webhook_info.url)
    if webhook_info.url != webhook_url:
        print("qoiyldy")
        await bot.set_webhook(
            url=webhook_url,
            # allowed_updates=["message", "callback_query"]
        )

@app.post(WEBHOOK_PATH)
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    #await dp.feed_webhook_update(bot=bot, update=types.Update(**update))


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await bot.session.close()

@app.post("/get-data")
async def get_user(request: Request):
    global user_id
    global username
    
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        print('No Content-Type provided')
        raise HTTPException(status_code=400, detail='No Content-Type provided')
    elif content_type == 'application/json':
        print("eemaa bolgan siaqty")
        try:
            result = await request.json()
            print("this is the result of the entering data",result)
            user_id = result['user_id']
            username = result['username']

            print(f'\n{datetime.now()}\n/get-data\nUser ID: {user_id}; Username: {username}')
            # db.add_user(result['user_id'], result['username'])
            # db.add_boost(result['user_id'], "power_click", 1)
            return JSONResponse(status_code=200, content=result)
        except JSONDecodeError:
            print('Invalid JSON data')
            raise HTTPException(status_code=400, detail='Invalid JSON data')
    else:
        print('Content-Type not supported')
        raise HTTPException(status_code=400, detail='Content-Type not supported')


@app.get("/get-user")
async def get_user_id():
    global user_id
    global username
    user_data = {'user_id': user_id, 'username': username}
    user_id = ''
    username = ''
    print(f'\n{datetime.now()}\n/get-user\nUser ID: {user_id}; Username: {username}')
    return JSONResponse(content=user_data, media_type="application/json")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

