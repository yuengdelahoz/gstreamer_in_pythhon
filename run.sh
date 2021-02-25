#! /bin/sh
#
# run.sh
# Copyright (C) 2021 yuengdelahoz <yuengdelahoz@Yueng>
#
# Distributed under terms of the MIT license.
#

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
docker run --rm -it \
	--net=host \
	--device /dev/video0:/dev/video0 \
	-w /home/developer \
	-v $DIR/src:/home/developer \
	ysdelahoz/gstreamer:python3 bash
