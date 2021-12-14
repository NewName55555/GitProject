"""
Задание по Python

Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
Пример работы:

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
"""

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

def new_level(parent, input_list):
    c = []
    d = {}
    for (a, b) in input_list:
        if a == parent:
            c.append(b)
    for i in c:
        d[i] = new_level(i, input_list)
    return d

def to_tree(input_list):
    main_d = {}
    for (a, b) in input_list:
        if a == None:
            main_d[b] = new_level(b, input_list)
    return main_d

for i in to_tree(source).items():
    print(i)
        



































