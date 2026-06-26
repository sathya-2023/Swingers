import upstox_client
from upstox_client.rest import ApiException

from config import UPSTOX_ACCESS_TOKEN

configuration = upstox_client.Configuration()

configuration.access_token = UPSTOX_ACCESS_TOKEN

client = upstox_client.ApiClient(configuration)

user_api = upstox_client.UserApi(client)

try:
    response = user_api.get_profile("2.0")
    print(response)

except ApiException as e:
    print(e)