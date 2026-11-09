# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/doc_loaders/messages_panel_reader.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/doc_loaders/messages_panel_reader.py
from __future__ import absolute_import
from helpers import html
import resource_helper
_EXPECTED_STYLES = {'entityStyle': ('fontSize', 'fontFace', 'fontColor')}

def _getDefaultSettings():
    return {'direction': 'up', 
       'lifeTime': 1000, 
       'alphaSpeed': 1000, 
       'maxLinesCount': 5, 
       'poolSettings': (), 
       'textBottomPadding': 0.0, 
       'textRightPadding': 0.0, 
       'useHtml': False, 
       'showUniqueOnly': False, 
       'messageGap': 0}


def _readSettings(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'settings')
    settings = _getDefaultSettings()
    for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(xmlCtx, subSection, 'setting')
        settings[item.name] = item.value

    return settings


def _readStyles(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'styles', safe=True)
    styles = {}
    if section is not None:
        for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(xmlCtx, subSection, 'style')
            expectedKeys = _EXPECTED_STYLES[item.name]
            for key in expectedKeys:
                pass

            styles[item.name] = item.value

    return styles


def _readMessages(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'messages')
    messages = {}
    for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(xmlCtx, subSection, 'message')
        text, aliases = item.value
        aliases = aliases.split(',', 1)
        if len(aliases) == 1:
            aliases *= 2
        messages[item.name] = (html.translation(text), tuple(aliases))

    return messages


_cache = {}

def readXML(path):
    global _cache
    if path in _cache:
        return _cache[path]
    ctx, root = resource_helper.getRoot(path)
    settings = _readSettings(ctx, root)
    styles = _readStyles(ctx, root)
    messages = _readMessages(ctx, root)
    _cache[path] = (
     settings, styles, messages)
    return (
     settings, styles, messages)
