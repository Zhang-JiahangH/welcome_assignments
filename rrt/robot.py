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

    def plan_rrt(self, tgt_coord):
        """tgt_coord is a x,y tuple"""
        # student implements it.
        pass


class Obstacle(Obj):
    def __init__(self, coord, w=80, color=50):
        super(Obstacle, self).__init__(coord, w, color)
