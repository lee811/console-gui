#!/usr/bin/python

import urwid

palette = [
	('banner', 'black', 'light gray'),
	('streak', 'black', 'light red'),
	('bg', 'black', 'dark blue')]

main = None
loop = None

def exit_on_esc(key):
    if str(key) == 'esc':
        raise urwid.ExitMainLoop()

def createOverlay(widget, width, height, valign='middle',
	top=0, right=0, bottom=0, left=0,
	min_width=40, min_height=25):
	return urwid.Overlay(widget, urwid.SolidFill(u"\u0020"),
		align='center', width=('relative', width),
		valign=valign, height=('relative', height),
		min_width=min_width, min_height=min_height,
		top=top, bottom=bottom, right=right, left=left)

def draw():
	global main
	global loop
	global palette

	fill = urwid.Filler(urwid.Text("Welcome!"), 'top')
	main = urwid.Padding(fill, left=0, right=0)
	inner_overlay = createOverlay(main, 80, 80, valign='top', top=2, bottom=2)
	overlay_map = urwid.AttrMap(inner_overlay, 'banner')
	overlay = createOverlay(overlay_map, 70, 70, min_width=70, min_height=30)
	bg_map = urwid.AttrMap(overlay, 'bg')
	loop = urwid.MainLoop(bg_map, palette, unhandled_input=exit_on_esc)