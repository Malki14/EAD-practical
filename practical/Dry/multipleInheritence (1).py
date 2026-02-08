class Father:

    def __init__(self):
        pass

    def fatherProperty(self):
        print("Father's Property ")

class Mother:

    def __init__(self):
        pass

    def motherProperty(self):
        print("Mother's Property ")

class Child(Father, Mother):

    def __init__(self):
        pass

    def Property(self):
        print("Child will inherit following Property ")
        super().fatherProperty()
        super().motherProperty()


akila = Child()
akila.Property()