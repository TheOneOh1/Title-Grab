#!/usr/bin/python3
import requests, argparse, re

parser = argparse.ArgumentParser(description="This is a Title Grabbing Tol")

parser.add_argument("-url", type=str, help="Enter Complete URL", required=True)

a = parser.parse_args()

print("Finding Title for : "+a.url)

if "https" in a.url or "http" in a.url:
        data1 = requests.get(a.url,timeout=10)
        
        for i in data1:
                collect = re.findall(r"<title>(.*?)</title>",i.decode('utf-8'))
                if collect:
                        print("Title Found : ",collect)

else:
        print("Error : Wrong Input, Look for -h or --help")
