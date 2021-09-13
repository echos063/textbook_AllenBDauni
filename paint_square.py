# def right_justify(s):
#     a = (' ' * (70 - len(s))) + s
#     print(a)
#     print(len(a))
#
#
# right_justify('abrakadabra')

# def do_twice(func, arg):
#     func(arg)
#     func(arg)
#
#
# def print_twice(arg):
#     print(arg)
#     print(arg)
#
#
# def do_four(func, arg):
#     do_twice(func, arg)
#     do_twice(func, arg)
#
#
# do_twice(print, 'Spam')
# print('\n')
# do_four(print, 'Spam')

def once(a, b):
    print(a, b * 11, a, b * 11, a)


def twice(a, b):
    once(a, b)
    once(a, b)


def four(a, b):
    twice(a, b)
    twice(a, b)


def full(a, b, c, d):
    once(a, b)
    four(c, d)
    once(a, b)
    four(c, d)
    once(a, b)


def more(a, b):
    print(a, b * 11, a, b * 11, a, b * 11, a, b * 11, a)


def more_twice(a, b):
    more(a, b)
    more(a, b)


def more_four(a, b):
    more_twice(a, b)
    more_twice(a, b)


def more_full(a, b, c, d):
    more(a, b)
    more_four(c, d)
    more(a, b)
    more_four(c, d)
    more(a, b)


full('+', '-', '|', " ")
print('\n')
more_full('+', '-', '|', " ")
