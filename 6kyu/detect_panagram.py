def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s.lower():
            return False
    return True
