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
from gi.repository import Gst,GObject

''' Initialize GStreamer '''

GObject.threads_init()
Gst.init(None)

''' Build Pipeline '''
pipeline = Gst.parse_launch("playbin uri=https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm")

