# skeleton-ros

## PyCharm sync packages fix

<https://github.com/LuxerIThink/ros2-pycharm-fix>

Directories:

`/opt/ros/kilted/lib/python3.12/site-packages/`
`/opt/ros/kilted/local/lib/python3.12/dist-packages/`

## Compile and run

```bash
make d-python
source /opt/ros/kilted/setup.sh
rosdep install -i --from-path src --rosdistro kilted -y
colcon build --packages-select car
source install/setup.bash
ros2 run car talker
ros2 run car listener
```
