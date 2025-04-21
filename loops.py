#!/usr/bin/env python

print("---Loops---")

servers = ["Web-01", "db-02", "Web-03", "app-01"]
ports = [22,80,33]


print("\nChecking Servers:")
for server in servers:
    print(f"Pinging...{server}")

#Loop through list items and range

for i in range(len(ports)):
    port = ports[i]
    print(f"Checking port: {port} (Index {i}) on Web-01")

print("\nServer Configuration")

server_config = {"hostname": "db-server-01", "ip": "192.168.1.23", "port":"3323"}
for key, value in server_config.items():
   print(f"{key}: {value}")


print("\n---While Loops---")
count = 0
max_tries = 3
service_ready = False

while not service_ready and count<max_tries:
   print(f"Checking service status (Attempts {count + 1})...")
   if count == 1:
     print("Service is now ready!.")
     service_ready = True
   else:
     print(" Service is not ready yet. ")
   count +=1

if service_ready:
    print("Proceeding with deployment.")
else:
    print(f"Service failed to start after {max_retries} attempts.")


print("\n--- Done ---")
