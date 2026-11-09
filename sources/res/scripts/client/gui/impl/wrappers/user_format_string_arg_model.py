# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/wrappers/user_format_string_arg_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/user_format_string_arg_model.py
from __future__ import absolute_import
from gui.impl.gen.view_models.common.format_string_arg_model import FormatStringArgModel

class UserFormatStringArgModel(FormatStringArgModel):
    __slots__ = ()

    def __init__(self, value, name='', style=None, align=FormatStringArgModel.ALIGN_LEFT, hardSpace=False):
        super(UserFormatStringArgModel, self).__init__()
        self.setValue(value)
        self.setName(name)
        self.setAlign(align)
        self.setHardSpace(hardSpace)
        if style is not None:
            self.setStyle(style)
        return
