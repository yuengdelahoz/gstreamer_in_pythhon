#! /bin/bash
#
# docker_build.sh
# Copyright (C) 2021 careai <careai@careai-desktop>
#
# Distributed under terms of the MIT license.
#


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
docker build $DIR -t ysdelahoz/gstreamer:python3

