# data_engineering_challenge_application

# function splits turns the input into a list
def split(word):
    return [char for char in word]

# function rejoins list into a string
def listToString(s):
    strl = ""
    return(strl.join(s))

# function evaluates inputs and outputs sorted numbers
def evaluate_input():
    # if user_input.lstrip('-').replace('.', '', 1).isdigit():
    if user_input.isdigit():
        # splits input into a list
        num_list = split(user_input)
        # test whether or not the list is sorted
        flag = 0
        test_list = num_list[:]
        test_list.sort(reverse=True)
        if (test_list == num_list):
            flag = 1
        # if list sorted, print "-1"
        if (flag):
            print("-1")
        # else print num_list sorted in descending order
        else:
            num_list.sort(reverse=True)
            print(listToString(num_list))
    else:
        # if statement to deal with negative numbers
        if user_input.lstrip('-').replace('.', '', 1).isdigit():
            num_list = split(user_input)
            flag = 0
            test_list = num_list[:]
            test_list.sort()
            if (test_list == num_list):
                flag = 1
            # if list sorted, print "-1"
            if (flag):
                print("-1")
            # else print num_list sorted in ascending order
            else:
                num_list.sort()
                print(listToString(num_list))
        else:
            print("Please Enter in Digits")

# run function evaluate_input()
user_input = input('Enter an input: ')
evaluate_input()
