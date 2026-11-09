# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/maps_training/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/maps_training/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.shared import EVENT_BUS_SCOPE
from gui.app_loader import settings

def getStateMachineRegistrators():
    from gui.impl.lobby.maps_training.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    from gui.impl.lobby.maps_training.maps_training_result_view import MapsTrainingResultWindow
    return (
     ViewSettings(VIEW_ALIAS.MAPS_TRAINING_BATTLE_RESULTS, MapsTrainingResultWindow, '', WindowLayer.TOP_WINDOW, VIEW_ALIAS.MAPS_TRAINING_BATTLE_RESULTS, ScopeTemplates.LOBBY_SUB_SCOPE, True),)


def getContextMenuHandlers():
    return ()


def getBusinessHandlers():
    return (
     _MapsTrainingPackageBusinessHandler(),)


class _MapsTrainingPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.MAPS_TRAINING_BATTLE_RESULTS, self.loadView),)
        super(_MapsTrainingPackageBusinessHandler, self).__init__(listeners, settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
