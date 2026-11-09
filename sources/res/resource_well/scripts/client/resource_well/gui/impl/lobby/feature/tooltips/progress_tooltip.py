# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/tooltips/progress_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/lobby/feature/tooltips/progress_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from resource_well.gui.impl.gen.view_models.views.lobby.tooltips.progress_tooltip_model import ProgressTooltipModel

class ProgressTooltip(ViewImpl):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.resource_well.mono.lobby.tooltips.progress_tooltip(), model=ProgressTooltipModel(), args=args, kwargs=kwargs)
        super(ProgressTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ProgressTooltip, self).getViewModel()

    def _onLoading(self, progress, *args, **kwargs):
        diff = kwargs.pop('diff', None)
        super(ProgressTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setCurrentProgress(progress)
            if diff is not None:
                model.setNeedShowDiff(True)
                model.setProgressDiff(diff)
        return
