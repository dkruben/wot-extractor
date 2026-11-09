# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSBuffWithBoosterSequencesComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSBuffWithBoosterSequencesComponent.py
from __future__ import absolute_import
from LSBuffSequencesComponent import LSBuffSequencesComponent
from dyn_components_groups import groupComponent
from xml_config_specs import StrParam, Vector3Param, ListParam, ObjParam, IntParam, BoolParam
_DEFAULTS = 'default'

@groupComponent(sequences=ListParam(valueParam=ObjParam(sequence=StrParam(), bindNode=StrParam(), offset=Vector3Param(), loopCount=IntParam(default=-1), autoStart=BoolParam(default=True), visibleTo=StrParam(default='all'), sniperModeVisibleTo=StrParam(default='all'), checkNodeExists=BoolParam(default=False), boosterFactors=StrParam(default=_DEFAULTS))))
class LSBuffWithBoosterSequencesComponent(LSBuffSequencesComponent):

    def __init__(self):
        super(LSBuffWithBoosterSequencesComponent, self).__init__()
        self._sequences = None
        return

    @property
    def _componentConfigs(self):
        if not self._sequences:
            matchedItems = []
            defaults = []
            factorSet = set(self.factors.split())
            for seq in self.groupComponentConfig.sequences:
                if seq.boosterFactors == _DEFAULTS:
                    defaults.append(seq)
                elif not factorSet.isdisjoint(seq.boosterFactors.split()):
                    matchedItems.append(seq)

            self._sequences = matchedItems if matchedItems else defaults
        return self._sequences
