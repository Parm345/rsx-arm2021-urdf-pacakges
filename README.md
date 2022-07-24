
# Table of Contents

[Steps To Use in Rviz](https://github.com/Parm345/rsx-arm2021-urdf-pacakges#steps-to-use-in-rviz)

[Just Using URDF File](https://github.com/Parm345/rsx-arm2021-urdf-pacakges#just-using-urdf-file)

# Steps To Use in Rviz

The instructions assume you have installed ROS Melodic already.

## 1. Create Catkin Workspace

Follow the commands to create a workspace. Name the workspace whatever you would like. I will use `sample_folder`.

``` Bash
mkdir sample_folder
cd sample_folder
mkdir src
catkin_make
```

## 2. Copy and Paste Packages

Copy `display2` and `urdf_tempalte_4` packages into the `src` folder of the catkin workspace. 

## 3. Install Dependencies Via apt-get


### Needed Packages
``` Bash
joint-state-publisher
ros-melodic-joint-state-publisher
ros-melodic-joint-state-publisher-gui
ros-melodic-robot-state-publisher
```

### Example Terminal Command

``` bash
sudo apt-get install joint-state-publisher
```

## 4. Reference URDF File Location

In the package `display2`, open `display.launch` in the `launch` folder. In `display.launch` set the `default` argument in <arg name="model"> to the absolute path of the urdf file. The `default` argument should look like `.../urdf_template_4/urdf/urdf_template_4.urdf`.

## 5. Rebuild Workspace

`cd` the terminal into the catkin workspace and enter the following command.

``` bash
catkin_make
```

## 6. Source Workspace In Terminal

Still should be in the catkin workspace.

``` bash
source devel/setup.bash
```

## 7. Run The Launch File

``` bash
roslaunch display2 display.launch
```

# Just Using URDF File 

## Warning
The urdf file will only work if it's kept in the `urdf_template_4` package. The urdf file refrences the meshes via the package itself.
