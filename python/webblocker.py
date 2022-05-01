import time
from time import datetime as dt
sites_to_block=[]  #enter websites url to block
window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

def block_websites(start_hour,end_hour):
    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day,start_hour)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,end_hour):
            print("Do the work...")
            with open(window_host, 'r+') as hostfile:
                hosts=hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect +' '+site+'\n')
        else:
            with open(window_host,'r+') as hostfile:
                hosts= hostfile.readline()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print("Good Time")
        time.sleep(3)


if __name__ == '__main__':
    block_websites(9,18)  #from 9am to 18pm sites will be blocked 