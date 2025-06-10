def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(path):
    value = {}

    with open(path) as e:

        counting = e.read()

        for i in counting:
            
            if i.lower() in value:
                value[i.lower()] += 1
            else:
                value.update({i.lower() : 1})
        return value

def sort_it(check):
    new_list = []

    for key, value in check.items():
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = value
        new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(d):
    return d["num"]