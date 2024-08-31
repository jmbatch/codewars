def identity(integer: int) -> int:
    return integer

def zero(f=identity):
    return f(0)

def one(f=identity):
    return f(1)

def two(f=identity):
    return f(2)

def three(f=identity):
    return f(3)

def four(f=identity):
    return f(4)

def five(f=identity):
    return f(5)

def six(f=identity):
    return f(6)

def seven(f=identity):
    return f(7)

def eight(f=identity):
    return f(8)

def nine(f=identity):
    return f(9)

def plus(right: int):
    return lambda left: left + right

def minus(right: int):
    return lambda left: left - right

def times(right: int):
    return lambda left: left * right

def divided_by(right):
    return lambda left: left // right
