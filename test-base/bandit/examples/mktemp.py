import tempfile as tmp
import tempfile.mktemp as mt
from tempfile import mktemp

foo = 'hi'

mktemp(foo)
tempfile.mktemp('foo')
mt(foo)
tmp.mktemp(foo)
