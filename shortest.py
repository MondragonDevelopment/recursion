def shortest(makeRecursiveCall):
    print('shortest(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:  # Base Case
        print('Returning from base case.')
        return
    else:
        shortest(False)
        print('Returning from recursive case.')
        return


print('Calling shortest(False):')
shortest(False)
print('Calling shortest(True):')
shortest(True)
