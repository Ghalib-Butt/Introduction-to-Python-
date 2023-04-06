class MyClass:
    def my_method(self):
        print("Original method")

def monkey_patch(self):
    print("Patched method")

obj = MyClass()
obj.my_method()  # Output: Original method

MyClass.my_method = monkey_patch  # Monkeypatching the method

obj.my_method()