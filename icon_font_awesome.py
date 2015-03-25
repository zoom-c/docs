import sys
from docutils.nodes import emphasis
from docutils.parsers.rst.roles import set_classes

def icon_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
	options.update({'classes': ["fa-" + x for x in text.split(",")]})
	options['classes'].append('fa')
	set_classes(options)
	node = emphasis(**options)
	return [node], []

def setup(app):
	app.info('Adding the icon role')
	app.add_role('icon', icon_role)
	return
