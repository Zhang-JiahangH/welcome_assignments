import rrt
import utils
import env
import math

class Obj(object):
    def __init__(self, coord, w, color):
        self.coord = coord
        self.w = w
        self.color = color

    def draw(self, world_map):
        """world_map is where we want to draw the robot."""
        world_map[self.coord[0] - self.w // 2: self.coord[0] + self.w // 2,
        self.coord[1] - self.w // 2: self.coord[1] + self.w // 2] = self.color

    def reset_pos(self, coord):
        self.coord = coord


class Robot(Obj):
    def __init__(self, coord, w=40, color=100):
        super(Robot, self).__init__(coord, w, color)

    def plan_rrt(self, tgt_coord, world, step=10.0):
        """tgt_coord is a x,y tuple"""
        # student implements it.
        target = Robot(tgt_coord)
        # check whether the target is legal
        path=[]
        for i in world.obs_lst:
            if utils.check_collision(target, i):
                return path
        # initialize the stopping criteria
        find = False
        # initialize the node list storage
        seed = rrt.node(self.coord[0], self.coord[1])
        node_list = [seed]
        # initialize the outpue
        path=[]
        while not find:
            # assume we can find next point
            satis = True
            random_point = rrt.random_node(world)
            parent_index = rrt.get_nearest(node_list, random_point)
            parent = node_list[parent_index]
            # calculate the expected next stop for robot
            theta = math.atan2(random_point.y_index - parent.y_index, random_point.x_index - parent.x_index)
            new_stop = rrt.node(parent.x_index + step*math.cos(theta), parent.y_index + step*math.sin(theta))
            new_stop.parent = parent
            rob_temp = Robot((new_stop.x_index, new_stop.y_index))
            for j in world.obs_lst:
                if utils.check_collision(j, rob_temp):
                    satis = False
            if satis: 
                node_list.append(new_stop)
                # determine whether it is close enough to the target
                dx = new_stop.x_index - tgt_coord[0]
                dy = new_stop.y_index - tgt_coord[1]
                d = math.sqrt(dx * dx + dy * dy)
                if d <= step:
                    path.append(tgt_coord)
                    find = True
                    break
        # output/return the path which lead to the target
        nodes = node_list[len(node_list)-1]
        path.append((nodes.x_index, nodes.y_index))
        while nodes.parent != None:
            nodes = nodes.parent
            path.append((nodes.x_index, nodes.y_index))
        return path

        
class Obstacle(Obj):
    def __init__(self, coord, w=80, color=50):
        super(Obstacle, self).__init__(coord, w, color)


