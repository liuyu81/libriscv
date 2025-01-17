#
# Copyright 2024 WuXi EsionTech Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import List, Set
# pylint: disable=import-error,no-name-in-module
from riscv import isa
from riscv.disasm import disasm_insn_t
from riscv.processor import insn_desc_t
from .mycsrs import MSCTLR
from .myisas import MyLRSC


# pylint: disable=abstract-method
@isa.register("huimt")
class HuiMtISA(isa.ISA):
    """
    HuiMt-E Extensions to RISC-V ISA
    """

    def __init__(self):
        super().__init__()
        self.lrsc = MyLRSC()

    def get_instructions(self) -> List[insn_desc_t]:
        return [
            *self.lrsc.get_instructions()
        ]

    def get_disasms(self) -> List[disasm_insn_t]:
        return [
            *self.lrsc.get_disasms()
        ]

    def reset(self) -> None:
        super().reset()
        self.lrsc.reset()
        msctlr = MSCTLR(self.p)
        self.p.state.add_csr(msctlr.address, msctlr)
