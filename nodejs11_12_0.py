#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

y = "y"
x = "x"
ent = input("Tecle (y) para instalar ou (x) para cancelar: ")
if(ent == "y"):
    os.system("sudo apt-get update")
    os.system("sudo apt-get install curl python-software-properties")
    os.system("curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -")
    os.system("sudo apt-get install nodejs-legacy")
    os.system("sudo apt install npm")

else:
    exit()