def isPalindrome(string):

    if len(string)==0 or len(string)==1:
        return True
    else:
        head = string[0]
        tail = string[-1]
        body = string[1:-1]
        return head == tail and isPalindrome(body)


print(isPalindrome('anitalavalatina'))
