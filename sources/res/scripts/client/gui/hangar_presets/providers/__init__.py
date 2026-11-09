# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_presets/providers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/providers/__init__.py
from constants import QUEUE_TYPE
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider
from gui.hangar_presets.providers.random_dynamic_gui_providers import RandomHangarDynamicGuiProvider, WinbackHangarDynamicGuiProvider, RandomNP2HangarDynamicGuiProvider
from gui.hangar_presets.providers.event_dynamic_gui_provider import EventHangarDynamicGuiProvider
from gui.hangar_presets.providers.ranked_dynamic_gui_provider import RankedHangarDynamicGuiProvider
from gui.hangar_presets.providers.mapbox_dynamic_gui_provider import MapboxHangarDynamicGuiProvider
from gui.hangar_presets.providers.maps_training_dynamic_gui_provider import MapsTrainingHangarDynamicGuiProvider
from gui.hangar_presets.providers.spec_battle_dynamic_gui_providers import SpecBattleHangarDynamicGuiProvider
from gui.shared.system_factory import registerHangarDynamicGuiProvider
registerHangarDynamicGuiProvider(QUEUE_TYPE.UNKNOWN, DefaultHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.RANDOMS, RandomHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.EVENT_BATTLES, EventHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.RANKED, RankedHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.MAPBOX, MapboxHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.MAPS_TRAINING, MapsTrainingHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.WINBACK, WinbackHangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.RANDOM_NP2, RandomNP2HangarDynamicGuiProvider)
registerHangarDynamicGuiProvider(QUEUE_TYPE.SPEC_BATTLE, SpecBattleHangarDynamicGuiProvider)
