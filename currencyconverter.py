import requests
import time


def convert(amount, curr1, curr2):
    url = f"https://api.frankfurter.app/latest?from={curr1}&to={curr2}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][curr2]
    return amount* rate

def get_rate(curr1,curr2):
    url = f"https://api.frankfurter.app/latest?from={curr1}&to={curr2}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][curr2]
    return rate


def main():
    while True:
        time.sleep(1)
        file_path = r'request-file\currency-request.txt'
        f = open(file_path, 'r')
        data = f.read().strip()
        f.close()
        if  len(data) == 0:
            continue
        
        inputs = data.split()

        if inputs[0].lower() == "current":
            f = open(file_path, 'w')
            f.write(get_rate(inputs[1], inputs[2]))
            f.close

        
        if inputs[0].lower() == "convert":
            f = open(file_path, 'w')
            f.write(convert(inputs[1], inputs[2], inputs[3]))
            f.close





