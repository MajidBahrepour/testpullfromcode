
import subprocess

# Discard any local changes using git reset 
subprocess.call(["git", "reset", "--hard"])

# Define the git pull command to execute 
command = ["git", "pull", "origin", "main"]

# Execute the git pull command and capture the output 
output = subprocess.check_output(command)

# Print the output
print(output.decode("utf-8"))

import os


# In[2]:


current_directory = os.getcwd()
file_path= os.path.join(current_directory,'massage.txt')


# In[3]:


file = open(file_path)


# In[4]:


content = file.read()
print(content)
file.close()


# In[ ]:




