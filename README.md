# Ros Control Gazebo Test

## Steps to run

Cloning to your catkin workspace src

```bash
cd ~/catkin_ws/src
git clone https://github.com/YePeOn7/ros_control_gazebo_test.git
```

Please run each command in separate console

### 1. Launching Gazebo with empty world

```bash
roslaunch rcg gazebo.launch
```

### 2. Spawn the model to Gazebo

```bash
roslaunch rcg spawn.launch
```

### 3. Run ros controller interface

```bash
roslaunch rcg control.launch
```

### 4. Run ros controller test

```bash
rosrun rcg test.py
```
