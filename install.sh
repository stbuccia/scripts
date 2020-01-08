#!/bin/bash
chmod 755 script/*
if [[ $(echo $PATH | grep $HOME/.local/bin) ]]; then
    yes | cp -rf script/* $HOME/.local/bin
else 
    yes | cp -rf script/* /usr/bin
fi
