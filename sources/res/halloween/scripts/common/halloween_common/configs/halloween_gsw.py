# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/common/halloween_common/configs/halloween_gsw.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/common/halloween_common/configs/halloween_gsw.py
from __future__ import absolute_import
import typing
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, schemas
from halloween_common.halloween_constants import HALLOWEEN_GSW_PARAMS_KEY
if typing.TYPE_CHECKING:
    from typing import List, Optional

class CardModel(models.Model):
    __slots__ = ('quests', 'visibleByToken')

    def __init__(self, visibleByToken, quests):
        super(CardModel, self).__init__()
        self.visibleByToken = visibleByToken
        self.quests = quests or []


class CardsModel(models.Model):
    __slots__ = ('card', )

    def __init__(self, card):
        super(CardsModel, self).__init__()
        self.card = card


class GSWModel(models.Model):
    __slots__ = ('cards', )

    def __init__(self, cards):
        super(GSWModel, self).__init__()
        self.cards = cards


cardSchema = schemas.Schema(fields={'visibleByToken': (fields.String(required=False, default='')), 
   'quests': (fields.ListFromString(field=fields.String(), required=False))}, modelClass=CardModel, checkUnknown=True)
cardsSchema = schemas.Schema(fields={'card': (fields.List(fieldOrSchema=cardSchema, required=True))}, modelClass=CardsModel, checkUnknown=True)
GSWSchema = GameParamsSchema[GSWModel](gameParamsKey=HALLOWEEN_GSW_PARAMS_KEY, fields={'cards': (fields.Nested(schema=cardsSchema, required=True))}, modelClass=GSWModel, checkUnknown=True, usedInReplay=True)
