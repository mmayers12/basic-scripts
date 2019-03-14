#!/bin/bash

#unmount the problem drives
sudo umount /dev/sdc1
sudo umount /dec/sdd1

# Fix whatever garbage lock windows puts on them
sudo ntfsfix /dev/sdc1
sudo ntfsfix /dev/sdd1

# Remount drives
sudo mount -a
