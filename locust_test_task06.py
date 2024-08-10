from locust import User,TaskSet, task,between, events

class MyWebUser(User):
    wait_time=between(1,2)

    #Nested tasks
    # By default, it will pick one taskset class and once it's chosen, it will be stuck there
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
        class Product_Module(TaskSet):
            @task()
            def add_product(self):
                print("Additng products")

            @task()
            def delete_product(self):
                 print("delete product")  