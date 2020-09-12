import http.client
from termcolor import colored
import os

starting_profile = 1
end_profile = 10000000

if not os.path.isfile("existent_profiles.txt"):
    c = open("existent_profiles.txt", "w")
    c.close()

for i in range(starting_profile, end_profile):
    r = http.client.HTTPSConnection("www.roblox.com")
    r.request("HEAD", "/users/{}/profile".format(i))
    r1 = r.getresponse()
    if r1.status == 200:
        print(f"{i}", colored("exists", "green"))
        with open("existent_profiles.txt", "a") as f:
            f.write("{}\n".format(i))
    elif r1.status == 302:
        print(f"{i}", colored("doesn't exist", "red"))