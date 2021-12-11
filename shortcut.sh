#!/bin/bash

cd shortcut
pyinstaller --onefile update_shortcut.py > /dev/null 2>&1
mv dist/update_shortcut ~/Desktop/TkinterProject
cd ..
