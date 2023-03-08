def test(func):
    def inner():
        print("Inner function")
        func()
    # return inner
    print("Outer Function")
    return inner

@test
def main():
    print("Main function")

main()