import subprocess

# Discard any local changes using git reset 
subprocess.call(["git", "reset", "--hard"])

# Define the git pull command to execute 
command = ["git", "pull"]

# Execute the git pull command and capture the output 
output = subprocess.check_output(command)

# Print the output
print(output.decode("utf-8"))
