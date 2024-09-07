def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    return
print_params()
print_params(2,"fff",False)
print_params(1,25)
print_params(1,2,[1,2,3])

values_list = [1,"F",True]
values_dict = {"a": 1,"b": "F", "c": False}
print(" ")
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, "g"]
print_params(*values_list_2, 42)