# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mode_selector/tooltips/mode_selector_alert_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/tooltips/mode_selector_alert_tooltip.py
from gui.impl.gen import R
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.windows.simple_tooltip_content_model import SimpleTooltipContentModel
from gui.impl.pub import ViewImpl

class AlertTooltip(ViewImpl):

    def __init__(self, header, body, alert):
        self.__header = header
        self.__body = body
        self.__alert = alert
        settings = ViewSettings(R.views.lobby.mode_selector.tooltips.AlertTooltip(), model=SimpleTooltipContentModel())
        super(AlertTooltip, self).__init__(settings)

    def _onLoading(self, *args, **kwargs):
        model = self.getViewModel()
        model.setHeader(self.__header)
        model.setBody(self.__body)
        model.setAlert(self.__alert)
