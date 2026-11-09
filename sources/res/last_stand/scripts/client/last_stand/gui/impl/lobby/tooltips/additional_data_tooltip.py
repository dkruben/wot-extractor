# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/additional_data_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/additional_data_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class AdditionalDataTooltipView(ViewImpl):

    def __init__(self):
        super(AdditionalDataTooltipView, self).__init__(ViewSettings(R.views.last_stand.mono.lobby.tooltips.additional_data_tooltip(), model=ViewModel()))
