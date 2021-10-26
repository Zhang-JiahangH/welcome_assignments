import random

class node(object):
    def __init__(self, x, y):
        self.x_index = x
        self.y_index = y
        self.parent = None

def random_node(world):
    x = random.uniform(20, world.w-20)
    y = random.uniform(20, world.w-20)
    return node(x,y)

def get_nearest(node_list, target_node): 
    d_list = []
    for node in node_list:
        d_list.append((node.x_index - target_node.x_index) ** 2 + (node.y_index - target_node.y_index) ** 2)
    min_index = d_list.index(min(d_list))
    return min_index


