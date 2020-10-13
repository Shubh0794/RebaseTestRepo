def run_decorator_script(func):
    """
    Just creating a sample decorator function for testing out VS Code environment setup for Python. 
    """
    def wrapper():
        print("  START  ".center(80,"-"))
        func()
        print("   END   ".center(80,"-"))
    return wrapper


@run_decorator_script
def hello_world():
    print ("\nHELLO WORLD!\n")

hello_world()



# name = "Mojo Jojo"
# print(f"My name is {name}")






