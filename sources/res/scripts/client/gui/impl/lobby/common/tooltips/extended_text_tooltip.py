# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/tooltips/extended_text_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/tooltips/extended_text_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.extended_text_tooltip_model import ExtendedTextTooltipModel
from gui.impl.pub import ViewImpl

class ExtendedTextTooltip(ViewImpl):
    __slots__ = ('__text', '__stringifyKwargs')

    def __init__(self, text, stringifyKwargs):
        settings = ViewSettings(R.views.lobby.common.tooltips.ExtendedTextTooltip())
        settings.model = ExtendedTextTooltipModel()
        self.__text = text
        self.__stringifyKwargs = stringifyKwargs
        super(ExtendedTextTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ExtendedTextTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setText(self.__text)
            tx.setStringifyKwargs(self.__stringifyKwargs)
