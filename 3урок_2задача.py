def thesaurus(*names): # * позволяет вводить несколько значений
    dict_name = dict()
    for name in names:
        dict_name.setdefault(name[0],[]) # setdefault если в словаре нету ключа создаст новый ключ 
        dict_name[name[0]].append(name)
    return(dict_name)

print(thesaurus('Виталий', 'Сшаа'))