import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN, GROUP_ID, ADMIN_ID, USE_FAKE_API, CHANNEL_LINK, CHANNEL_NAME
from otp_checker import save_otp, get_status, set_status, get_otp_count, get_last_otps
from fake_api import get_fake_otp

# Logging
logging.basicConfig(level=logging.INFO)

# Bot and Dispatcher
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Only admin allowed
async def check_admin(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Access Denied.")
        return False
    return True

# Format OTP message
def format_otp_msg(otp_data):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = (
        f"🔥 Telegram {otp_data['country']} RECEIVED! ✨\n\n"
        f"⏰ Time: {time}\n"
        f"🌍 Country: {otp_data['country']}\n"
        f"⚙️ Service: {otp_data['service']}\n"
        f"☎️ Number: {otp_data['number']}\n"
        f"🔑 OTP: <code>{otp_data['otp']}</code>\n"
        f"📩 Full Message: \n{otp_data['message']}"
    )
    return msg

# Channel button
def get_channel_button():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text=CHANNEL_NAME, url=CHANNEL_LINK)]
    ])

# /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not await check_admin(message): return
    await message.answer("🤖 OTP Bot started.\nNow forwarding OTPs...")

# /on
@dp.message(Command("on"))
async def cmd_on(message: types.Message):
    if not await check_admin(message): return
    set_status("Online")
    await message.answer("✅ Bot is <b>Online</b> now.")

# /off
@dp.message(Command("off"))
async def cmd_off(message: types.Message):
    if not await check_admin(message): return
    set_status("Offline")
    await message.answer("🚫 Bot is <b>Offline</b> now.")

# /status
@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    if not await check_admin(message): return
    count = get_otp_count()
    status = get_status()
    await message.answer(f"📡 Bot Status: {status}\n📥 OTPs saved: {count}")

# /check
@dp.message(Command("check"))
async def cmd_check(message: types.Message):
    if not await check_admin(message): return
    otps = get_last_otps()
    if not otps:
        await message.answer("📭 No OTPs found.")
        return
    out = "\n\n".join([f"🔑 <code>{o['otp']}</code> | {o['number']} ({o['country']})" for o in otps])
    await message.answer(f"<b>Last OTPs:</b>\n\n{out}")

# /admin
@dp.message(Command("admin"))
async def cmd_admin(message: types.Message):
    if not await check_admin(message): return
    await message.answer(
        "<b>🔐 Admin Panel</b>\n"
        "/on – Enable forwarding\n"
        "/off – Pause forwarding\n"
        "/status – Bot status\n"
        "/check – Last OTPs"
    )

# Background OTP fetcher
async def otp_fetcher():
    while True:
        if get_status() != "Online":
            await asyncio.sleep(5)
            continue

        otp_data = get_fake_otp()
        if otp_data:
            save_otp(otp_data)
            msg = format_otp_msg(otp_data)
            await bot.send_message(GROUP_ID, msg, reply_markup=get_channel_button())

        await asyncio.sleep(10)

# Run bot
async def main():
    asyncio.create_task(otp_fetcher())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
