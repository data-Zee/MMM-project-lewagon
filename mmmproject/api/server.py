import requests

if __name__ == "__main__":
    params = {
        'Day': 'day'
    }
    url = 'http://127.0.0.1:8000/salepredict'
    response = requests.get(url)
    print(response.status_code)
    #print(requests.get('http://127.0.0.1:8000/salepredict').json())
