import time
from datetime import datetime as dt


win_path = r"C:\Windows\System32\drivers\etc\hosts"
# win_path = "hosts"
lin_path = "/etc/hosts"
redirect = "127.0.0.1"
webiste_list = ["www.facebook.com", "facebook.com"]

while True:
    print("hey")
    if 8 < dt.now().hour <= 12:
        with open(win_path, 'r+') as f:
            content = f.read()
            for website in webiste_list:
                if website not in content:
                    f.write(f"{redirect} {website}\n")
    else:
        with open(win_path, 'r+') as f:
            content = f.readlines()  # read lines into list
            f.seek(0)  # go to beginning of file
            for line in content:
                if not any(w in line for w in webiste_list):
                    f.write(line)  # write lines w/o websites (start @ 0 -> we build the file again from the top)
            f.truncate()  # drop all the lines below where we finished writing
    time.sleep(5)
