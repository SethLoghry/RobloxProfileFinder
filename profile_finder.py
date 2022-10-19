__author__ = "Gonçalo M."
__copyright__ = "Copyright 2020, DniGamer"
__license__ = "Apache License 2.0"
__version__ = "1.2"
__email__ = "dnigamerofficial@gmail.com"
__status__ = "Production"

import http.client
import os
import sys

starting_profile = 2447931823
end_profile = 2447931823

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\u001b[37m'

if not os.path.isfile("existent_profiles.txt"):
    c = open("existent_profiles.txt", "w")
    c.close()

def main(starting_profile, end_profile):
    print(bcolors.WHITE, "===========================================")
    print(bcolors.WHITE, "Starting Roblox profile finder by DniGamer")
    print(bcolors.WHITE, "===========================================")
    print(bcolors.WHITE, "Starting profile:", starting_profile)
    print(bcolors.WHITE, "End profile:", end_profile)
    print(bcolors.WHITE, "===========================================")
    for i in range(starting_profile, end_profile):
        r = http.client.HTTPSConnection("www.roblox.com")
        r.request("HEAD", "/users/{}/profile".format(i))
        r1 = r.getresponse()
        if r1.status == 200:
            print(bcolors.GREEN, i, "exists")
            with open("existent_profiles.txt", "a") as f:
                f.write("{}\n".format(i))
        elif r1.status == 302:
            print(bcolors.RED, i, "doesn't exist (skipping)")

if __name__ == "__main__":
    try:
        main(starting_profile, end_profile)
    except KeyboardInterrupt:
        print(bcolors.WHITE, "Killed.")
        sys.exit(0)
