from time import time
from collections import defaultdict
from typing import Union

USERS = defaultdict(list)
MESSAGES = 3
SECONDS = 3


def is_flood(uid: int) -> Union[bool, None]:
    """Checks if a user is flooding"""

    USERS[uid].append(time())
    if len(list(filter(lambda x: time() - int(x) < SECONDS, USERS[uid]))) > MESSAGES:
        return True


if __name__ == "__main__":
    while 1:
        try:
            input(">>> ")
        except (EOFError, KeyboardInterrupt):
            break
        if is_flood(12345678):
            print("flood")
        else:
           print("not flood")
    print()
