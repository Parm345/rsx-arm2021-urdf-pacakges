# rsx-arm2021-urdf-pacakges

## Steps To Use in Rviz

1. Create Catkin Workspace and add these two pacakges to the `src` repository
2. Modify the `default` value of `<arg name="model">` in `display2/launch/display.launch` to be the path to `urdf/urdf_template_4.urdf` in the `urdf_template_4` package
3. Run `roslaunch display2 display.launch`

## Warning

The meshes need to be in the same package as the urdf file to work.
