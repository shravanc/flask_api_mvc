import os

yourpath = os.path.abspath(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))
