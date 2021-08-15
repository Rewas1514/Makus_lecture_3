dict_1 = {
    'один': 'one',
    'два' : 'two',
    'три' : 'three',
    'четыре' : 'four',
    'пять' : 'five',
    'шесть' : 'six',
    'семь': 'seven',
    'восемь' : 'eight',
    'девять' : 'nine',
    'десять' : 'ten'

}

def translator():
    word = input('Введите словом от 1 до 10: ')
    print(dict_1.get(word))

translator()