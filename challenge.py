import json
import sys
from pathlib import Path

def read_prices_file(filename): 
    try:
        with open(filename, 'r') as pricesFile:
            data = json.load(pricesFile)  # Intentar cargar el JSON
    except FileNotFoundError as e:
        raise ValueError(f"El archivo '{filename}' no existe. Error: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"El archivo '{filename}' no contiene un JSON válido. Error: {e}")
    
    return data

def import_prices_from_data(data):
    # Uso un dict para almacenar los precios segun su ticker
    prices = {}
    for d in data:     
        if d['name'] in prices:
            prices[d['name']].append(d)
        else:
            prices[d['name']] = [d]
    return prices
    
def get_last_price(prices, source):
    # De un dict de precios por nombre obtengo el ultimo precio de una fuente
    last_price = prices[0]
    for price in prices:
        if price['source'] == source and last_price['timestamp'] < price['timestamp']:
            last_price = price
    return last_price

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: challenge.py <filename>")
        exit(1)
    
    data = read_prices_file(sys.argv[1])
    
    prices = import_prices_from_data(data)

    for key in prices:
        print(key)

        print(get_last_price(prices[key], 'A'))
        print(get_last_price(prices[key], 'B'))
        print("")