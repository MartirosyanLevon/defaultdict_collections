from collections import defaultdict

data = [
    ('Smith', 2),
    ('Anderson', 1),
    ('Cruse', 5),
    ('Anderson', 2),
    ('Fry', 4),
]

marks = defaultdict(int)
marks_list = defaultdict(list)
marks_uniq = defaultdict(set)

for surname, mark in data:
    # print(surname, mark)
    marks[surname] += mark
    marks_list[surname].append(mark)
    marks_uniq[surname].add(mark)

print('MARKS', marks)
print('MARK_LIST', marks_list)
print('MARKS_UNIQ', marks_uniq)
