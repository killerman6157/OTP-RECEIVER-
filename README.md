OTP Receiver Bot

## 🧾 Summary
Wannan bot ɗin na aiogram 3.0+ ne wanda aka tsara domin karɓar OTP (One-Time Password) daga fake or real SMS panels. Bot ɗin yana karɓar OTP sannan ya aika saƙo kai tsaye zuwa Telegram user, group, ko channel.

> **Developer**: Bashir Rabiu 🇳🇬  
> **Telegram**: [@LootFiHunter](https://t.me/LootFiHunter)  
> **GitHub**: [killerman6157](https://github.com/killerman6157)

---

## 📁 File Structure

OTP-RECEIVER-/ │ ├── main.py              👉 Main bot logic (aiogram 3+) ├── config.py            👉 Bot configuration (token, panel names) ├── otp_checker.py       👉 Checks and filters OTPs ├── otp_data.json        👉 Stores received OTPs ├── status.json          👉 Bot status & counters ├── README.md            👉 This guide

---

## 🚀 Features

- ✅ Karɓar OTP via fake panels
- ✅ Send OTP to Telegram (channel or group)
- ✅ Multiple panel support (IMS, SniperSMS, etc.)
- ✅ Logs OTPs with JSON
- ✅ Anti-duplicate filtering
- ✅ Fast response using `async`
- ✅ Works with Python 3.9+

---

## 🔧 Installation

### 1. Termux Setup
```bash
pkg update && pkg upgrade
pkg install python git
pip install -U aiogram

> ⚠️ Idan kana amfani da Termux da Python 3.12, ka downgrade:



pkg uninstall python
pkg install python==3.11

2. Clone or Download Project

git clone https://github.com/killerman6157/OTP-RECEIVER-.git
cd OTP-RECEIVER-

3. Configure config.py

BOT_TOKEN = "your_bot_token_here"
ADMIN_ID = 123456789
PANELS = ["SniperSMS", "IMS", "TrueSMS"]


---

▶️ Run the Bot

python main.py


---

🧪 How it Works

1. Bot receives incoming OTP as message from external system or fake API.


2. otp_checker.py filters duplicate OTPs.


3. Saves valid OTP to otp_data.json.


4. Sends to Telegram user/channel.


5. Logs status to status.json.




---

📌 Future Features

🔜 Real panel API integration

🔐 Admin panel for monitoring

🔄 Live OTP auto-forward

📊 Stats dashboard (using Flask)



---

📞 Contact

Telegram: @LootFiHunter

GitHub: killerman6157


> Made in Kano 🇳🇬 by Bashir Rabiu
