# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/common/param_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/param_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.param_tooltip_model import ParamTooltipModel
from gui.impl.pub import ViewImpl

class ParamTooltipView(ViewImpl):

    def __init__(self, tooltipType, params, resId):
        settings = ViewSettings(layoutID=resId, model=ParamTooltipModel())
        self._tooltipType = tooltipType
        self._params = params
        super(ParamTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ParamTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ParamTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setType(self._tooltipType)
            model.setParams(self._params)
