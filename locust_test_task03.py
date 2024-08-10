from locust import User,taskSet, task,between, events


class UserBehaviour(TaskSet):
   @task()
   def add_cart(self):
        print("I am logging into web URL")
   @task()
   def view_product(self):
       print("I am logging out web URL")


class MyWebUser(User):
    wait_time=between(1,2)
    #This will run the tasks randomuly
    #tasks = [add_cart, view_product]
    #This will add the task weightage
    #i.e. {taskfunc: weightage, taskfunc2: weightage....}
    tasks = [UserBehaviour]



