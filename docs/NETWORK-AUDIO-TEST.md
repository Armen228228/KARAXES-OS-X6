# Network and audio validation

The image includes NetworkManager, wpa_supplicant, PipeWire/WirePlumber, ALSA tools and common Debian firmware packages. This improves hardware coverage; it does not guarantee every adapter works.

Identify the exact Wi-Fi USB chipset and audio controller. In a Linux live session run:

```bash
lspci -nnk
lsusb
cat /proc/asound/cards
rfkill list
sudo dmesg | grep -iE 'firmware|failed to load|Direct firmware load'
```

After booting KARAXES Live USB:

```bash
nmcli device status
nmcli radio wifi
wpctl status
aplay -l
/usr/local/sbin/karaxes-hardware-report
```

If Wi-Fi is absent, capture `lsusb -nn` and firmware-related `dmesg`. If audio is absent, capture `lspci -nnk`, `/proc/asound/cards`, `wpctl status`, and `dmesg`. Do not claim support until the target adapter/controller passes a real test.
