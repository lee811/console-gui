import urwid

class menu():
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

	def get(self, callback):
	    title = urwid.Text(self.title)
	    question = [title, urwid.Divider(), urwid.Text(self.question), urwid.Divider()]
	    for c in self.choices:
	        button = urwid.Button(c)
	        urwid.connect_signal(button, 'click', callback, c)
	        question.append(urwid.AttrMap(button, None, focus_map='reversed'))
	    return urwid.ListBox(urwid.SimpleFocusListWalker(question))