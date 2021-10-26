# RRT and Collision Checking

## Description

In this assignment, you will implement several functions to plan collision-free trajectories for a robot among several 
fixed obstacles in a 2d environment. The code skeleton is written in Python, while you are welcome to rewrite it and 
implement the required functionalities in C++.

To check whether your implementation is right, please follow the following steps and verify the output of your code.

### Step 1. Visualize a world with several obstacles and one robot

Once you finish implementing the function World::visualize in env.py. Run env.py, you will see 
something like this:
[Step 1. Expected result](misc/step1.png).

### Step 2. Check collision

Once you finish implementing the function check_collision in utils.py. Run run_collision_checking.py, there 
should be no exception raised.

### Step 3. Randomly create worlds with 2 obstacles and a robot

Once you finish implementing the function create_random_world in utils.py. Run run_random_world.py, you should be able 
to create a random world and there should be no overlapping between different obstacles and between obstacles and the robot.

### Step 4. RRT

Once you finish implement the function Robot::plan_rrt in robot.py. Run run_rrt.py. You will 
run your rrt planner 5 times. You should show that your planner can generate a collision-free trajectory for your 
robot from the initial pos to the sampled target pos. You should also show your planner can deal with the situation where the sampled 
target pos is in collision with one obstacle so that it is invalid.

**Comment: ** For this part, in order to check the collision efficiently, import the env and utils. To record the path nodes, create a new class called node in rrt.py and implement some helper functions

** visualized outcomes are stored in (result) **




