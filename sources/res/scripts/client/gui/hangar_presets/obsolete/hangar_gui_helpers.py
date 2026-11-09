# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_presets/obsolete/hangar_gui_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/obsolete/hangar_gui_helpers.py
import operator
from functools import wraps
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

def ifComponentAvailable(componentType=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangar, *args, **kwargs):
            hangarGuiCtrl = dependency.instance(IHangarGuiController)
            if hangarGuiCtrl.sfController.isComponentAvailable(componentType):
                return method(hangar, *args, **kwargs)

        return wrapper

    return decorator


def ifComponentInPreset(componentType=None, defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(presetGetter, *args, **kwargs):
            preset = presetGetter.getPreset()
            if preset is not None and componentType in preset.visibleComponents:
                return method(presetGetter, preset, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(presetGetter)
                return defReturn

        return wrapper

    return decorator


def hasCurrentPreset(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangarGuiSfCtrl, *args, **kwargs):
            currentPreset = hangarGuiSfCtrl.getCurrentPreset()
            if currentPreset is not None:
                return method(hangarGuiSfCtrl, currentPreset, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(hangarGuiSfCtrl)
                return defReturn

        return wrapper

    return decorator
