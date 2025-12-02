import requests
import time


def convert(amount, curr1, curr2):
    try:
        url = f"https://api.frankfurter.app/latest?from={curr1}&to={curr2}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][curr2]
        total = amount* rate
        return str(total)
    except:
        return 'Error: Could not make conversion'

def get_rate(curr1,curr2):
    try:
        url = f"https://api.frankfurter.app/latest?from={curr1}&to={curr2}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][curr2]
        return str(rate)
    except:
        return 'Error: Could retrieve rate'



def main():
    while True:
        time.sleep(1)
        file_path = r'currency-converter\request-file\currency-request.txt'
        f = open(file_path, 'r')
        data = f.read().strip()
        f.close()
        if  len(data) == 0:
            continue
        
        inputs = data.split()

        if inputs[0].lower() == "rate":
            print("Received current command with the inputs " + inputs[1], inputs[2])
            f = open(file_path, 'w')
            content = get_rate(inputs[1], inputs[2])
            f.write(content)
            print("Sent " + content)
            f.close()

        
        if inputs[0].lower() == "convert":
            print("Received convert command with the inputs ")
            f = open(file_path, 'w')
            content = convert(inputs[1], inputs[2], inputs[3])
            f.write(content)
            print("Sent " + content)
            f.close()


main()


