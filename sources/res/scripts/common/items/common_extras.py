# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/common_extras.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/common_extras.py
from __future__ import absolute_import
from extension_utils import importClass
from items import _xml
from constants import IS_CLIENT, IS_EDITOR, IS_BOT
import collections

def readExtras(xmlCtx, section, subsectionName, defaultModName, **kwargs):
    NoneExtra = importClass('NoneExtra', defaultModName)
    noneExtra = NoneExtra('_NoneExtra', 0, '', None)
    extras = [
     noneExtra]
    extrasDict = {(noneExtra.name): noneExtra}
    for extraName, extraSection in _xml.getChildren(xmlCtx, section, subsectionName):
        ctx = (xmlCtx, subsectionName + '/' + extraName)
        if extrasDict.has_key(extraName):
            _xml.raiseWrongXml(ctx, '', 'name is not unique')
        clientName, _, serverName = extraSection.asString.partition(':')
        classPath = (clientName if IS_CLIENT or IS_EDITOR or IS_BOT else serverName).strip()
        classObj = importClass(classPath, defaultModName)
        if classObj is not None:
            classExtras = classObj(extraName, len(extras), xmlCtx[1], extraSection, **kwargs)
            if isinstance(classExtras, collections.Iterable):
                for extra in classExtras:
                    extrasDict[extra.name] = extra

                extras.extend(classExtras)
            else:
                extras.append(classExtras)
                extrasDict[extraName] = classExtras
        else:
            _xml.raiseWrongXml(ctx, '', "Can't import %s" % classPath)

    if len(extras) > 200:
        _xml.raiseWrongXml(xmlCtx, subsectionName, 'too many extras')
    return (tuple(extras), extrasDict)
