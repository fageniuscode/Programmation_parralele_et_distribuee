"""assert <condition>, <optional-message>"""

def get_age(age):
    assert age > 0, "Age can't be negative!"
    print("Ok your age is : ", age)
get_age(-1)