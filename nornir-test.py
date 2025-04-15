from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def hello_world(task):
    result = Result(
        host=task.host, result=f"{task.host.name} says hello world!")
    # print_result(result)
    return result


def main():
    # Get URL and token from environment variables
    nautobot_url = os.getenv("NAUTOBOT_URL")
    nautobot_token = os.getenv("NAUTOBOT_TOKEN")
    
    book_nornir = InitNornir(
        inventory={
            "plugin": "NautobotInventory",
            "options": {
                "nautobot_url": nautobot_url,
                "nautobot_token": nautobot_token,
                # "filter_parameters": {"location": locations },
                "ssl_verify": False,
            },
        },
    )
    print(f"Hosts found:{len(book_nornir.inventory.hosts)}") 
    print(book_nornir.inventory.hosts.keys())
    result = book_nornir.run(task=hello_world)
    print_result(result)

if __name__ == "__main__":
    main()