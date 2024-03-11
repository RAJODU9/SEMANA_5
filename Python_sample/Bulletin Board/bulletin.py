def enter_evaluation():
    while True:
        print("Please enter your rating from 1 to 5")
        point = get_user_input()
        if point <= 5:
            print("Please enter your comment")
            comment = input()
            post = f"Point: {point} Comment: {comment}"
            with open("data.txt", "a") as file_pc:
                file_pc.write(f"{post}\n")
            break
        else:
            print("Please enter a number from 1 to 5")


def check_results():
    print("Results so far")
    with open("data.txt", "r") as read_file:
        print(read_file.read())


def get_user_input():
    while True:
        num = input()
        if num.isdecimal():
            num = int(num)
            if 1 <= num <= 3:
                return num
            else:
                print("Please enter from 1 to 3")
        else:
            print("Please enter from 1 to 3")


def main():
    while True:
        print("Please select the process you want to perform")
        print("1: Enter evaluation points and comments")
        print("2: Check the results so far")
        print("3: End")
        num = get_user_input()

        if num == 1:
            enter_evaluation()
        elif num == 2:
            check_results()
        elif num == 3:
            print("Exit")
            break


if __name__ == "__main__":
    main()
