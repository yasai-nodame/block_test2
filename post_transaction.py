import requests
import json
import datetime

def main():
    time = datetime.datetime.now().isoformat()

    transaction = {
        "time": time,
        "sender": "A-san",
        "receiver": "B-san",
        "amount": 111,
        "description": "YYY Project Expenses",
        "signature": "signature_sample"
    }

    url = "https://block-test10.onrender.com/transaction_pool/" 
    res = requests.post(url, json.dumps(transaction))
    print(res.json())

if __name__ == "__main__":
    main()