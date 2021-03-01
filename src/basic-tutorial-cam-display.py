#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 yuengdelahoz <yuengdelahoz@Yueng>
#
# Distributed under terms of the MIT license.

"""
Tutorial to display camera and save video feed

"""

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject,GLib
import sys
import utils
import os
file_dir =os.path.dirname(__file__)

def on_message(bus, message, loop):
	t = message.type
	if t == Gst.MessageType.EOS:
		sys.stdout.write("End-of-stream\n")
		loop.quit()
	elif t==Gst.MessageType.WARNING:
		err, debug = message.parse_warning()
		sys.stderr.write("Warning: %s: %s\n" % (err, debug))
	elif t == Gst.MessageType.ERROR:
		err, debug = message.parse_error()
		sys.stderr.write("Error: %s: %s\n" % (err, debug))
		loop.quit()
	return True

''' Initialiqueue_displayze GStreamer '''
Gst.init(None)
pipeline = Gst.Pipeline()

src = utils.create_gst_element("v4l2src", "usb-cam");
src_caps = utils.create_gst_element("capsfilter", "source_caps")
src_caps.set_property('caps', Gst.Caps.from_string("video/x-raw, width=640, height=480"))

tee = utils.create_gst_element("tee", "tee");
encoder = utils.create_gst_element("jpegenc","encoder");
encoder_caps = utils.create_gst_element("capsfilter", "encoder_caps")
encoder_caps.set_property("caps", Gst.Caps.from_string("image/jpeg, framerate=30/1"))
muxer = utils.create_gst_element("avimux","muxer");
filesink = utils.create_gst_element("filesink","file_sink");
filesink.set_property("location","rec.avi")

videoconvert = utils.create_gst_element("videoconvert","video_converter");
videoconvert2 = utils.create_gst_element("videoconvert","video_converter2");
videosink = utils.create_gst_element("autovideosink","video_display");
queue_display = utils.create_gst_element("queue", "queue_display");
queue_record = utils.create_gst_element("queue", "queue_record");

pipeline.add(src)
pipeline.add(src_caps)
pipeline.add(tee)
pipeline.add(queue_record)
pipeline.add(videoconvert)
pipeline.add(encoder)
pipeline.add(encoder_caps)
pipeline.add(muxer)
pipeline.add(filesink)
pipeline.add(queue_display)
pipeline.add(videoconvert2)
pipeline.add(videosink)

''' src -> tee 
	       tee -> queue_display -> videconvert -> videosink
	       tee -> queue_record -> encoder -> muxer -> filesink
'''
# src -> tee
src.link(src_caps) 
src_caps.link(tee)

#  tee -> queue_display -> videconvert -> videosink
queue_display.link(videoconvert)
videoconvert.link(videosink)

tee_display_pad=tee.get_request_pad('src_%u')
queue_display_sink_pad = queue_display.get_static_pad('sink')
tee_display_pad.link(queue_display_sink_pad)

#  tee -> queue_record -> videconvert2 -> encode -> muxer -> filesink
queue_record.link(videoconvert2)
videoconvert2.link(encoder)
encoder.link(encoder_caps)
encoder_caps.link(muxer)
muxer.link(filesink)

tee_record_pad=tee.get_request_pad('src_%u')
queue_record_sink_pad = queue_record.get_static_pad('sink')
tee_record_pad.link(queue_record_sink_pad)

loop =GLib.MainLoop()
bus = pipeline.get_bus()
bus.add_signal_watch()
bus.connect("message",on_message, loop)

''' Start playing '''
pipeline.set_state(Gst.State.PLAYING)
try:
	loop.run()
except:
	pass

# cleanup
pipeline.set_state(Gst.State.NULL)
