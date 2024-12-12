import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Packages to install (listed in requirements.txt)
with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

print("Installing required packages...")
for package in dependencies:
    try:
        __import__(package.split("==")[0].split(">=")[0])
    except ImportError:
        print(f"{package} not found. Installing...")
        install(package)

print("All dependencies installed!")

