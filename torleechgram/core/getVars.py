# -*- coding: utf-8 -*-
# Copyright (c) 2021 Priiiyo [priiiyo@github]

from ExecVarsSample import ExecVars
#from ..core.database_handle import TorLeechGramDB
from torleechgram import SessionVars
import os

def get_val(variable):
    return SessionVars.get_var(variable)

