
def multiply_and_greet(*args,**kwargs):
    multiple=1
    for number in args:
        multiple *=number
    print(multiple)
    keys=kwargs.keys()
    if "country" in keys:
        print(f"Hello {kwargs['name']} from {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif "name" in keys:
        print(f"Hello {kwargs['name']}")
    else:
        print (f"Hello Anonymous")
    