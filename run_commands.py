#!/usr/bin/env python3

import subprocess
import sys

print("---Running External commands Using Python---")
print("\nRunning 'ls -l etc'..")
try:
    result = subprocess.run(["ls","-l","/etc"], capture_output=True, text=True, check=True)
    print(f"Command executed sucessfully.(Exit code: {result.returncode})")
#Output 1st 100 Characters
    print("Output of first 100 Characters: ")
    print(result.stdout[:100]+ "...")
except FileNotFoundError:
    print("Error: ls command not found. Is it in your PATH? ")
    sys.exit(1)
except subprocess.CalledProcessError as e:
   print(f"Error: Command failed with exit code: {e.returncode}")
   print(f"Stderr:{e.stderr}")
   sys.exit(1)
except Exception as e:
   print(f"An unexpected error occured {e}")
   sys.exit(1)

print("\n-----Running 'ls non_existent_file'-----")

try:
   resfail = subprocess.run(["ls", "non_existent_file"], capture_output=True, text=True, check=True)
   print("Command Executed Sucessfully.")
except subprocess.CalledProcessError as e:
   print(f"Command fail as expected: {e.returncode}")
   print(f"Stderr: {e.stderr.strip()}")

print("\n---Running 'whoami...'")

try:
   whoami = subprocess.run(["whoami"], capture_output=True, check=True, text=True)
   current_user = whoami.stdout.strip()
   print(f"Python script confirms user is: {current_user}")
except Exception as e:
   print("Failed to run 'whoami'{e}")

# Example 4: Running a command that requires sudo (requires careful handling)

SERVICE = "ssh"
print(f"\nChecking status of {SERVICE}, might require 'sudo'...")
try:
   status = subprocess.run(["sudo", "systemctl", "is-active", SERVICE], capture_output=True, text=True)
   if status.returncode == 0:
      print(f"Service {SERVICE} is active.")
   else:
      print(f"Service {SERVICE} is not active. EXIT CODE: {status.returncode}")

except FileNotFoundError:
  print("Error: 'sudo' or 'systemctl' commmand not found")
except Exception as e:
  print(f"An unexpected error ocurred {e}")

