import math
import sys
from os import rename

import requests

# print(sys.version)
# print(sys.executable)


def greet(who):
    test = "test"
    greeting = "Hello,{}".format(who)
    return greeting


# print(greet('World'))
# print(greet('Corey'))
r = requests.get("https://coreyms.com")
print(r.status_code)
