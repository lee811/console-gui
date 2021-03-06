#!/usr/bin/python

import urwid, elements, entry
from subprocess import call

def on_ask_change(edit, new_edit_text, pre):
	entry.main.original_widget.body.widget_list[2].set_text(('streak', pre + new_edit_text))

def exit_program():
    raise urwid.ExitMainLoop()

def execute_result(button=None, widget=None):
    if widget == None:
	exit_program()
        # next widget
        pass
    else:
        entry.main.original_widget = widget

def execute_widget():
    elements.Execute('ls / -lh').update_widget(execute_result)

def text_result(button):
    exit_program()

def text_widget():
    text = elements.Text(title='Congratulations, ' + answers[-1] + '!', 
        text='text.txt')
    entry.main.original_widget = text.get_widget(text_result)

def qna_result(button, qnaObj):
    if qnaObj.answer != '':
       answers.append(qnaObj.answer)
       text_widget()

def qna_widget():
    qna = elements.QnA(title='Widget #2', question='What is your name?')
    entry.main.original_widget = qna.get_widget(qna_result)

def menu_result(button, choice):
    answers.append(choice)
    qna_widget()

def menu_widget():
    choices = ' 0 1 2 3 4 5 6 7 8 9'.split()
    title = 'Widget #1'
    question = 'Choose a number'
    menuObj = elements.Menu(title, question, choices)
    entry.main.original_widget = menuObj.get_widget(menu_result)

install_script = "script.sh"
answers = []
entry.draw()
menu_widget()

def start():
    entry.loop.run()
    return install_script
