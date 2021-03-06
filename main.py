from helloworld import say_hello_world
from my_other_dir.greetings import say_hi

def main():
    res1 = say_hello_world()
    res2 = say_hi("Bob")
    
    return res1 + "" + res2

if __name__ == "__main__":
    print(main())
