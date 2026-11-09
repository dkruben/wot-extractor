# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/links.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/links.py
from __future__ import absolute_import
import re
from gui import macroses
from debug_utils import LOG_ERROR
from adisp import adisp_process, adisp_async

class URLMacros(object):
    __MACROS_PREFIX = '$'

    def __init__(self, allowedMacroses=None):
        super(URLMacros, self).__init__()
        self.__asyncMacroses = macroses.getAsyncMacroses()
        self.__syncMacroses = macroses.getSyncMacroses()
        macrosKeys = list(self.__syncMacroses)
        macrosKeys.extend(self.__asyncMacroses)
        if allowedMacroses is not None:
            macrosKeys = [key for key in macrosKeys if key in allowedMacroses]
        patterns = []
        for macro in macrosKeys:
            patterns.append('\\%(macro)s\\(.*\\)|\\%(macro)s' % {'macro': (self._getUserMacrosName(macro))})

        self.__filter = re.compile(('|').join(patterns))
        self.__argsFilter = re.compile('\\$(\\w*)(\\((.*)\\))?')
        return

    def clear(self):
        self.__asyncMacroses = None
        self.__syncMacroses = None
        self.__argsFilter = None
        self.__filter = None
        return

    def hasMarcos(self, url):
        return len(self.__filter.findall(url)) > 0

    @adisp_async
    @adisp_process
    def parse(self, url, params=None, callback=(lambda *args: None)):
        for macros in self.__filter.findall(url):
            macroName, _, args = self.__argsFilter.match(macros).groups()
            replacement = yield self._replace(macroName, args, params)
            url = url.replace(macros, replacement)

        callback(url)

    @adisp_async
    @adisp_process
    def _replace(self, macros, args, params, callback):
        result = ''
        if macros in self.__asyncMacroses:
            result = yield self.__asyncMacroses[macros](self, args, params)
        elif macros in self.__syncMacroses:
            result = self.__syncMacroses[macros](args)
        else:
            LOG_ERROR('URL macros is not found', macros)
        callback(result)

    def _getUserMacrosName(self, macros):
        return '%s%s' % (self.__MACROS_PREFIX, str(macros))
