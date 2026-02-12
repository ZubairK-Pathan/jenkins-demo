from datetime import datetime
import platform

print("Jenkins Python Automation")

# system info
print("System:", platform.system())

# simple test
def multiply(a, b):
    return a * b

assert multiply(3, 4) == 12
print("Test passed")

# logging
with open("build_log.txt", "a") as f:
    f.write("Build run at: " + str(datetime.now()) + "\n")

print("Log updated")
print("Execution Complete")
