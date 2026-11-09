# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/__init__.py
from __future__ import absolute_import
from collections import namedtuple
from frameworks.wulf import WindowLayer
import gui.Scaleform.framework.ScopeTemplates
from gui.Scaleform.framework.settings import UIFrameworkImpl

def getSwfExtensionUrl(extension, swf):
    return extension + '|' + swf


class COMMON_VIEW_ALIAS(object):
    LOGIN = 'login'
    LOBBY = 'lobby'
    BATTLE = 'battle'
    CURSOR = 'cursor'
    WAITING = 'waiting'


class GroupedViewSettings(namedtuple('GroupedViewSettings', 'alias clazz url layer group event scope cacheable containers canDrag canClose isModal isCentered flags')):

    def getDAAPIObject(self):
        return {'alias': (self.alias), 
           'url': (self.url), 
           'layer': (self.layer), 
           'event': (self.event), 
           'group': (self.group), 
           'isGrouped': (self.group is not None), 
           'canDrag': (self.canDrag), 
           'canClose': (self.canClose), 
           'isModal': (self.isModal), 
           'isCentered': (self.isCentered), 
           'flags': (self.flags)}

    def replaceSettings(self, settings):
        return self._replace(**settings)

    def toImmutableSettings(self):
        return self


GroupedViewSettings.__new__.__defaults__ = (
 None, None, None, 0, None, None, None, False, None, True, True, False, True, 0)

class ViewSettings(GroupedViewSettings):

    @staticmethod
    def __new__(cls, alias, clazz, url, layer, event, scope, cacheable, containers, canDrag, canClose, isModal, isCentered, flags):
        return GroupedViewSettings.__new__(cls, alias, clazz, url, layer, None, event, scope, cacheable, containers, canDrag, canClose, isModal, isCentered, flags)


ViewSettings.__new__.__defaults__ = (
 None, None, None, 0, None, None, False, None, True, True, False, True, 0)

class ComponentSettings(GroupedViewSettings):

    @staticmethod
    def __new__(cls, alias, clazz, scope):
        return GroupedViewSettings.__new__(cls, alias, clazz, None, WindowLayer.UNDEFINED, None, None, scope, False, None, True, False, True, 0)


ComponentSettings.__new__.__defaults__ = (None, None, None)

class ContainerSettings(namedtuple('ContainerSettings', 'type clazz')):
    pass


ContainerSettings.__new__.__defaults__ = (None, None)
