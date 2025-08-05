import json
import os

OTP_FILE = "data/otp_data.json"
STATUS_FILE = "data/status.json"

def save_otp(otp_text):
    if not os.path.exists(OTP_FILE):
        with open(OTP_FILE, "w") as f:
            json.dump([], f)

    with open(OTP_FILE, "r") as f:
        data = json.load(f)

    data.append({"otp": otp_text})
    
    with open(OTP_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_status(new_status):
    with open(STATUS_FILE, "w") as f:
        json.dump({"status": new_status}, f)

def get_status():
    if not os.path.exists(STATUS_FILE):
        return "Offline"
    
    with open(STATUS_FILE, "r") as f:
        return json.load(f).get("status", "Offline")
