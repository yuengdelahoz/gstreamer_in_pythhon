#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 yuengdelahoz <yuengdelahoz@Yueng>
#
# Distributed under terms of the MIT license.

"""
Basic tutorial 1: Hello world!

"""

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject,GLib
import sys

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

''' Initialize GStreamer '''
Gst.init(None)

''' Build Pipeline '''
pipeline = Gst.parse_launch("playbin uri=https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm")

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




