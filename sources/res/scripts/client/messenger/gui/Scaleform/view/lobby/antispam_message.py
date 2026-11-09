# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/antispam_message.pyc (uncompyle6 3.9.3 / Python 3.14.3) - nao e o codigo original
# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/antispam_message.py
from __future__ import absolute_import
from constants import IS_CHINA
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import CONTACTS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
MAX_ANTISPAM_MESSAGES = 3
_isClosed = False

def isShownParse error at or near `LOAD_GLOBAL' instruction at offset 0


def close():
    global _isClosed
    counter = _getCounter()
    newCounter = min(counter + 1, MAX_ANTISPAM_MESSAGES)
    _isClosed = True
    if newCounter != counter:
        _setCounter(newCounter)
    return


def reset():
    global _isClosed
    _isClosed = False
    return


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def _getCounter(settingsCore=None):
    return settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.CONTACTS, CONTACTS.ANTISPAM_MESSAGES_COUNTER, default=0)


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def _setCounter(counter, settingsCore=None):
    return settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.CONTACTS, {(CONTACTS.ANTISPAM_MESSAGES_COUNTER): counter})


return
# wot-extractor: AVISO - descompilacao partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 15)
