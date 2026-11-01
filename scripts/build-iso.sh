#!/usr/bin/env bash
set -Eeuo pipefail
[[ $EUID -eq 0 ]] || { echo "Run with sudo: sudo ./scripts/build-iso.sh" >&2; exit 1; }
command -v lb >/dev/null || { echo "Missing live-build. Install live-build, debootstrap, squashfs-tools, xorriso." >&2; exit 1; }
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
rm -f .build
lb clean --purge || true
lb config --mode debian --distribution trixie --architectures amd64 --binary-images iso-hybrid --archive-areas "main contrib non-free non-free-firmware" --bootappend-live "boot=live components username=karaxes locales=en_US.UTF-8 keyboard-layouts=us" --iso-application "KARAXES OS X6" --iso-volume "KARAXES_X6" --image-name "karaxes-os-x6-amd64"
lb build 2>&1 | tee build.log
ISO="$(find "$ROOT" -maxdepth 1 -type f -name '*.iso' -printf '%T@ %p\n' | sort -nr | head -n1 | cut -d' ' -f2-)"
[[ -n "$ISO" ]] || { echo "Build completed without an ISO output." >&2; exit 2; }
sha256sum "$ISO" | tee "$ISO.sha256"
echo "ISO: $ISO"
