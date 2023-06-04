import re

test_1 = re.sub('\D', '', 'abc123')

print(test_1)
if test_1 is not None:
    print("Yes")