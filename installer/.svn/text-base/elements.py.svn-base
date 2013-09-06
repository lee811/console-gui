import urwid, sys
from subprocess import Popen, PIPE, STDOUT


class Menu():
	def __init__(self, title=None, question=None, choices=None):
		if choices is None:
			self.choices = []
		else:
			self.choices = choices

		if title is None:
			self.title = ''
		else:
			self.title = title

		if question is None:
			self.question = ''
		else:
			self.question = question

	def get_widget(self, callback):
	    title = urwid.Text(('underline', self.title))
	    question = [title, urwid.Divider(),
	    	urwid.Text(self.question),
	    	urwid.Divider()]
	    for c in self.choices:
	        button = urwid.Button(c)
	        urwid.connect_signal(button, 'click', callback, c)
	        question.append(
	        	urwid.AttrMap(button, None, focus_map='reversed'))
	    return urwid.ListBox(urwid.SimpleFocusListWalker(question))

class QnA():
	def __init__(self, title=None, question=None):
		if title is None:
			self.title = ''
		else:
			self.title = title

		if question is None:
			self.question = ''
		else:
			self.question = question

		self.answer = ''

	def get_widget(self, callback):
		title = urwid.Text(('underline', self.title))
		question = urwid.Text(self.question)
		answer = urwid.Edit('')
		button = urwid.Button('Ok')
		div = urwid.Divider()
		urwid.connect_signal(button, 'click', callback, self)
		urwid.connect_signal(answer, 'change', self.__on_change)
		return urwid.Filler(
			urwid.Pile([title, div, question, div, answer, div, button]), valign='top')


	def __on_change(self, edit, new_edit_text):
		self.answer = new_edit_text

class Text():
	def __init__(self, title=None, text=None):
		if title is None:
			self.title = ''
		else:
			self.title = title

		if text is None:
			self.text = ''
		else:
			try:
				with open(text) as text_file:
					self.text = text_file.read()
			except IOError:
				self.text = text

		self.answer = ''

	def get_widget(self, callback):
		title = urwid.Text(('underline', self.title))
		text = urwid.Text(self.text)
		button = urwid.Button('Ok')
		div = urwid.Divider()
		urwid.connect_signal(button, 'click', callback)
		return urwid.Filler(
			urwid.Pile([title, div, text, div, button]), valign='top')

class Execute():
	def __init__(self, cmd=None):
		if cmd is None:
			self.cmd = ''
		else:
			self.cmd = cmd

	def update_widget(self, callback):
		output = ''
		process = Popen(self.cmd.split(), stdout=PIPE, stderr=STDOUT)
		# Poll process for new output until finished
		while True:
			nextline = process.stdout.readline()
			if nextline == '' and process.poll() != None:
				break
			output += str(nextline)
			response = urwid.Text([output, '\n'])
			callback(widget=urwid.Filler(urwid.Pile([response])))

		response = urwid.Text([output, '\n'])
		done = urwid.Button('Ok')
		urwid.connect_signal(done, 'click', callback)
		widget = urwid.Filler(urwid.Pile([response,
			urwid.AttrMap(done, None, focus_map='reversed')]))
		callback(widget=widget)