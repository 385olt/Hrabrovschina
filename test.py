import copy
import pickle

REMEMBERED_FILE = 'remembered.pickled'

remembered = pickle.load(open(REMEMBERED_FILE, 'rb'))

def get_indexes(source, target, start_index = 0):
    if target not in source[start_index:]:
        return []

    index = source.index(target, start_index)
    return [index] + get_indexes(source, target, index + 1)

def find_pos(lists, target, found_pos = {}):
    new_found_pos = dict()
    for i, l in enumerate(lists):
        indexes = get_indexes(l, target)
        if bool(indexes):
            new_found_pos[i] = dict()
            for index in indexes:
                if i in found_pos and index in found_pos[i]:
                    if l[index] == target:
                        new_found_pos[i][index + 1] = found_pos[i][index] + 1
                else:
                    new_found_pos[i][index + 1] = 1
    return new_found_pos

def get_next(lists, found_pos):
    nexts = list()
    for i in found_pos:
        for p in found_pos[i]:
            if found_pos[i][p] > 1 and p < len(lists[i]):
                for k in range(1, found_pos[i][p]):
                    nexts.append(lists[i][p])
    return nexts

found_positions = dict()

print(remembered[:20])

found_positions = find_pos(remembered, 'постмодернист', found_positions)
print(found_positions)
print('nexts: ' + str(get_next(remembered, found_positions)))
found_positions = find_pos(remembered, 'Ф.', found_positions)
print(found_positions)
print('nexts: ' + str(get_next(remembered, found_positions)))
found_positions = find_pos(remembered, 'Ницше', found_positions)
print(found_positions)
print('nexts: ' + str(get_next(remembered, found_positions)))
