def sayThankyou(func):
    def wrapper(name,*args,**kwargs):
        print("Started...")
        func(name)
        print("Thank you..")
    return wrapper

@sayThankyou
def hello(name):
    print("hello",name)

hello("Prabhu")
hello("Preeti")

    
