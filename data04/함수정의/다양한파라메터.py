

def list_p(x):
    for index in range(len(x)):
        print(index, x[index])

def set_p(x):
    for data in x:
        print(data)

def dic_p(x):
    for data in x.values():
        print('값',data)
    print('---------------------')
    print(x)
    for key in x:
        print('키', key, ':', '값', x[key])

def tuple_p(x):
    for data in x:
        print(data)
