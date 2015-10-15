__author__ = 'KoicsD'


def are_the_same(first, second):
    return first == second


def first_true(fun, obj, lst):
    for index in range(len(lst)):
        if fun(obj, lst[index]):
            return index
    return -1


def true_for_any(fun, obj, lst):
    for item in lst:
        if fun(obj, item):
            return True
    return False


def listing(lst, prefix, delimiter, postfix):
    text = prefix
    for i in range(len(lst)):
        if i > 0:
            text += delimiter
        text += lst[i]
    text += postfix
    return text
