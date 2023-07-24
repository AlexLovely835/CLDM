import math

def currency_string(value_in_copper):
    gold = str(math.floor(value_in_copper / 100))
    silver = str(math.floor(value_in_copper / 10) % 10)
    copper = str(value_in_copper % 10)
    
    if gold == '0':
        gold_string = ''
    else:
        gold_string = gold + ' GP '
    if silver == '0':
        silver_string = ''
    else:
        silver_string = silver + ' SP '
    if copper == '0':
        copper_string = ''
    else:
        copper_string = copper + ' CP '
    return f'{gold_string}{silver_string}{copper_string}'.strip()

if __name__ == '__main__':
    choice = input('Copper value: ')
    print(currency_string(int(choice)))