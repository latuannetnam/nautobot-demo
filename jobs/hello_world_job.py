from nautobot.apps.jobs import Job, register_jobs
class HelloWorld(Job):
    """
    A simple job that prints "Hello, World!" to the console.
    """
    def run(self):
        self.logger.debug("Hello, World!")

register_jobs(HelloWorld)        