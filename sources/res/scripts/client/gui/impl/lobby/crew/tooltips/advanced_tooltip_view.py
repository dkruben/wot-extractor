# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/advanced_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/advanced_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.advanced_tooltip_view_model import AdvancedTooltipViewModel
from gui.impl.pub import ViewImpl

class AdvancedTooltipView(ViewImpl):
    __slots__ = ('_movie', '_header', '_description')

    def __init__(self, movie, header, description):
        settings = ViewSettings(R.views.lobby.crew.tooltips.AdvancedTooltipView(), model=AdvancedTooltipViewModel())
        super(AdvancedTooltipView, self).__init__(settings)
        self._movie = movie
        self._header = header
        self._description = description

    @property
    def viewModel(self):
        return super(AdvancedTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(AdvancedTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setMovie(self._movie)
            tx.setHeader(self._header)
            tx.setDescription(self._description)
