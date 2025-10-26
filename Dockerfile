FROM osrf/ros:kilted-desktop

# Install deps
RUN apt update \
    # && apt upgrade -y \
    && apt install python3-pip python3-colcon-common-extensions python3-rosdep -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install requirements
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt --break-system-packages

# Build your code
#RUN . /opt/ros/kilted/setup.sh \
#    && rosdep update && rosdep install --from-paths src --ignore-src -r -y \
#    && colcon build
