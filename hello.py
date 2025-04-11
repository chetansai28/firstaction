import os

# Read input from environment variable
name = os.getenv('INPUT_NAME')  # GitHub Actions passes input like this

print(f"Hello, {name}! Welcome to GitHub Actions.")
