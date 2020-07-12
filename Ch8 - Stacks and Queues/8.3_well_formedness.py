
d = {'(':')', '[':']', '{':'}'}

# ( ] [ )

def check(str1):
    s = []
    s.append(str1[0])

    for i in range(1, len(str1)):
        # for unmatched closing brackets
        try:
            d[s[-1]]
        except KeyError:
            return False

        if(str1[i] == d[s[-1]]):
            s.pop()
        else:
            s.append(str1[i])

    if len(s) == 0:
        return True
    else:
        return False


str1 = input()
print(check(str1))
