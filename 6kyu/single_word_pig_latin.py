def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = list(s)

    if(s.isalpha()):
        if string[0].lower() not in vowels:
            cat = ''.join(string[1:])
            dog = string[0].lower()
            for i in range(len(s)):
                if string[i].lower() in vowels:
                    dog = ''.join(string[:i:])
                    cat = ''.join(string[i:])
                    break
            return cat.lower() + dog.lower() + 'ay'
        else:
            return s.lower() + 'way'
    else:
        return None
