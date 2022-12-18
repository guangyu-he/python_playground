if __name__ == "__main__":
    symbols = "!§$%&/"
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

    codes = [ord(symbol) for symbol in symbols]
    print(codes)

    codes = [last := ord(c) for c in symbols]
    print(last)
