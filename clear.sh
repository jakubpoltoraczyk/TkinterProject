#!/bin/bash

files_to_remove="$(find -name __pycache__)"
rm -rf $files_to_remove
