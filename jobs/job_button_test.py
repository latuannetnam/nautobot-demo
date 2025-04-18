from nautobot.apps.jobs import Job, register_jobs, JobButtonReceiver
name  ="Job Button Test"
class HelloWorldJobButton(JobButtonReceiver):
    """
    A simple job that add Button to nautobot.
    """
    class Meta:
        name = "Hello World Job Button"
        
    def receive_job_button(self, obj):
        self.logger.debug("Job button received", extra={"object": obj})
        self.logger.debug("Job Button name", extra={"object": obj.name})

register_jobs(HelloWorldJobButton)
