import random
import env
import robot


def check_collision(obj0, obj1):
    """
    Check if the obj0 collides with the obj1.
    Return True, if the obj0 collides with obj1,
    Return False, if the obj0 doesn't collide with obj1.
    """
    # student implements it.
    object0 = [obj0.coord[0]-(obj0.w/2), obj0.coord[1]-(obj0.w/2), obj0.coord[0]+(obj0.w/2), obj0.coord[1]+(obj0.w/2)]
    object1 = [obj1.coord[0]-(obj1.w/2), obj1.coord[1]-(obj1.w/2), obj1.coord[0]+(obj1.w/2), obj1.coord[1]+(obj1.w/2)]
    return not (object0[2] <= object1[0] or object0[3] <= object1[1] or object0[0] >= object1[2] or object0[1] >= object1[3])


def create_random_world():
    """With this function we can create 2 obstacles and 1 robot."""
    world = env.World()
    # student implements it.
    temp_x = random.randint(40,360)
    temp_y = random.randint(40,360)
    obs1 = robot.Obstacle((temp_x,temp_y))
    world.add_obs(obs1)
    temp_x = random.randint(40,360)
    temp_y = random.randint(40,360)
    obs2 = robot.Obstacle((temp_x,temp_y))
    while check_collision(obs1,obs2):
        temp_x = random.randint(40,360)
        temp_y = random.randint(40,360)
        obs2 = robot.Obstacle((temp_x,temp_y))
    world.add_obs(obs2)
    temp_x = random.randint(40,360)
    temp_y = random.randint(40,360)
    rob = robot.Robot((temp_x, temp_y))
    while check_collision(rob, obs1) or check_collision(rob, obs2):
        temp_x = random.randint(40,360)
        temp_y = random.randint(40,360)
        rob = robot.Robot((temp_x, temp_y))
    world.add_robot(rob)
    return world
