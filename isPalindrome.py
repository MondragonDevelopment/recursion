def isPalindrome(phrase):
    if len(phrase) == 0 | len(phrase) == 1:
        return True
    else:
        head = phrase[0]
        tail = phrase[-1]
        return head == tail and isPalindrome(phrase[1:-1])


print(isPalindrome('anitalavalatina'))
print(isPalindrome('trample'))
