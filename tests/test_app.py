import sys
print(sys.path)

from src.app import index

def test_index():
    assert index() == "Hello World"

