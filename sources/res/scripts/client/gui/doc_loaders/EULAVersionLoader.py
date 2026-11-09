# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/doc_loaders/EULAVersionLoader.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/doc_loaders/EULAVersionLoader.py
from __future__ import absolute_import
import ResMgr
from helpers import VERSION_FILE_PATH
from soft_exception import SoftException
__author__ = 'd_savitski'
VERSION_TAG = 'showLicense'

class EULAVersionLoader(object):

    def __init__(self):
        super(EULAVersionLoader, self).__init__()
        self.__xmlVersion = 0
        self.loadXMLVersion()

    @property
    def xmlVersion(self):
        return self.__xmlVersion

    def loadXMLVersion(self):
        xmlFile = ResMgr.openSection(VERSION_FILE_PATH)
        if not xmlFile:
            raise SoftException('EULAVersionLoader.loadXMLVersion %s file is missing' % VERSION_FILE_PATH)
        xmlVersion = xmlFile.readString(VERSION_TAG)
        if not xmlVersion:
            raise SoftException('Subsection EULAVersionLoader.loadXMLVersion EULAVersion tag <%(ver)s> is missing or empty in %(path)s' % {'ver': VERSION_TAG, 'path': VERSION_FILE_PATH})
        self.__xmlVersion = int(xmlVersion)
