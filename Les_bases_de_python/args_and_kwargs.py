def add1(*args):
    s = sum(args)
    return s
print(add1(1, 2, 3, 4, 5))

def add(*nums):
    # print(nums)
    return sum(nums)
print(add(1, 2, 3, 4, 5))

def record(**data):
    print(data)
record(name = "Diallo", rollno = 85, age = 20)

def get_data(engine, *queries, **properties):
    print(engine, queries, properties)

get_data('mysql', 'python', 'flask', 'sjango', limit = 10, verbose = True)