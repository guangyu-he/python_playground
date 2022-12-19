if __name__ == "__main__":

    a_message = "abc"

    match a_message:
        case "ab":
            print("ab")
        case "bc":
            print("bc")
        case "abc":
            print("abc")
        case _:
            raise Exception("haha")

