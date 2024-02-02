def reverse(phrase):
    if len(phrase) == 1:
        return phrase
    else:
        head = phrase[0]
        tail = phrase[1:]
        return reverse(tail) + head


print(reverse('A man, a plan, a canal: Panama'))