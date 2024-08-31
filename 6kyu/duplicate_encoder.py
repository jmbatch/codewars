def duplicate_encode(word):
    word = word.lower()
    word_set = set(word)
    dups = set()

    for char in word:
        if char in word_set:
            word_set.remove(char)
        else:
            dups.add(char)

    return "".join(")" if char in dups else "("
                   for char in word)
