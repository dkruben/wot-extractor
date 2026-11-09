# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/errors.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/errors.py
__revision__ = '$Id$'

class DistutilsError(Exception):
    pass


class DistutilsModuleError(DistutilsError):
    pass


class DistutilsClassError(DistutilsError):
    pass


class DistutilsGetoptError(DistutilsError):
    pass


class DistutilsArgError(DistutilsError):
    pass


class DistutilsFileError(DistutilsError):
    pass


class DistutilsOptionError(DistutilsError):
    pass


class DistutilsSetupError(DistutilsError):
    pass


class DistutilsPlatformError(DistutilsError):
    pass


class DistutilsExecError(DistutilsError):
    pass


class DistutilsInternalError(DistutilsError):
    pass


class DistutilsTemplateError(DistutilsError):
    pass


class DistutilsByteCompileError(DistutilsError):
    pass


class CCompilerError(Exception):
    pass


class PreprocessError(CCompilerError):
    pass


class CompileError(CCompilerError):
    pass


class LibError(CCompilerError):
    pass


class LinkError(CCompilerError):
    pass


class UnknownFileError(CCompilerError):
    pass
