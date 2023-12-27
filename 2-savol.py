import threading


def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@printer
def calculyator(number):
    return str(number)[::-1]


def main():
    numbers = input("sonlarni probel bilan kiriting: ").split()

    v = []
    for number in numbers:
        a = threading.Thread(target=calculyator, args=(int(number),))
        v.append(a)
        a.start()

    for a in v:
        a.join()


if __name__ == "__main__":
    main()
