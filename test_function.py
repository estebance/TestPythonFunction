from collections import Counter


if __name__ == '__main__':
    # list of strings
    strings_list = []
    # capture the type
    while True:
        input_text = input("Please enter a string.... to finish and return the value please type exit: ")
        if input_text != 'exit':
            strings_list.append(input_text)
        else:
            break
    if len(strings_list) > 0:
        categorized_values = dict(Counter(strings_list))
        for key, value in categorized_values.items():
            if value % 2 != 0:
                print(key + ":" + str(value) + "\n")
