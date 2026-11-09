# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/tooltips/simple_icon_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/tooltips/simple_icon_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.common.tooltips.simple_icon_tooltip_model import SimpleIconTooltipModel, HeaderType
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class SimpleIconTooltipView(ViewImpl):
    __slots__ = ('__header', '__body', '__icon', '__headerType')

    def __init__(self, header, body, icon, headerType):
        self.__header = header
        self.__body = body
        self.__icon = icon
        self.__headerType = headerType
        settings = ViewSettings(R.views.lobby.common.tooltips.SimpleIconTooltip(), model=SimpleIconTooltipModel())
        super(SimpleIconTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SimpleIconTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setHeader(self.__header)
            tx.setBody(self.__body)
            tx.setIcon(self.__icon)
            tx.setHeaderType(HeaderType(self.__headerType))
