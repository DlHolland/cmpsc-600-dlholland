import mako
from mako import template
from mako.template import Template

Template("hello")

# XXX(fletcher): for some reason, bandit is missing the one below. keeping it
# in for now so that if it gets fixed inadvertitently we know.
mako.template.Template("hern")
template.Template("hern")
