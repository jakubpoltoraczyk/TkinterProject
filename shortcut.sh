#!/bin/bash

cd shortcut
pyinstaller --onefile update_shortcut.py &> /dev/null
mv dist/update_shortcut ~/Desktop/TkinterProject
cd ..
