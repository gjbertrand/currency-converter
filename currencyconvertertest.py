import time

file_path = r'currency-converter\request-file\currency-request.txt'

def write_to_file(text):
    f = open(file_path, 'w')
    f.write(text)
    f.close

def read_file():
    f = open(file_path, 'r')
    data = f.read().strip()
    f.close()
    return data


def main():

    print("Type 'rate' to see the conversion rate from one currency to another")
    print("Type 'convert' to convert an amount in a currency from one to another")
    command = input("Enter the command: ")

    if command.lower().strip() == 'rate':
        currency1 = input("Enter in the first currency: ")
        currency2 = input("Enter in the second currency: ")
        final_string = 'rate' + ' ' + currency1 + " " + currency2
        time.sleep(5)
        write_to_file(final_string)
        print(read_file())
        

        

    elif command.lower().strip() == 'convert':
        amount = input("Enter in the amount")
        currency1 = input("Enter in the first currency: ")
        currency2 = input("Enter in the second currency: ")
        final_string = 'convert' + ' ' + amount + ' ' + currency1 + " " + currency2
        write_to_file(final_string)
        time.sleep(5)
        print(read_file())
main()