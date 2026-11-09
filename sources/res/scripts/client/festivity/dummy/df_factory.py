# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/festivity/dummy/df_factory.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/dummy/df_factory.py
from __future__ import absolute_import
from festivity.dummy.df_controller import DummyController
from festivity.dummy.df_processor import DummyCommandsProcessor
from festivity.dummy.df_requester import DummyRequester
from skeletons.festivity_factory import IFestivityFactory

class DummyFactory(IFestivityFactory):

    def __init__(self):
        self.__requester = DummyRequester()
        self.__processor = DummyCommandsProcessor()
        self.__controller = DummyController()

    def getRequester(self):
        return self.__requester

    def getProcessor(self):
        return self.__processor

    def getController(self):
        return self.__controller
