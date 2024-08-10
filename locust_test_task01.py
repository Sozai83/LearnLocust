from locust import User,task,between, events
#Only run when the test started
@events.test_start.add_listener
def script_start(**kwargs):
    print("I am connecting to DB")

#only runs when the test ended
@events.test_stop.add_listener
def script_end(**kwargs):
    print("I am disconnectiong from DB")


class MyWebUser(User):
    wait_time=between(1,2)


    @task(2)
    def add_cart(self):
       print("I am logging into web URL")

    #Users will view_product more - by passing larger number it determines the weight of the task being chosen
    @task(4)
    def view_product(self):
       print("I am logging out web URL")

    