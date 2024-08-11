from locust import HttpUser, task, between, SequentialTaskSet

#Created a separate user behaviour and run the tasks sequentially
@task()
class UserBehaviour(SequentialTaskSet):
    @task
    def launch_URL(self):
        resp1 = self.client.get('/mercurycruise.psp', name = "launch")
        print(resp1.text)
        print(resp1.status_code)
        print(resp1.headers)
    
    @task
    def login(self):
        login_data = {"action": "process", 
                      "userName":"quamile1@gmail.clom", 
                      "password": "qamile", 
                      "login.x": "41", 
                      "login.y":"12"}
        
        resp2 = self.client.post('/login.psp', name = "login", data=login_data)
        print(resp2.text)
        print(resp2.status_code)
        print(resp2.headers)
    
    

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://newtours.demoaut.com"

    task = [UserBehaviour]