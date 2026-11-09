# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/__init__.py
from __future__ import absolute_import
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_statistics import Comp7ProfileStatistics
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_technique_page import Comp7ProfileTechniquePage
    from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_technique_window import Comp7ProfileTechniqueWindow
    return (
     ComponentSettings(VIEW_ALIAS.PROFILE_STATISTICS, Comp7ProfileStatistics, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE, Comp7ProfileTechniquePage, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_WINDOW, Comp7ProfileTechniqueWindow, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return ()
