# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/common/base_sub_model_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/base_sub_model_view.py
from __future__ import absolute_import
import typing
from frameworks.wulf import ViewModel
from py2to3 import patched_typing
TViewModel = typing.TypeVar('TViewModel', bound=ViewModel)

class BaseSubModelView(patched_typing.Generic[TViewModel], object):
    __slots__ = ('_viewModel', '_isLoaded')

    def __init__(self, viewModel):
        self._viewModel = viewModel
        self._isLoaded = False

    def isLoaded(self):
        return self._isLoaded

    def onLoading(self, *args, **kwargs):
        self._isLoaded = True

    def initialize(self, *args, **kwargs):
        self._addListeners()

    def update(self, *args, **kwargs):
        pass

    def finalize(self):
        self._removeListeners()
        self._viewModel = None
        return

    def _addListeners(self):
        pass

    def _removeListeners(self):
        pass
