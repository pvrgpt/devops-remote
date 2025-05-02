#!/usr/bin/env python3
import subprocess
import sys
import time

def check_service_status(service_name):
    print(f"Checking Status for '{service_name}'...")
    try:
       result = subprocess.run(["systemctl", "is-active","--quiet", service_name], capture_output=True, text=True)
       return result.returncode == 0
    except FileNotFoundError:
       print("Error: 'systemctl' command not found. Is systemd installed?")
       return None
    except Exception as e:
       print(f"An unexpected error occurred {e}")
def start_services(service_name):
    print(f"Attempting to start service '{service_name}'...(requires sudo)")
    try:
       result = subprocess.run(["sudo","systemctl","start", service_name], capture_output=True, check=True, text=True)
       print(f"Start command for '{service_name}' executed sucessfully.")
       return True
    except FileNotFoundError:
       print("Error: 'sudo' or 'systemctl' command not found.")
       return None
    except subprocess.CalledProcessError as e:
       print(f"Error executing start command for '{service_name}' (Exit code '{e.returncode}').")
       print(f"Stderr:{e.stderr.strip()}")
       print("Possible reasons: Incorrect service name, permissions issue, service mask")
       return False
    except Exception as e:
       print(f"An unexpected error ocurred {e}")
       return False

if len(sys.argv) != 2:
   print(f"Usage: python3 {sys.argv[0]} <service_name>")
   sys.exit(1)

service_to_manage=sys.argv[1]

initial_status=check_service_status(service_to_manage)

if initial_status is True:
   print(f"Result: Service '{service_to_manage}' is already active.")
   exit_code=0
elif initial_status is False:
   print(f"Result: Service '{service_to_manage}' is inactive.")
   start_attempt=start_services(service_to_manage)
   if start_attempt:
      print("\nWaiting briefly to start the service")
      time.sleep(3)
      print("\n Rechecking service status")
      final_status=check_service_status(service_to_manage)
      if final_status is True:
         print(f"Success: Service {service_to_manage} is now active.")
         exit_code=0
      elif final_status is False:
         print("Failure: Service is still inactive after start attempt.")
         exit_code=1
      else:
         print("Warning: Could not determine final service status after start attempt.")
         exit_code = 1
   else:
      print(f"Failure: Could not successfully execute start command for '{service_to_manage}'.")
      exit_code = 1
elif initial_status is None:
    print("Failure: Could not determine initial service status.")
    exit_code = 1 

print("\n---Script Finished---")
sys.exit(exit_code)
