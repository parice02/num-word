from tools import get_str


def main(_input):
    try:
        _input = int(_input)
        return get_str(_input)
    except:
        raise TypeError
