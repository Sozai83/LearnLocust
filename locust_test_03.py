from locust import User,task,between

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
    