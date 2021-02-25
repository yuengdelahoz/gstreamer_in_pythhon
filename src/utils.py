#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 yuengdelahoz <yuengdelahoz@Yueng>
#
# Distributed under terms of the MIT license.

"""

"""
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GObject, Gst, GstRtspServer
from gi.repository import GLib
import sys

def create_gst_element(element, name):
	ele = Gst.ElementFactory.make(element,name)
	if not ele:
		sys.stderr.write(" Unable to create %s \n" % name)
	print("Creating %s " % name)
	return ele
