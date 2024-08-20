def read_file(file_name):
    with open(file_name, 'r') as file:
        items = file.readlines()
        return items


def write_file(file_name, new_item):
    previous_items = read_file(file_name)
    with open(file_name, 'w') as file:
        file.writelines(previous_items)
        file.write(new_item + '\n')


def update_file(file_name, item_list):
    with open(file_name, 'w') as file:
        file.writelines(item_list)
