import notify2
import time
import random

print("Running Confessions...");
lines = [line.rstrip('\n') for line in open('confessions') if line.strip()]
print("Successfully loaded %d confessions" %len(lines));
icon = "icon.png"
notify2.init("Confessions")
while True:
	time.sleep(10); #wait 10 seconds
	i = random.randint(0, len(lines)-1)
	body, title = lines[i].split('(');
	title = title.replace(")", "")
	notify2.Notification(title, body, icon).show()
	print("- {0:s} ({1:s})".format(body,title)); 
	time.sleep(33 * 60); #wait 33 minutes