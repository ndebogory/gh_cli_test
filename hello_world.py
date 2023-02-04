import os

if __name__ == "__main__":
    if "WORKFLOW_NAME" in os.environ:
        print(f'Hello, {os.environ["WORKFLOW_NAME"]}')
    else:
        print('Hello, world!')
