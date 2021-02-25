#! /bin/bash
#
# run.sh
# Copyright (C) 2021 yuengdelahoz <yuengdelahoz@Yueng>
#
# Distributed under terms of the MIT license.
#

xhost +
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
docker run --rm -it \
	--net=host \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=unix$DISPLAY \
	--device /dev/snd \
	--device /dev/video0:/dev/video0 \
	-w /home/developer \
	-v $DIR/src:/home/developer \
	-e XDG_RUNTIME_DIR=/run/user/1000 \
	ysdelahoz/gstreamer:python3 
