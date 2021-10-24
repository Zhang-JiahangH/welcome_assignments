import random

from rrt.utils import create_random_world

if __name__ == '__main__':
    num_runs = 5

    for _ in range(num_runs):
        # first create a world
        world = create_random_world()

        # ramdomly sample target coordinates
        robot = world.robot_lst[0]
        robot_low = 0 + robot.w / 2
        robot_high = world.w - robot.w / 2
        target_coord = (random.randint(robot_low, robot_high),
                        random.randint(robot_low, robot_high))

        traj = robot.plan_rrt(target_coord)
