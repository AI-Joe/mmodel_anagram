import os

if sorted(os.getenv('STRING_ONE').replace(" ", "")) == sorted(os.getenv('STRING_TWO').replace(" ", "")):
    print(True)
else:
    print(False)
