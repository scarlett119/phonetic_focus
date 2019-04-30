import re

# # input files
with open('C:/Users/RA12/PycharmProjects/focus/sub12_3d.csv', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    print('csv lines: ' + str(len(lines)))
with open('C:/Users/RA12/PycharmProjects/focus/sub12_3d.TextGrid', 'r', encoding="utf-8") as f1:
    lines1 = f1.readlines()
with open('C:/Users/RA12/PycharmProjects/focus/target_mapping.txt', 'r', encoding="utf-8") as f2:
    maps = f2.readlines()

# # output file
write_file = open('C:/Users/RA12/PycharmProjects/focus/labeled.TextGrid', 'w+', encoding="utf-8")
# copy the first 14 lines in input textgrid to output file
write_file.writelines(lines1[0:14])


# # Block 1: work on the mappings between written forms and target labels
d = {}
# each written form to be replaced as a index; the according target label to replace it as the value of the index
for map in maps:
    # the format of the mapping table: x = y
    # x: written form to be replaced
    # y: target label to replace
    d[map.split('=')[0].strip()] = map.split('=')[1].strip()

# # start from the 15th line of textgrid: sort out data into a 2-d list
intv = []
intvs = []
counter = 1
for i in lines1[14:]:
    if counter <= 4:
        intv.append(i)
        counter = counter + 1
    if counter > 4:
        intvs.append(intv)
        intv = []
        counter = 1
print('textgrid intervals: ' + str(len(intvs)))

# # process csv
csv = []
for line in lines[1:]:
    line = line.strip()
    trial = line.split(',')
    trial[1] = re.sub(r'(Question: )|(Prompt question: )', '', trial[1])
    trial[2] = re.sub(r'Read the sentence: Washing ', '', trial[2])
    trial[2] = re.sub(r' relieves stress.', '', trial[2]).strip()
    if trial[2] in d:
        trial[2] = d[trial[2]]



# # start labeling textgrid based on csv
    if trial[1].find('What fruit can you wash to relieve stress') == 0:
        label = 's1_fc_'
    elif re.search(r'Doing what with.+relieves stress', trial[1]):
        label = 's1_po_'
    elif re.search(r'What can washing.+do for stress', trial[1]):
        label = 's1_pr_'
    elif trial[1].find('Does washing apples relieve stress') == 0:
        label = 's2_fc_'
    elif re.search(r'Does eating.+relieve stress', trial[1]):
        label = 's2_po_'
    elif re.search(r'Does washing.+increase stress', trial[1]):
        label = 's2_pr_'

    intvs[int(trial[0])*2-1][3] = ' '*12 + 'text = "' + label + trial[2] + '" \n'

for each in intvs:
    write_file.writelines(each)













