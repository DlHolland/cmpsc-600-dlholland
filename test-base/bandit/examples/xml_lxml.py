import lxml
import lxml.etree
from defusedxml.lxml import fromstring
from defuxedxml import lxml as potatoe
from lxml import etree

xmlString = "<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"
root = lxml.etree.fromstring(xmlString)
root = fromstring(xmlString)
