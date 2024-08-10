from locust import User,task,between, events

def add_cart(userclass):
   print("I am logging into web URL")

def view_product(userclass):
   print("I am logging out web URL")


class MyWebUser(User):
    wait_time=between(1,2)
    #This will run the tasks randomuly
    #tasks = [add_cart, view_product]
    #This will add the task weightage
    #i.e. {taskfunc: weightage, taskfunc2: weightage....}
    tasks = {add_cart: 3, view_product:6}




    