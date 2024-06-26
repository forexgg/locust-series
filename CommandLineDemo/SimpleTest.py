from locust import HttpUser, task, constant


class MyLoadTest(HttpUser):

    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/")

# locust -f .\CommandLineDemo\SimpleTest.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com
