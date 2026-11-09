# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/loggers.py
import logging

def getLogger(loggerName):
    return logging.getLogger(('GameLoading.{}').format(loggerName))


def getSequencesViewHistoryLogger():
    return getLogger('SequencesViewHistory')


def getCdnConfigLogger():
    return getLogger('CdnConfig')


def getCdnCacheLogger():
    return getLogger('CdnCache')


def getResourcesLogger():
    return getLogger('Resources')


def getStatesLogger():
    return getLogger('States')


def getTransitionsLogger():
    return getLogger('Transitions')


def getStateMachineLogger():
    return getLogger('StateMachine')


def getLoaderSettingsLogger():
    return getLogger('LoaderSettings')


def getLoaderLogger():
    return getLogger('Loader')
