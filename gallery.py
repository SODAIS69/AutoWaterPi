import os

pictures=os.listdir(f'{os.path.dirname(os.path.abspath(__file__))}/Captured/')
print(pictures)