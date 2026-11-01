#!/usr/bin/env bash
set -u
out="${1:-karaxes-hardware-report.txt}"
{ echo "KARAXES OS X6 HARDWARE REPORT"; date -Is; echo; echo "=== OS / KERNEL ==="; cat /etc/os-release 2>/dev/null; uname -a; echo; echo "=== PCI ==="; lspci -nnk 2>&1; echo; echo "=== USB ==="; lsusb 2>&1; echo; echo "=== NETWORK ==="; ip -brief link 2>&1; nmcli device status 2>&1; echo; echo "=== AUDIO ==="; aplay -l 2>&1; arecord -l 2>&1; wpctl status 2>&1; echo; echo "=== STORAGE ==="; lsblk -o NAME,MODEL,SIZE,TYPE,FSTYPE,MOUNTPOINTS 2>&1; echo; echo "=== MEMORY ==="; free -h 2>&1; echo; echo "=== SENSORS ==="; sensors 2>&1; } | tee "$out"
echo "Saved: $out"
