def get_count(sentence):
    total = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = [x for x in sentence]
    for char in vowels:
        count = sentence.count(char)
        total = total + count
    return total
