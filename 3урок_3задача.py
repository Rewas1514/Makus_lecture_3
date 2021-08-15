import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    jokes_list = []
    for i in range(num):
        nouns_word = random.choice(nouns)
        adverbs_word = random.choice(adverbs)
        adjectives_word = random.choice(adjectives)
        jokes_list.append(f'{nouns_word},{adjectives_word},{adverbs_word}')
    return jokes_list

print(get_jokes(3))