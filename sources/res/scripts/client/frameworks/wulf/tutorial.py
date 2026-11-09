# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/tutorial.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/tutorial.py
from __future__ import absolute_import
import logging, typing
from .py_object_binder import PyObjectEntity
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
_logger = logging.getLogger(__name__)

class Tutorial(PyObjectEntity):
    __slots__ = ()

    @classmethod
    def create(cls, proxy, model):
        manager = Tutorial()
        manager.bind(proxy)
        proxy.setModel(model.proxy)
        return manager

    def getModel(self):
        return self.proxy.getModel()

    def destroy(self):
        if self.proxy is not None:
            self.proxy.clear()
        self.unbind()
        return
