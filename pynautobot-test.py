import pynautobot
import urllib3
import json
import os
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get URL and token from environment variables
nautobot_url = os.getenv("NAUTOBOT_URL")
nautobot_token = os.getenv("NAUTOBOT_TOKEN")

nautobot = pynautobot.api(
    url=nautobot_url,
    token=nautobot_token,
    verify=False,    
)
# Get all devices
devices = nautobot.dcim.devices.all()
# Print the name of each device
for device in devices:
    print(device.name)

# Get all locations
locations = nautobot.dcim.locations.all()
# Print the name of each location
for location in locations:
    print(location.name)

# GraphQL query to get all devices with their location
query = """query {
    devices {
        id
    }
}
"""
# Execute the query
response = nautobot.graphql.query(query=query)
# Print the response
pprint(response.json)