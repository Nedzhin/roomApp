import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup

def webapp_builder(username) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Open the Room app",
        #url = "https://medium.com/@ustsl/telegram-mini-applications-8a2602d6d4b8",
        web_app=WebAppInfo(
             url=f'https://83d9-109-239-43-7.ngrok-free.app'
             )
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    print(message.from_user.username)
    await message.reply(
        "Let's go!",
        reply_markup=webapp_builder(message.from_user.username)
        )

async def main() -> None:
    bot = Bot(token="7033953674:AAFCoYER2twhVSSj3RPJ4H-p5vykJF9opj8", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())