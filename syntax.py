#!/usr/bin/env python3

print("--- Variables and Basic Data Types ---")

server_name = "Webserver01"
message = "Deployment Successfull."
multilinestring = """This is
multiline
string"""


print(f"Server name: {server_name}")
print(f"Status {message}")
print(multilinestring)
print(f"Type of server name: {type(server_name)}")

#Integers
num_servers = 5
error_code = -1
print(f"\nNumber of servers: {num_servers}")
print(f"Type of num_servers: {type(num_servers)}")

#Floating Point
load = 0.75
pi_value = 3.14159
print(f"Current CPU load: {load}")
print(f"pi_value: {pi_value}")


#Boolen
is_active = True
needRestart = False
print(f"\nService Active: {is_active}")
print(f"Type of is_Active: {is_active}")

#List
ip_addresses = ["192.168.1.10", "10.1.1.5", "172.16.30.100"]
ports = [80, 443,22]
mixed_list = ["config.yaml", 100, True]

print(f"IP adddresses: {ip_addresses}")
print(f"First IP: {ip_addresses[0]}")

print(f"\nOpen Ports:{ports}")
ports.append(8080)
print(f"Ports after append: {ports}")
print(f"Type of ip_addresses; {type(ip_addresses)}")

#Dictionaries
#Unordered Collection of key-pair values

server_config= {
"hostname": "localhost",
"ip": "192.168.1.4",
"port": "8080",
"is_Master":True
}

print(f"Server COnfig: {server_config}")
print(f"Serve Config IP{server_config['ip']}")

#Add a new key-pair value
server_config["os"] = "Ubuntu 22.04"
print(f"Server Config after OS add: {server_config}")


#NoneType
#Represents the absence of a value
result = None
print(f"\nInitial Result: {result}")
print(f"Type of result: {type(result)}")
