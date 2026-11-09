# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/crew_members_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/crew_members_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.crew_members_tooltip_model import CrewMembersTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class CrewMembersTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.crew_members_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = CrewMembersTooltipModel()
        super(CrewMembersTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CrewMembersTooltip, self).getViewModel()
