# KARAXES OS X6 — Architecture (initial)

## Layer model
1. **Firmware / boot:** GRUB EFI and legacy BIOS boot path via Debian live-build hybrid media.
2. **Base OS:** Debian 13 Trixie amd64, Linux kernel, systemd, apt/dpkg.
3. **Hardware abstraction:** PCI/USB/sysfs, udev, hwinfo/lshw, lm-sensors, smartmontools, NetworkManager, PipeWire.
4. **Compatibility desktop substrate:** Xorg + Openbox initially. This is a window manager substrate, not the KARAXES desktop identity.
5. **KARAXES Desktop:** custom GTK4 shell, panel, dock, launcher, notifications and Control Center.
6. **System services:** privileged broker(s) with narrow DBus/polkit actions; no shell command execution from untrusted UI strings.
7. **Applications:** Hardware Manager, Driver Manager, Performance Manager, System Monitor, Game Center, Update & Recovery.

## Why Xorg + Openbox first
The first target includes older GPUs and machines. A modest Xorg/Openbox substrate gives broad legacy compatibility while the visible desktop is implemented by KARAXES. A Wayland compositor can be evaluated later after the shell and hardware support mature.

## Service boundaries
- UI processes run unprivileged.
- Read-only hardware inventory is collected from standard system interfaces.
- Any operation that changes packages, drivers, boot settings, disks or power policy must go through a dedicated privileged service with explicit user confirmation and audit logging.
- No arbitrary `sudo` command construction from the UI.

## Planned components
- `karaxes-shell`: desktop shell, launcher, dock, notification surface.
- `karaxes-control`: Standard / Advanced Control Center.
- `karaxes-hw`: hardware inventory and capability probes.
- `karaxes-drivers`: repository and compatibility resolver; install/rollback workflow.
- `karaxes-monitor`: telemetry with explicit unavailable states.
- `karaxes-games`: library, Wine prefixes, backups and update confirmation.
- `karaxes-recovery`: snapshots/restore strategy and recovery environment.
- `karaxes-l10n`: en / ru / hy message catalogs and keyboard layouts.

## Live session defaults
- LightDM autologin is configured for the live account `karaxes` (the live-config account must be created by the live boot process).
- Openbox starts the KARAXES GTK shell through the live user's Openbox autostart file.
- `en_US.UTF-8`, `ru_RU.UTF-8` and `hy_AM.UTF-8` locales are generated; English remains the default in this prototype.
