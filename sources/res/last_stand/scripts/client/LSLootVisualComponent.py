# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSLootVisualComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSLootVisualComponent.py
from __future__ import absolute_import
from LSBuffSequencesComponent import LSBuffSequencesComponent
from dyn_components_groups import groupComponent
from xml_config_specs import StrParam

@groupComponent(stateParam=StrParam(default='state'))
class LSLootVisualComponent(LSBuffSequencesComponent):

    def __init__(self, stateParam='state'):
        super(LSLootVisualComponent, self).__init__()
        self._stateParam = stateParam

    def set_lootState(self, prev):
        self._onChangeLootState()

    def _onAvatarReady(self):
        super(LSLootVisualComponent, self)._onAvatarReady()
        self._onChangeLootState()

    def _onChangeLootState(self):
        for animator in self._animators:
            animator.setFloatParam(self._stateParam, self.lootState)
