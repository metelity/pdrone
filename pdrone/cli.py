import os
import sys
import requests
import csv
import sqlite3
from .banner import print_banner

# PDrone api
SERVER_URL = "http://185.252.146.112:3434"
API_KEY = ""

def get_phone_info(phone_number):
    url = f"http://apilayer.net/api/validate?access_key=33619e4e16f6b0e9050611ce09532706&number={phone_number}&format=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def search_on_server(search_term):
    headers = {"X-API-Key": API_KEY}
    try:
        response = requests.post(
            f"{SERVER_URL}/api/search",
            json={"search": search_term},
            headers=headers
        )
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

def print_ip_info(ip_info):
    if "error" in ip_info:
        print(f"Error: {ip_info['error']}")
        return

    if ip_info.get("status") == "fail":
        print(f"Error: {ip_info.get('message', 'Unknown error')}")
        return

    print("\nIP address information:")
    print(f"IP: {ip_info.get('query', 'unknown')}")
    print(f"Country: {ip_info.get('country', 'unknown')}")
    print(f"Country Code: {ip_info.get('countryCode', 'unknown')}")
    print(f"Region: {ip_info.get('regionName', 'unknown')}")
    print(f"City: {ip_info.get('city', 'unknown')}")
    print(f"ZIP: {ip_info.get('zip', 'unknown')}")
    print(f"Latitude: {ip_info.get('lat', 'unknown')}")
    print(f"Longitude: {ip_info.get('lon', 'unknown')}")
    print(f"Timezone: {ip_info.get('timezone', 'unknown')}")
    print(f"ISP: {ip_info.get('isp', 'unknown')}")
    print(f"Organization: {ip_info.get('org', 'unknown')}")
    print(f"AS: {ip_info.get('as', 'unknown')}" + "\n")

def print_search_results(results):
    if "error" in results:
        print(f"Error: {results['error']}")
        return

    if not results.get("results"):
        print("No results found.")
        return

    print("\nSearch results from server database:")
    for idx, row in enumerate(results["results"], 1):
        print(f"\nResult #{idx}:")
        for key, value in row.items():
            print(f"{key.capitalize()}: {value}")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  pdrone -s <phone number>  - Search phone number info")
        print("  pdrone -i <IP address>    - Search IP address info")
        print("  pdrone -d <search term>   - Search in server database")
        return
        
    os.system("clear")
    print_banner()
    
    option = sys.argv[1]
    
    if option == "-s":
        phone_number = sys.argv[2]
        phone_info = get_phone_info(phone_number)
        print_phone_info(phone_info)
    elif option == "-i":
        ip_address = sys.argv[2]
        ip_info = get_ip_info(ip_address)
        print_ip_info(ip_info)
    elif option == "-d":
        search_term = sys.argv[2]
        search_results = search_on_server(search_term)
        print_search_results(search_results)
    else:
        print("Invalid option. Use:")
        print("  -s for phone search")
        print("  -i for IP search")
        print("  -d for server database search")

if __name__ == "__main__":
    main()
