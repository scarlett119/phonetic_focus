import re

# set path
with open('C:/Users/scarl/PycharmProjects/focus/3d-19-1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
write_file = open('C:/Users/scarl/PycharmProjects/focus/3d-19-1.csv', 'w+', encoding="utf-8")

# create a 1-dimensional list as placeholder of each element in each trial
d1 =[]
# create a 2-dimensional list as placeholder of each trial
d2 =[]

# loop through each level-3 trial and sort them into the placeholder
for x in lines[23:]:
    x = x.strip()
    if re.search('Level: 1', x):
        break
    if re.search('Level: 2', x):
        break

    if re.search('LogFrame End', x):
        d2.append(d1)
        d1 = []
    elif not re.search('LogFrame Start', x):
        # x = re.sub(r'.+: ', '', x)
        d1.append(x)

# Output
for each in d2:
    write_file.writelines(','.join(each)+'\n')
