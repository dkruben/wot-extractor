# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/py_object_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/py_object_wrappers.py
from __future__ import absolute_import
from constants import IS_EDITOR, IS_WEB, IS_CGF_DUMP
if not (IS_EDITOR or IS_WEB or IS_CGF_DUMP):
    import _wulf as _py_objects
else:
    import wulf_wrapper as _py_objects
ValueType = _py_objects.ValueType
Resource = _py_objects.Resource
PyObjectArray = _py_objects.PyObjectArray
PyObjectMap = _py_objects.PyObjectMap
PyObjectCommand = _py_objects.PyObjectCommand
PyGuiApplication = _py_objects.PyGuiApplication
PyObjectViewSettings = _py_objects.PyObjectViewSettings
PyObjectView = _py_objects.PyObjectView
PyObjectViewModel = _py_objects.PyObjectViewModel
PyObjectWindowSettings = _py_objects.PyObjectWindowSettings
PyObjectWindow = _py_objects.PyObjectWindow
PyObjectWindowsArea = _py_objects.PyObjectWindowsArea
PyResAccessor = _py_objects.ResAccessor
isTranslatedKeyValid = _py_objects.isTranslatedKeyValid
isTranslatedTextExisted = _py_objects.isTranslatedTextExisted
getTranslatedText = _py_objects.getTranslatedText
getTranslatedPluralText = _py_objects.getTranslatedPluralText
getImagePath = _py_objects.getImagePath
getSoundEffectId = _py_objects.getSoundEffectId
getLayoutPath = _py_objects.getLayoutPath
getTranslatedTextByResId = _py_objects.getTranslatedTextByResId
getTranslatedPluralTextByResId = _py_objects.getTranslatedPluralTextByResId
getTranslatedKey = _py_objects.getTranslatedKey
getNumberFormat = _py_objects.getNumberFormat
getRealFormat = _py_objects.getRealFormat
getTimeFormat = _py_objects.getTimeFormat
getDateFormat = _py_objects.getDateFormat
caseMap = _py_objects.caseMap
__all__ = ('ValueType', 'Resource', 'PyObjectArray', 'PyObjectMap', 'PyObjectCommand',
           'PyGuiApplication', 'PyObjectViewSettings', 'PyObjectView', 'PyObjectViewModel',
           'PyObjectWindowSettings', 'PyObjectWindow', 'PyObjectWindowsArea', 'PyResAccessor',
           'isTranslatedKeyValid', 'isTranslatedTextExisted', 'getTranslatedText',
           'getTranslatedPluralText', 'getImagePath', 'getSoundEffectId', 'getLayoutPath',
           'getTranslatedTextByResId', 'getTranslatedPluralTextByResId', 'getTranslatedKey',
           'getNumberFormat', 'getRealFormat', 'getTimeFormat', 'getDateFormat',
           'caseMap')
