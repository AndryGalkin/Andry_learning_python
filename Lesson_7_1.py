import os

dir_list = {'my_project': [{'settings':[]}, {'mainapp':[]}, {'adminapp':[]}, {'authapp':[]}]}

for key, value in dir_list.items():
    if not os.path.exists(key):
        os.mkdir(os.path.join(key))
        for item in value:
            for k in item.keys():
                print(key, k)
                os.mkdir(os.path.join(key, k))


