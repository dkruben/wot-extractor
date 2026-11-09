# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/hotkey_updaters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/hotkey_updaters.py
from __future__ import absolute_import
import typing
from collections import namedtuple
import CommandMapping
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
HotKeyCommand = namedtuple('HotKeyCommand', ['command', 'key', 'satelliteKeys'])

class IHotKeysView(object):

    def setHotkeys(self, hotKeyCommands):
        raise NotImplementedError


class HotKeysUpdater(ViewUpdater):

    def initialize(self):
        super(HotKeysUpdater, self).initialize()
        CommandMapping.g_instance.onMappingChanged += self._onMappingChanged
        self._onMappingChanged()

    def finalize(self):
        CommandMapping.g_instance.onMappingChanged -= self._onMappingChanged
        super(HotKeysUpdater, self).finalize()

    def _onMappingChanged(self, *_):
        raise NotImplementedError


class HotKeysViewUpdater(HotKeysUpdater):
    _DEFAULT_KEYS = (
     None, ())

    def __init__(self, commands, view):
        super(HotKeysViewUpdater, self).__init__(view)
        self.__commands = commands

    def _onMappingChanged(self, *_):
        self.view.setHotkeys([HotKeyCommand(command, *(CommandMapping.g_instance.getCommandKeys(command) or self._DEFAULT_KEYS)) for command in self.__commands])
