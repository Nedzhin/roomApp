from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import router as controllers_router
from database import firebase

from dotenv import load_dotenv
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.types import Message, Update, WebAppInfo
from typing import Any
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from datetime import datetime
from fastapi import Request, HTTPException
from json import JSONDecodeError

logging.basicConfig(level=logging.INFO)
load_dotenv()

TOKEN = os.environ["TELEGRAM_TOKEN"]
BACK_URL = os.environ["BACK_URL"]
REACT_URL = os.environ["FRONT_URL"]
print("front url:", REACT_URL)
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = BACK_URL + WEBHOOK_PATH

#initializing the bot
bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     logging.info("Setting up the webhook")
#     await bot.set_webhook(url=WEBHOOK_URL,
#                           allowed_updates=dp.resolve_used_update_types(),
#                           drop_pending_updates=True)
#     yield
#     logging.info("Deleting the webhook on shutdown")
#     await bot.delete_webhook()

#initializing the FastApi App
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup() -> None:
    logging.info("Started")
    firebase.create_database()
    print("started")
    webhook_url = WEBHOOK_URL
    print("value gotton from env",WEBHOOK_URL)
    webhook_info = await bot.get_webhook_info()
    print(webhook_info.url)
    print(webhook_url)
    if webhook_info.url != webhook_url:
        await bot.set_webhook(
            url=webhook_url,
            allowed_updates=["message", "callback_query"]
        )
    
@app.post(WEBHOOK_PATH)
async def webhook(update: dict[str, Any]) -> None:
    logging.info(f"Received update: {update}")
    await dp.feed_webhook_update(bot=bot, update=types.Update(**update))

@app.on_event("shutdown")
async def on_shutdown() -> None:
    logging.info(f"Shut down")
    await bot.session.close()
    await bot.delete_webhook()
    
def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Open the Room app",
        web_app=WebAppInfo(
             url = REACT_URL
             )
    )
    return builder.as_markup()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    print(message.from_user.username)
    await message.answer("Hi")
    await message.reply(
        "Let's go!",
        reply_markup=webapp_builder()
        )
    


# @app.post(WEBHOOK_PATH)
# async def webhook(update: dict[str, Any]) -> None:
#     logging.info(f"Received update: {update}")
#     await dp.feed_webhook_update(bot=bot, update=types.Update(**update))

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


app.include_router(controllers_router)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )