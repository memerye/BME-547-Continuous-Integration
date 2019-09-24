def is_tachycardic(s):
    s = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        if i not in fomart:
            s = s.replace(i, '')
    t = "tachycardic           "  # 11 blank space padding
    s = s + "           "         # 11 blank space padding
    if t in s:
        return True
    else:
        # bonus
        i = 0
        j = 0
        flag = 0
        while i < 11 and j < 11:
            if s[i] != t[j]:
                flag = flag + 1
                if s[i] == t[j+1]:  # miss one letter
                    j = j + 1
                elif s[i] == t[j+2]:
                    j = j + 2       # miss two letter
                    flag = flag + 1
                elif s[i+1] == t[j]:
                    i = i + 1       # insert one letter
                elif s[i+2] == t[j]:
                    i = i + 2       # insert two letter
                    flag = flag + 1
            if flag > 2:
                return False
            else:
                i = i + 1
                j = j + 1
        return True


if __name__ == "__main__":
    result = is_tachycardic("ooooops tachycardic")
    print(result)
