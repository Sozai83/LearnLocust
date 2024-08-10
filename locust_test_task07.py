from locust import User,TaskSet, task,between, events

class MyWebUser(User):
    wait_time=between(1,2)

    #Nested tasks
    # By default, it will pick one taskset class and once it's chosen, it will be stuck there
    #by using self.interrupt method
    # once the stop task is selected (with self.interrupt is in) it will then select a task randomly
    @task()
    class UserBehaviour(TaskSet):

        @task()
        class CartModule(TaskSet):
            @task()
            def add_cart(self):
                print("Additng items")

            @task()
            def delete_cart(self):
                 print("delete cart")
            
            @task()
            def stop(self):
                print("I am stopping")
                self.interrupt()

        @task()
        class Product_Module(TaskSet):
            @task()
            def add_product(self):
                print("Additng products")

            @task()
            def delete_product(self):
                 print("delete product")

            @task()
            def stop(self):
                print("I am stopping")
                self.interrupt()
