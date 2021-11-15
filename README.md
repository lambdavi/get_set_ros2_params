# get_set_ros2_params
## Steps to test:
1. Create a new workspace (mkdir new_ws)
2. Clone this repo
3. Execute "colcon build" in /new_ws
4. Open 2 new terminals and write ". install/setup.bash" in both of them (the working directory has to be /new_ws for both)
5. Now start the global parameter server: ros2 launch my_robot_bringup my_robot.launch.py
6. In the other terminal: ros2 run client client_start
7. (Optional) if u want to try communication between two nodes, open new terminal (in the same directory and repeat 4th command) and type: ros2 run client_star2
