import requests

if __name__ == "__main__":
    params = {
        'Day': 'day'
    }
    url = 'http://127.0.0.1:8000/salepredict'
    response = requests.get(url)
    print(response.status_code)
    #print(requests.get('http://127.0.0.1:8000/salepredict').json())

    url = 'http://localhost:8000/budgetdivider'

    params = {
    'TOTAL_DAILY_BUDGET':1000, 'Date':'2023-09-06'
    }
    response = requests.get(url, params=params)
    print (response.json())
    print(response.status_code)
