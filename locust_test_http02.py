from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://newtours.demoaut.com"

    @task
    def launch_URL(self):
        self.client.get('/mercurycruise.psp', name = "launch")
    
    @task
    def login(self):
        login_data = {"action": "process", 
                      "userName":"quamile1@gmail.clom", 
                      "password": "qamile", 
                      "login.x": "41", 
                      "login.y":"12"}
        
        self.client.post('/login.psp', name = "login", data=login_data)
