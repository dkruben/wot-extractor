# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/__init__.py
from __future__ import absolute_import
import os
from gui.Scaleform.locale.MENU import MENU
from skeletons.gui.system_messages import ISystemMessages
from skeletons.gui.techtree_events import ITechTreeEventsListener
SCALEFORM_SUPPORT = False
try:
    import _Scaleform
    SCALEFORM_SUPPORT = True
except ImportError:
    raise NotImplementedError('Client not support Scaleform')

SCALEFORM_SWF_PATH_V3 = 'gui/flash'
VEHICLE_TYPES_ICONS_DIR_PATH = '../maps/icons/filters/tanks/'
CUSTOMIZATION_TYPES_ICONS_DIR_PATH = '../maps/icons/filters/customization/'
NATION_FILTER_ICONS_DIR_PATH = '../maps/icons/filters/nations/'
BUTTON_FILTER_ICONS_DIR_PARH = '../maps/icons/library/'
LEVEL_FILTER_ICONS_DIR_PARH = '../maps/icons/filters/levels/'
DEFAULT_VIDEO_BUFFERING_TIME = 2.0

def getVehicleTypeAssetPath(vehicleType, extension='.png'):
    return ('').join([VEHICLE_TYPES_ICONS_DIR_PATH, vehicleType, extension])


def getCustomizationTypeAssetPath(type, extension='.png'):
    return ('').join([CUSTOMIZATION_TYPES_ICONS_DIR_PATH, type, extension])


def getButtonsAssetPath(button, extension='.png'):
    return ('').join((BUTTON_FILTER_ICONS_DIR_PARH, button, extension))


def getNationsFilterAssetPath(nationName, extension='.png'):
    return ('').join((NATION_FILTER_ICONS_DIR_PATH, nationName, extension))


def getLevelsAssetPath(level_str, extension='.png'):
    return ('').join([LEVEL_FILTER_ICONS_DIR_PARH, level_str, extension])


def getNecessaryArenaFrameName(arenaSubType, hasBase=None):
    if arenaSubType.startswith('assault'):
        return ('{0}{1}').format('assault', '1' if hasBase else '2')
    return arenaSubType


def getPathForFlash(path, base=SCALEFORM_SWF_PATH_V3):
    return os.path.relpath(path, base)


def getScaleformConfig(manager):
    from gui.Scaleform.SystemMessagesInterface import SystemMessagesInterface
    messages = SystemMessagesInterface()
    messages.init()
    manager.addInstance(ISystemMessages, messages, finalizer='destroy')
    from gui.Scaleform.daapi.view.lobby.techtree.techtree_events import TechTreeEventsListener
    listener = TechTreeEventsListener()
    listener.init()
    manager.addInstance(ITechTreeEventsListener, listener, finalizer='fini')
