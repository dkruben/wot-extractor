# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/frontline_skill_packer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/frontline_skill_packer.py
from __future__ import absolute_import
import typing
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_base_model import SkillBaseModel
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
    from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill

def packBaseSkills(skills, skillsData):
    for skillData in skillsData:
        skill = SkillBaseModel()
        packSkillBaseModel(skill, skillData)
        skills.addViewModel(skill)


def packSkillBaseModel(skill, skillData):
    skillInfo = skillData.getSkillInfo()
    skill.setId(skillData.skillID)
    skill.setIcon(skillInfo.icon)
    skill.setName(skillInfo.name)
