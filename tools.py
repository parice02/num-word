num_letters = {
    0: "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize",
    17: "dix-sept",
    18: "dix-huit",
    19: "dix-neuf",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    70: "soixante-dix",
    80: "quatre-vingt",
    90: "quatre-vingt-dix",
    100: "cent",
}


def process_str(_input):
    num_str = ""
    grouped_by_3 = group_by_3(str(_input))
    group_length = len(grouped_by_3)
    p = ["milliard", "million", "mille", ""]

    if group_length == 1:
        p = p[-1:]
    elif group_length == 2:
        p = p[-2:]
    elif group_length == 3:
        p = p[-3:]
    else:
        p = p

    for i, group in enumerate(grouped_by_3):
        space = "" if i == 0 else " "
        num_str += space + get_by_3(group) + " " + p[i]
    #print(p)
    return num_str


def get_int(_input):
    raise NotImplementedError


def group_by_3(_input: str):
    _str = ""
    _list_str = []
    reversed_input = _input[::-1]
    for i, c in enumerate(reversed_input):
        _str += c
        if (i + 1) % 3 == 0 or (i + 1) == len(_input):
            _list_str.append(_str[::-1])
            _str = ""

    r = _list_str[::-1]
    #print("groupage", r)
    return r


def decompose_num(_input: str):
    _input_len = len(_input)
    r = [f"{c}*{10**(_input_len - i - 1)}" for i, c in enumerate(_input)]
    #print("decomposition", r)
    return r


def get_by_3(_input: str):
    _str = ""
    decomposed_num = decompose_num(_input)
    for i, char in enumerate(decomposed_num):
        p, d = char.split("*")
        p, d = int(p), int(d)
        if p == 0:
            continue

        space = "" if i == 0 else " "
        if d == 100:
            if p == 1:
                _str += space + num_letters[d]
            else:
                _str += space + num_letters[p] + " " + num_letters[d]
        elif d == 10:
            if p == 1:
                s = decomposed_num[i + 1].split("*")[0]
                c = int(f"{p}{s}")
                _str += space + num_letters[c]
                break
            else:
                _str += space + num_letters[p * d]
        elif d == 1:
            if p == 1:
                et = space + "et " if i != 0 else space
                _str += et + num_letters[p]
            else:
                _str += space + num_letters[p]
    #print("str of group:", _str)
    return _str


def get_str(_input):
    try:
        int(_input)
        if len(str(_input)).__gt__(12):
            raise ValueError("Too much digit")
        return process_str(_input)
    except Exception:
        raise Exception
