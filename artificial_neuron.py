from mpmath import sigmoid


def activate(input, weight):
    h = 0
    for i, w in zip(input, weight):
        h += i*w
    return sigmoid(h)

if __name__ == "__main__":
    input = [.5, .3, .2]
    print(input)
    weight = [.4, .7, .2]
    print(weight)
    output = activate(input, weight)
    print(output)