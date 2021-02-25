FROM mavi0/gstreamerparser
LABEL mantainer="Yueng De La Hoz <ysdelahoz@gmail.com>"
ENV DEBIAN_FRONTEND noninteractive

RUN apt update
RUN apt-get install -y \
	libgstrtspserver-1.0-0 \
	gstreamer1.0-rtsp \
	libgirepository1.0-dev \
	gobject-introspection \
	gir1.2-gst-rtsp-server-1.0 \
	python3-gi python3-dev python3-gst-1.0 \
	less

WORKDIR /home/developer
RUN echo "set -o vi" >> ~/.bashrc
CMD ["bash"]

