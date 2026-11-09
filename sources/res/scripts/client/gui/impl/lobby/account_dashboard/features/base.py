# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_dashboard/features/base.py
import typing
if typing.TYPE_CHECKING:
    from typing import Union
    from gui.impl.gen.view_models.views.lobby.account_dashboard.account_dashboard_model import AccountDashboardModel

class FeatureItem(object):

    def __init__(self, viewModel):
        self._viewModel = viewModel

    def initialize(self, *args, **kwargs):
        pass

    def finalize(self):
        self._viewModel = None
        return

    def createToolTipContent(self, event, contentID):
        pass

    def createPopOverContent(self, event):
        pass

    def _fillModel(self, model):
        raise NotImplementedError

    def fill(self, ctx=None):
        if ctx is None:
            with self._viewModel.transaction() as tx:
                self._fillModel(tx)
        else:
            self._fillModel(ctx)
        return

    def getViewModel(self):
        return self._viewModel
