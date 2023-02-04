import os

if __name__ == "__main__":
    name = os.environ.get("WORKFLOW_NAME", 'world')
    print(f'Hello, {name}!')
