import re

nospace = re.compile('\S+')

quotation = re.compile('("\S)[^"]*(\S")')

twonum = re.compile('(?<=[ \n])(-?([0-9]*\.[0-9]+|[0-9]+))(\s|,|, )(-?([0-9]*\.[0-9]+|[0-9]+))')

likely_name = re.compile('([A-Z][a-z]([a-z]*)?|[A-Z][.])[ ]([A-Z][a-z]([a-z]*)?)([ ][A-Z][a-z]*)?')