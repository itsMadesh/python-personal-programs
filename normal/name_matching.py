import re

names=["amadesh","maappashaa","amma","999"]
for i in names:
    print(re.search("[a-z]",i))