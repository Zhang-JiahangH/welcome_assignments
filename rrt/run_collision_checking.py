from env import World
from utils import check_collision
from robot import Obstacle, Robot

if __name__ == '__main__':
    world = World()
    obs0 = Obstacle((200, 200))
    world.add_obs(obs0)
    obs1 = Obstacle((65, 340))
    world.add_obs(obs1)
    obs2 = Obstacle((340, 65))
    world.add_obs(obs2)
    robot0 = Robot((100, 100))
    world.add_robot(robot0)

    assert not check_collision(robot0, obs0)
    world.visualize()

    # set the robot to a new pos
    robot0.reset_pos((340, 65))
    world.visualize()
    assert check_collision(robot0, obs2)

    # set the robot to a new pos
    robot0.reset_pos((25, 300))
    world.visualize()
    assert  check_collision(robot0, obs1)
