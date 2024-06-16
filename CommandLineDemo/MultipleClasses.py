from locust import HttpUser, task, constant, TaskSet


class FirefoxBrowserTest(TaskSet):

    @task
    def launch(self):
        print("Firefox Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class ChromeBrowserTest(TaskSet):

    @task
    def launch(self):
        print("Chrome Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class EdgeBrowserTest(TaskSet):

    @task
    def launch(self):
        print("Edge Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):

    wait_time = constant(1)
    tasks = [ChromeBrowserTest, FirefoxBrowserTest, EdgeBrowserTest]

# locust -f .\CommandLineDemo\SimpleTest.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com -L CRITICAL --logfile mylog.log --html Run1

# DEBUG/INFO/WARNING/ERROR/CRITICAL

# List all the User Classes
# locust -f .\CommandLineDemo\SimpleTest.py -l

# Print the task execution ratio
# locust -f .\CommandLineDemo\SimpleTest.py --show-task-ratio
# locust -f .\CommandLineDemo\SimpleTest.py --show-task-ratio-json
