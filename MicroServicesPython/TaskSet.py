import random
from locust import HttpLocust, TaskSet, task

paths = ["/Prod/visits/324?startDate=20171014",
         "/Prod/visits/324",
         "/Prod/visits/320"]


class SimpleLocustTest(TaskSet):

    @task
    def get_something(self):
        index = random.randint(0, len(paths) - 1)
        self.client.get(paths[index])


class LocustTests(HttpLocust):
    task_set = SimpleLocustTest
