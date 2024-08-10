from locust import User,SequentialTaskSet, task,between, events




class MyWebUser(User):
    wait_time=between(1,2)
    #This will run the tasks randomuly
    #tasks = [add_cart, view_product]
    #This will add the task weightage
    #i.e. {taskfunc: weightage, taskfunc2: weightage....}
    @task()
    class UserBehaviour(SequentialTaskSet):
        def on_start(self):
             print("I will login")


        @task()
        def find_flight(self):
                print("I will find flight by entering criteria")    
            
        @task()
        def select_flight(self):
            print("select flight")

        @task()
        def book_flight(self):
            print("book flight")