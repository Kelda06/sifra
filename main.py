ori_text = input("Zadej text k zašifrování: ")
am_sh = int(input("Zadej posun: "))


abc = ["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t","u", "v", "w", "x","y", "z"]


def cipher(ori_text):
    n_text = ""

    for letter in ori_text:
        if letter.islower():
            n_text += abc[check_index(letter)]
        elif letter.isupper():
            n_text += abc[check_index(letter)].upper()
        else:
            n_text += letter
    return n_text


def check_index(letter):
    original_index = abc.index(letter.lower())

    if (original_index + am_sh > len(abc)):
        return (original_index + am_sh) % len(abc)
    else:
        return original_index + am_sh

def main():
    print(cipher(ori_text))

if __name__ == "__main__":
    main()
