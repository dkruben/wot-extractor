# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/platoon/tooltip/platoon_alert_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/tooltip/platoon_alert_tooltip.py
from gui.impl.gen import R
from gui.impl import backport
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.lobby.platoon.alert_tooltip_model import AlertTooltipModel

class AlertTooltip(ViewImpl):

    def __init__(self, header, body):
        self.__header = header
        self.__body = body
        settings = ViewSettings(R.views.lobby.platoon.AlertTooltip(), model=AlertTooltipModel())
        super(AlertTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as model:
            model.setHeader(backport.text(self.__header))
            model.setBody(backport.text(self.__body))
