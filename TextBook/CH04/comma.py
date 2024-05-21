def insert_comma(my_list):
    if not my_list:
        return 'リストに何も入っていません。'

    if len(my_list) == 1:
        return str(my_list[0])

    result = ''.join(str(item) + ', ' for item in my_list[:-1])
    result += 'and ' + str(my_list[-1])
    return result


spam = ['apples', 'bananas', 'tofu', 'cats']
print(insert_comma(spam))