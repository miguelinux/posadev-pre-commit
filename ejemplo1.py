#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo en posadev
"""

import math
import os


def suma(num1: int, num2: int) -> int:
    res = num1 + num2
    return res


def main():
    """
    Comentario de la función
    """
    print("Pi es:", math.pi)
    print(os.path.exists("/etc/"))  # para saber si estoy en linux
    print("Pi es:", math.pi)

    la_suma = suma(10, 14)

    print(la_suma)


if __name__ == "__main__":
    main()
