# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/minor_short_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/minor_short_tooltip.py
from __future__ import absolute_import
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.minor_short_tooltip_model import MinorShortTooltipModel
from gui.impl.pub import ViewImpl

class MinorShortTooltip(ViewImpl):
    __slots__ = ('_icon', '_header', '_description')

    def __init__(self, icon, header, description):
        settings = ViewSettings(R.views.mono.vehicle_hub.tooltips.minor_short_tooltip(), model=MinorShortTooltipModel())
        self._icon = icon
        self._header = header
        self._description = description
        super(MinorShortTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MinorShortTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(MinorShortTooltip, self)._onLoading(*args, **kwargs)
        if self._icon:
            self.viewModel.setIcon(self._icon)
        self.viewModel.setHeader(self._header)
        self.viewModel.setDescription(self._description)
