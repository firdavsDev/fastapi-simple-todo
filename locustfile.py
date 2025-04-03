"""
Test the performance of a web application using Locust.
"""

from locust import HttpUser, between, task


class TodoUser(HttpUser):
    wait_time = between(0.01, 0.1)  # Oraliqni sozlash

    @task
    def get_todos(self):
        self.client.get("/todos/")

    @task
    def create_todo(self):
        self.client.post(
            "/todos/", json={"title": "Test Task", "description": "Test description"}
        )


# run: locust -f locustfile.py --host=http://127.0.0.1:8000
# open: http://localhost:8089
