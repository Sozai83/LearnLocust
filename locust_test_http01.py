import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://newtours.demoaut.com"

    @task
    def launch_URL(self):
        self.client.get('/mercurycruise.psp', name = "viewcruise")