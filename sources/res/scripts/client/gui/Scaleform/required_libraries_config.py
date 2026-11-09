# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/required_libraries_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/required_libraries_config.py
from __future__ import absolute_import
from soft_exception import SoftException
LOBBY_REQUIRED_LIBRARIES = [
 'windows.swf', 
 'animations.swf', 
 'common_i18n.swf', 
 'guiControlsLogin.swf', 
 'guiControlsLoginBattleDynamic.swf', 
 'ub_components.swf', 
 'serviceMessageComponents.swf']
BATTLE_REQUIRED_LIBRARIES = [
 'windows.swf', 
 'common_i18n.swf', 
 'popovers.swf', 
 'guiControlsLobbyBattleDynamic.swf', 
 'guiControlsLoginBattleDynamic.swf', 
 'guiControlsBattleDynamic.swf', 
 'battleMessages.swf']
ADDITIONAL_BATTLE_REQUIRED_LIBRARIES = {}

def addLobbyRequiredLibraries(swfList, personality):
    intersection = set(LOBBY_REQUIRED_LIBRARIES).intersection(set(swfList))
    if intersection:
        raise SoftException(('LOBBY_REQUIRED_LIBRARIES already has swf(s):{swfs}. Personality: {personality}').format(swfs=intersection, personality=personality))
    LOBBY_REQUIRED_LIBRARIES.extend(swfList)


def addBattleRequiredLibraries(swfList, arenaGuiType, personality):
    intersection = set(BATTLE_REQUIRED_LIBRARIES).intersection(set(swfList))
    if intersection:
        raise SoftException(('BATTLE_REQUIRED_LIBRARIES already has swf(s):{swfs}. Personality: {personality}').format(swfs=intersection, personality=personality))
    if arenaGuiType in ADDITIONAL_BATTLE_REQUIRED_LIBRARIES:
        raise SoftException(('ADDITIONAL_BATTLE_REQUIRED_LIBRARIES already has arena gui type:{t}. Personality: {personality}').format(t=arenaGuiType, personality=personality))
    ADDITIONAL_BATTLE_REQUIRED_LIBRARIES.update({arenaGuiType: swfList})
