FROM ubuntu:20.04
LABEL mantainer="Yueng De La Hoz <ysdelahoz@gmail.com>"
ENV DEBIAN_FRONTEND noninteractive

RUN apt update
RUN apt install -y \
	libgstreamer1.0-0 \
	gstreamer1.0-plugins-base \
	gstreamer1.0-plugins-good \
	gstreamer1.0-plugins-bad \
	gstreamer1.0-plugins-ugly \
	gstreamer1.0-libav \
	gstreamer1.0-doc \
	gstreamer1.0-tools \
	gstreamer1.0-x \
	gstreamer1.0-alsa \
	gstreamer1.0-gl \
	gstreamer1.0-pulseaudio \
	libgstrtspserver-1.0-0 \
	libgirepository1.0-dev \
	gstreamer1.0-rtsp \
	gobject-introspection \
	gir1.2-gst-rtsp-server-1.0 \
	python3-gi python3-dev python3-gst-1.0 \
	less \
	alsa-utils
WORKDIR /home/developer
RUN echo "set -o vi" >> ~/.bashrc
CMD ["bash"]

