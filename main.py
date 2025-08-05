import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.strategy import FSMStrategy
from aiogram.router import Router
from config import BOT_TOKEN
from otp_checker import save_otp, get_status, set_status

# Logging
logging.basicConfig(level=logging.INFO)

# Create router
router = Router()

# Handle /start command
@router.message(lambda msg: msg.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "<b>👋 Welcome to the OTP Receiver Bot</b>\n\n"
        "Use /status to check status.\n"
        "Send me any OTP and I will save it."
    )

# Handle /status
@router.message(lambda msg: msg.text == "/status")
async def status_handler(message: Message):
    status = get_status()
    await message.answer(f"📡 Bot Status: <b>{status}</b>")

# Handle /online
@router.message(lambda msg: msg.text == "/online")
async def online_handler(message: Message):
    set_status("Online")
    await message.answer("✅ Status changed to <b>Online</b>")

# Handle /offline
@router.message(lambda msg: msg.text == "/offline")
async def offline_handler(message: Message):
    set_status("Offline")
    await message.answer("❌ Status changed to <b>Offline</b>")

# Handle incoming OTPs (text messages)
@router.message()
async def otp_receiver(message: Message):
    text = message.text.strip()
    if text and text.isdigit() and 4 <= len(text) <= 8:
        save_otp(text)
        await message.answer("📩 OTP saved successfully.")
    else:
        await message.answer("❗ Invalid OTP format. Send 4–8 digit code.")

# Main function
async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
