print(__name__)

if __name__ == '__main__':
    print("Hello! I'm in main module!")
else:
    print("I'm a submodule!")

import itertools

print(itertools.count())
print(itertools.count())
print(itertools.count())
