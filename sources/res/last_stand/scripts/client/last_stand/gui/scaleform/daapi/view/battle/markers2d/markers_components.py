# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/markers2d/markers_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/markers2d/markers_components.py
from __future__ import absolute_import
from chat_commands_consts import DefaultMarkerSubType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import World2DActionMarkerComponent

class Camp2DActionMarkerComponent(World2DActionMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        super(Camp2DActionMarkerComponent, self)._setupMarker(gui)
        gui.setMarkerSubType(self.componentID, DefaultMarkerSubType.ENEMY_MARKER_SUBTYPE)
        gui.setHasAnimation(self.componentID, True)
        gui.onReplyFeedbackReceived += self._updateSticky
        return True

    def _deleteMarker(self):
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.onReplyFeedbackReceived -= self._updateSticky
        super(Camp2DActionMarkerComponent, self)._deleteMarker()

    def _updateSticky(self, componentID, isSticky):
        if self._componentID != componentID:
            return
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.setMarkerSticky(self.componentID, isSticky)


class Magnus2DActionMarkerComponent(World2DActionMarkerComponent):

    @classmethod
    def configReader(cls, section):
        config = super(Magnus2DActionMarkerComponent, cls).configReader(section)
        config.update({'shape': ''})
        return config

    def _setupMarker(self, gui, **kwargs):
        super(Magnus2DActionMarkerComponent, self)._setupMarker(gui)
        gui.setMarkerSubType(self.componentID, DefaultMarkerSubType.ALLY_MARKER_SUBTYPE)
        gui.setMarkerAlwaysSticky(self.componentID)
        gui.setMarkerSticky(self.componentID, self._config['is_sticky'])
        return True

    def _deleteMarker(self):
        gui = self._gui()
        if gui:
            gui.removeMarkerAlwaysSticky(self.componentID)
        super(Magnus2DActionMarkerComponent, self)._deleteMarker()
