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

#This only runs at the start
    def on_start(self):
       print("I am logging into web URL")

    @task
    def doing_work(self):
       print("I am doing some work on web URL")

# This only runs at the end    
    def on_stop(self):
        print("I am logging out web URL")
    