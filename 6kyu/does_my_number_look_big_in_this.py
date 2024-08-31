def narcissistic( value ):
    sum = 0
    values = str(value)
    digits = len(values)
    for i in values:
        sum = sum + int(i) ** digits
    number = int(value)
    if number == sum:
        return True
    else:
        return False
