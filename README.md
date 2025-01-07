## Assignment2_rt_part2

This project is a ROS2-based implementation that replicates the behavior previously implemented in turtlesim, now adapted for a new robot and simulation environment. Using the `robot_urdf` repository's ROS2 branch, the robot is spawned at position (2, 2) in the Gazebo simulation environment. The goal is to develop a ROS2 package with a single node capable of moving the robot around in the simulation environment.
## Prerequisites
Before running this project, ensure you have the following installed:

1. **ROS2 Foxy**.
2. **Gazebo and necessary ROS2 plugins**:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install ros-foxy-xacro ros-foxy-joint-state-publisher ros-foxy-gazebo*
   ```
  3. **Clone the robot_urdf repository**:
     ```bash
     git clone https://github.com/CarmineD8/robot_urdf.git
     cd robot_urdf
     git checkout ros2
     ```

     ## Installation
    ## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/MahmoudElderiny/assignment2_rt_part2.git
   cd assignment2_rt_part2
   ```
 2. **Build the ROS2 package**:
     ```bash
     colcon build
     ```
3. **Source the workspace**:
     ```bash
     source install/setup.bash
     ```
     
## How It Works

The project consists of a ROS2 node that controls the robot's movement in the Gazebo simulation environment. The node subscribes to necessary topics to monitor the robot's state and publishes commands to move it.


## Running the Simulation
1. **Launch the Gazebo simulation with the robot**:
```bash
ros2 launch robot_urdf gazebo.launch.py
```
2. **Run the ROS2 node**:
```bash
ros2 run assignment2_rt_part2 example_node.py robot_controller.py
```

## Repository Structure

- `src/`: Contains the ROS2 node implementation.
- `launch/`: Includes launch files for the ROS2 environment.
- `urdf/`: Contains the robot's URDF files for simulation.

## Notes

- Make sure Gazebo is installed and running properly before launching the simulation.
- Ensure that you are on the ROS2 branch of the `robot_urdf` repository.
