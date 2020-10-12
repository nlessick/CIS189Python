def make_list():
    """function will ask the user until the counter reaches 3
       it will call the get_input function where the user enters
       their values and returns it back to the make_list function
       and then finally the list will be printed"""
    count = 3
    list = []
    while count > 0:
        print("Please enter an item you want in the list. ")
        list.append(get_input())
        count -= 1
    print(list)


def get_input():
    user_input = input()
    return user_input

if __name__ == '__main__':
    make_list()

