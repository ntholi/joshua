import random
import time

from win11toast import toast

print("Running Confessions...")
lines = [
    line.rstrip("\n") for line in open("confessions", encoding="utf8") if line.strip()
]
print("Successfully loaded %d confessions" % len(lines))
icon = "icon.png"
while True:
    time.sleep(10)
    i = random.randint(0, len(lines) - 1)
    body, title = lines[i].split("(")
    title = title.replace(")", "")
    toast(title, body, duration="long")
    print("- {0:s} ({1:s})".format(body, title))
    time.sleep(33)
