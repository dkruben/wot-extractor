# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/genConsts/LAYER_NAMES.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/LAYER_NAMES.py


class LAYER_NAMES(object):
    UNDEFINED = ''
    ROOT = 'root'
    MARKER = 'marker'
    VIEWS = 'view'
    SUBVIEW = 'subView'
    TOP_SUB_VIEW = 'topSubView'
    WINDOWS = 'window'
    FULLSCREEN_WINDOWS = 'fullscreenWindow'
    IME = 'ime'
    SYSTEM_MESSAGES = 'systemMessages'
    DIALOGS = 'topWindow'
    SERVICE_LAYOUT = 'serviceLayout'
    HIDDEN_SERVICE_LAYOUT = 'hiddenServiceLayout'
    OVERLAY = 'overlay'
    TOOL_TIPS = 'toolTips'
    WAITING = 'waiting'
    CURSOR = 'cursor'
    LAYER_ORDER = [UNDEFINED, ROOT, HIDDEN_SERVICE_LAYOUT, MARKER, VIEWS, SUBVIEW, TOP_SUB_VIEW, 
     WINDOWS, FULLSCREEN_WINDOWS, SYSTEM_MESSAGES, DIALOGS, OVERLAY, IME, 
     SERVICE_LAYOUT, TOOL_TIPS, CURSOR, WAITING]
    FOCUS_ORDER = [WAITING, OVERLAY, DIALOGS, FULLSCREEN_WINDOWS, WINDOWS, TOP_SUB_VIEW, SUBVIEW, 
     VIEWS, MARKER]
