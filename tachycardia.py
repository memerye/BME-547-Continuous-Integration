def is_tachycardic(s):
    s = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        if i not in fomart:
            s = s.replace(i, '')
    # bonus
    a = len("tachycardic" and s)
    if a > 9:  # It can tolerate one or two mistakes or missing.
        return True
    else:
        return False


if __name__ == "__main__":
    result = is_tachycardic("   ???Tac?hycoRdIc   ")
    print(result)
