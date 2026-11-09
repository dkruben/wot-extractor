# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/tooltips/setup_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_post_progression/tooltips/setup_tooltip_view.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.setup_tooltip_view_model import SetupTooltipViewModel, SetupFeatureType
from gui.impl.lobby.veh_post_progression.tooltips.base_feature_tooltip_view import BaseFeatureTooltipView

class SetupTooltipView(BaseFeatureTooltipView):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(SetupTooltipView, self).__init__(R.views.lobby.veh_post_progression.tooltip.SetupTooltipView(), SetupTooltipViewModel(), *args, **kwargs)

    @property
    def viewModel(self):
        return super(SetupTooltipView, self).getViewModel()

    def _onLoading(self, step, *args, **kwargs):
        super(SetupTooltipView, self)._onLoading(step, *args, **kwargs)
        feature = kwargs.get('feature')
        isLevelShown = kwargs.get('isLevelShown', True)
        if feature is not None:
            with self.viewModel.transaction() as model:
                model.setIconName(feature.imgName)
                model.setType(SetupFeatureType(feature.name))
                model.setIsLevelShown(isLevelShown)
        return
