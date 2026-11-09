# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lootbox_system/base/config_parsing.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lootbox_system/base/config_parsing.py
from gui.server_events.bonuses import getNonQuestBonuses

def parseAllOfSection(data):
    slots = {}
    if data:
        for idx, slotsData in enumerate(data):
            probability, bonuses, name = parseSlotSection(slotsData)
            slot = slots.setdefault(idx, {})
            slot.setdefault('probability', probability)
            slot.setdefault('name', name)
            slot.setdefault('bonuses', bonuses)

    return slots


def parseSlotSection(data):
    if isinstance(data, tuple) and len(data) == 4:
        probability, _, _, rawData = data
        name = (rawData.get('properties') or {}).get('name') or ''
        return (
         probability, parseGroupsSection(rawData), name)
    return (
     0, [], '')


def parseGroupsSection(data):
    groups = data.get('groups', [])
    bonuses = []
    for groupData in groups:
        bonuses.extend(parseOneOfSection(groupData))

    return bonuses


def parseOneOfSection(data):
    oneOf = data.get('oneof', ())
    bonuses = []
    if oneOf and len(oneOf) == 2:
        _, items = oneOf
        for item in items:
            if item and len(item) == 4:
                _, _, _, rawData = item
                if rawData:
                    for k, v in rawData.iteritems():
                        if k == 'groups':
                            bonuses.extend(parseGroupsSection(rawData))
                        else:
                            bonuses.extend(getNonQuestBonuses(k, v))

    return bonuses
