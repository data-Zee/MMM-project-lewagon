import requests

if __name__ == "__main__":
    params = {
        'fb_cost': 1000.00,
        'google_cost': 800.00,
        'tt_cost': 500.00,
        'variable_1': 0,
        'variable_2': 1
    }
    print(requests.get('http://127.0.0.1:8000/salepredict', params=params).json())
