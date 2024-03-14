def reverse(string):

    if len(string)==0:
        return ''
    else:
        head = string[0]
        tail = string[1:]
        return reverse(tail) + head


a = 'I need some water'
print(reverse(a))
