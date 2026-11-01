# KARAXES OS X6 — M3 source package

Premium black / crimson / antique-gold desktop shell on Debian 13 Trixie amd64. The current source uses XFCE for mature window/session services and a custom GTK4 KARAXES shell for its branded home, navigation, dock, diagnostics and system-control launchers.

## Build

On a clean Debian 13 amd64 host or VM (recommended 4 vCPU, 6 GB RAM, 50 GB free disk):

```bash
sudo apt update
sudo apt install -y live-build debootstrap squashfs-tools xorriso git
git clone YOUR_GITHUB_REPOSITORY_URL karaxes-os-x6
cd karaxes-os-x6
sudo ./scripts/build-iso.sh
```

The resulting ISO and `.sha256` file are written to the repository root. Build requires internet access and can take a while.

## First test

Write the ISO to a spare USB drive and boot Live mode. Do not choose install, partition, format or erase during first validation. Test Ethernet, Wi-Fi, audio output/input, display, USB and storage. Run `sudo ./scripts/collect-hardware.sh` and share the report.

## Target PC

Intel i5-4600, 10 GB RAM, 460 GB SSD, NVIDIA GTX 550 Ti 3 GB. LB-LINK Wi-Fi chipset remains unknown and must be identified by USB VID:PID. Initial NVIDIA test is nouveau; Fermi proprietary driver support is not assumed.

## Honest status

M3 is an advanced source milestone, **not a finished or validated ISO**. GTK shell syntax can be checked, but GTK runtime, live-build, Wi-Fi chipset, audio devices and GTX 550 Ti must be tested on hardware. The branded desktop provides live inventory and launches native NetworkManager, PipeWire/PulseAudio, Bluetooth, display and settings tools. Full bespoke Control Center, driver installation/rollback, Game Center, complete translations and recovery UI remain unfinished.
