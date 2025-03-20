import os
import sys
import requests
from .banner import print_banner

def get_phone_info(phone_number):
    url = f"http://apilayer.net/api/validate?access_key=33619e4e16f6b0e9050611ce09532706&number={phone_number}&format=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def print_phone_info(phone_info):
    if "error" in phone_info:
        print(f"Error: {phone_info['error']}")
        return

    if not phone_info.get("valid"):
        print("Invalid phone number.")
        return

    print("\nPhone number information:")
    print(f"Number: {phone_info.get('international_format', 'unknown')}")
    print(f"Country: {phone_info.get('country_name', 'unknown')}")
    print(f"Region: {phone_info.get('location', 'unknown')}")
    print(f"Carrier: {phone_info.get('carrier', 'unknown')}")
    print(f"Line type: {phone_info.get('line_type', 'unknown')}" + "\n")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "-s":
        print("Usage: pdrone -s <phone number>")
        return

    phone_number = sys.argv[2]
    print_banner()
    phone_info = get_phone_info(phone_number)
    print_phone_info(phone_info)
