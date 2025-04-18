from nautobot.apps.jobs import Job, register_jobs, JobHookReceiver

class HelloWorldJobHook(JobHookReceiver):
    """
    A simple job that receives a job hook and prints "Hello, World!" to the console.
    """
    class Meta:
        name = "Hello World Job Hook"

    def receive_job_hook(self, change, action, changed_object):
        self.logger.debug(f"Job hook received {change} {action} {changed_object}")

register_jobs(HelloWorldJobHook)