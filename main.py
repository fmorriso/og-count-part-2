def og_count(text: str):
    n = 0
    locations = []
    search = 'og'
    words = text.lower().split()
    for i, word in enumerate(words):
        # print(f'{i=} {word=}')
        find = word.find(search)
        if find >= 0:
            n += 1
            locations.append(i)

    return (n, locations)


phrase = input('Enter some text: ')
(count, where) = og_count(phrase)
print(f'There were {count} words that contained "og".')
print(f'They occurred at indicies: {where}')
