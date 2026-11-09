# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/helpers/bonuses/optional_bonuses.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/helpers/bonuses/optional_bonuses.py
from __future__ import absolute_import
from future.utils import viewitems
from gui.server_events.bonuses import getNonQuestBonuses

def parseBonusData(data):
    groups = data.get('groups')
    if groups is None or not groups:
        return {}
    oneOfSection = groups[0].get('oneof')
    if oneOfSection is None:
        return {}
    result = {}
    if len(oneOfSection) == 2:
        _, items = oneOfSection
        for item in items:
            if item and len(item) == 4:
                probability, _, _, rawData = item
                if rawData:
                    name = (rawData.get('properties') or {}).get('name') or ''
                    if name:
                        cell = result.setdefault(name, {})
                        cell['probability'] = probability[0]
                        cell['bonuses'] = []
                        for k, v in viewitems(rawData):
                            cell['bonuses'].extend(getNonQuestBonuses(k, v))

    return result
