import random
import utils
import matplotlib.pyplot as plt

if __name__ == '__main__':
    num_runs = 5
    pic_n = 1
    for _ in range(num_runs):
        plt.clf()
        # first create a world
        world = utils.create_random_world()
        world.visualize()
        # ramdomly sample target coordinates
        robot = world.robot_lst[0]
        robot_low = 0 + robot.w / 2
        robot_high = world.w - robot.w / 2
        target_coord = (random.randint(robot_low, robot_high),
                        random.randint(robot_low, robot_high))

        # Display the result: 
        plt.scatter(target_coord[1],target_coord[0],s = 100,c = "white")
        """ print(target_coord)
        for j in world.obs_lst:
            print(j.coord) """
        traj = robot.plan_rrt(target_coord, world)
        """ print(len(traj))
        for i in traj:
            print(i)
        print(" ") """
        x = []
        y = []
        for m in traj:
            x.append(m[0])
            y.append(m[1])
        plt.scatter(y,x)
        name = "rrt/result/round" + str(pic_n) + ".png"
        plt.savefig(name)
        pic_n += 1
