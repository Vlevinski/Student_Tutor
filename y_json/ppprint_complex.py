import json
from pprint import pprint

data = '''
[
  {
    "__complex__":true,
    "real":42,
    "imag":36
  },
  {
    "__complex__":true,
    "real":64,
    "imag":11
  }
]
'''
numbers = json.loads(data)
print(numbers)
print(len(numbers))
for i in numbers:
    print(json.dumps(i, indent=4))

pprint(numbers)
