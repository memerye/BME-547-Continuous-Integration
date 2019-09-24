def is_tachycardic(s):
    s = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        if i not in fomart:
            s = s.replace(i, '')
    return s == "tachycardic"


if __name__ == "__main__":
    result = is_tachycardic("   ???Tac?hycaRdIc   ")
    print(result)
