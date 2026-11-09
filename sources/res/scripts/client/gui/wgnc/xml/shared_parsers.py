# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgnc/xml/shared_parsers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/xml/shared_parsers.py
from debug_utils import LOG_WARNING
from gui.wgnc.errors import ParseError

class SectionParser(object):
    __slots__ = ()

    def getTagName(self):
        raise NotImplementedError

    def parse(self, section):
        raise NotImplementedError

    def _readString(self, name, section):
        value = section.readWideString(name, '')
        if not value:
            raise ParseError((u'The {0} of section "{1}" is not defined.').format(name, self.getTagName()))
        return value


class ParsersCollection(SectionParser):
    __slots__ = ('_parsers', )

    def __init__(self, seq):
        super(ParsersCollection, self).__init__()
        self._parsers = dict((parser.getTagName(), parser) for parser in seq)

    def clear(self):
        self._parsers.clear()

    def parse(self, section):
        for name, sub in section.items():
            if name in self._parsers:
                parser = self._parsers[name]
                yield parser.parse(sub)
            else:
                LOG_WARNING(('Tag {0} is not supported. It is ignored.').format(name))
