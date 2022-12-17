def get_input():
    """
    This function ensures that a user correctly enters in a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        number = input("Enter a number between 1-10: ")
        if int(number) >= 1 and int(number) <= 10:
            return number






def main():
    print(get_input())



if __name__ == '__main__':
    main()
