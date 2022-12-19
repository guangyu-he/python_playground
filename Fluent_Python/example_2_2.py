def a_func(a, b, *rest):
    return a, b, rest


if __name__ == "__main__":
    print(a_func(1, 2, 3, 4, 5))
