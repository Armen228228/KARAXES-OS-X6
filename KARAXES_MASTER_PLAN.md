# KARAXES OS X6 — MASTER PROJECT PLAN

**Project:** KARAXES OS X6  
**Base system:** Debian 13 Trixie  
**Architecture:** x86-64  
**Repository:** https://github.com/Armen228228/KARAXES-OS-X6  
**Status:** Initial ISO build and OS architecture development

---

## 1. PROJECT GOAL

Create a fully functional, independent Linux-based operating system named KARAXES OS X6.

The goal is not to create a simple Debian theme. KARAXES must have its own visual identity, desktop shell, system management interface, applications and integrated tools.

The system must be installable and usable on different compatible x86-64 computers.

## 2. VISUAL IDENTITY

Preferred design:
- Black as the primary background.
- Deep crimson red as the main accent.
- Silver for secondary elements.
- Gold for premium highlights.
- Dramatic, luxurious, sophisticated and futuristic appearance.
- Avoid minimalist design and excessive visual clutter.
- Original dragon-head logo inspired by the name Caraxes, without copying existing copyrighted artwork.

The final product name is KARAXES OS X6.

## 3. LANGUAGE AND INPUT

Primary language: Russian.

Additional languages:
- Armenian
- English

Default keyboard layout: English QWERTY.

Optional quick keyboard switching:
- English
- Russian
- Armenian

## 4. LOGIN AND POWER MANAGEMENT

- Password must not be mandatory.
- Automatic login enabled by default.
- Optional password or PIN.
- Optional screen lock.
- Sleep disabled by default.
- Configurable screen-off timer.
- No automatic shutdown by default.
- All power settings must be configurable.

## 5. CUSTOM DESKTOP SHELL

Develop a proprietary KARAXES desktop shell with:

- Custom desktop.
- Custom Dock.
- Custom main menu.
- Custom Control Center.
- Notifications.
- Window management.
- System tray.
- Search.
- Desktop shortcuts.
- Custom icons and animations.
- Consistent visual design across applications.

XFCE may be used as the initial technical desktop foundation, but the final objective is a distinctive KARAXES interface.

## 6. CONTROL CENTER

Two operating modes:

- Standard Mode
- Advanced Mode

The Control Center must include:

1. Hardware Manager
2. Driver Manager
3. Performance Manager
4. Network & Wi-Fi
5. Display & Graphics
6. Sound
7. Storage
8. Security & Privacy
9. Updates & Recovery
10. Personalization

Features:
- Sidebar navigation.
- Search.
- Main settings panel.
- Clear device and system status.
- Advanced controls where appropriate.

## 7. PERFORMANCE MANAGER

Operating modes:

- Gaming
- Performance
- Balanced
- Power Saving

The system must apply only supported and verified settings. Unsupported hardware controls must be identified rather than simulated.

## 8. GAME CENTER

Develop an integrated game management application.

Required functions:
- Installed games library.
- Game installation and download queue.
- Wine compatibility.
- Separate Wine prefixes for individual games.
- Compatibility information.
- Save-game backup and restore.
- Update approval.
- Basic security checks.
- Support for legitimate official and non-official game sources.

No piracy, cracks or DRM circumvention.

## 9. SYSTEM MONITOR

Display:

- Operating system information.
- CPU.
- GPU.
- RAM.
- Storage.
- Motherboard.
- Network.
- Running processes.
- Uptime.
- Available temperature and sensor readings.
- Performance graphs.
- Hardware health alerts.

Missing sensor information must be marked unavailable. Never fabricate measurements.

## 10. HARDWARE AND DRIVER MANAGEMENT

The OS must dynamically detect hardware.

Requirements:
- Automatic hardware identification.
- Driver search through trusted repositories and manufacturer sources.
- Compatibility checks.
- Driver installation.
- Verification after installation.
- Rollback where possible.
- Hardware history.
- Hotplug device detection.
- Unknown or untested hardware clearly identified.

Do not promise universal compatibility without testing.

## 11. HARDWARE TESTING TARGET

Initial development and testing computer:

- Intel H81 motherboard.
- Intel Core i5 CPU (exact model to be confirmed).
- RAM: approximately 8–10 GB (exact amount to be confirmed).
- SSD: approximately 460 GB.
- NVIDIA GTX 550 Ti, 3 GB.
- Windows 10 Pro.
- UEFI available.
- Secure Boot disabled.

Additional hardware:
- LB-LINK BL-WN155A USB Wi-Fi adapter; exact chipset not yet confirmed.

The OS must not be designed exclusively for this computer.

## 12. BOOT AND INSTALLATION

Initial requirements:

- Live USB boot.
- UEFI support.
- Legacy BIOS support where technically possible.
- Hybrid ISO.
- Do not erase or modify the existing Windows installation during initial testing.
- Test the system before considering installation.

Secure Boot is not required in the initial version.

## 13. DEVELOPMENT ARCHITECTURE

Base distribution: Debian 13 Trixie Stable.

Build environment: GitHub Actions.

Repository:
https://github.com/Armen228228/KARAXES-OS-X6

Initial ISO build currently uses a Debian Docker container and live-build.

The first ISO is intended as a technical foundation, not the finished KARAXES OS.

## 14. CURRENT DEVELOPMENT STATUS

Completed:
- Project name selected.
- Main design direction defined.
- Debian 13 selected as the initial base.
- GitHub repository created.
- GitHub Actions workflow created.
- Initial package list defined.
- Several ISO build errors investigated.

Not yet completed:
- Successful ISO build.
- Live USB boot verification.
- Custom KARAXES logo.
- Custom desktop shell.
- Control Center.
- Game Center.
- System Monitor.
- Hardware Manager.
- Driver Manager.
- Final localization.
- Final visual design.

Latest known build issue:
The previous live-build process failed while requesting:

`http://deb.debian.org/debian/dists/trixie/Contents-amd64.gz`

The URL returned HTTP 404.

A new build approach was prepared using a Debian 13 Trixie Docker container instead of the previous Ubuntu-hosted live-build environment.

**The new workflow has not yet been verified.**

## 15. DEVELOPMENT RULES

1. Do not claim that a feature works before it has been tested.
2. Do not make unsupported hardware compatibility promises.
3. Prefer complete replacement files over instructions to edit scattered lines.
4. Keep all project requirements documented here.
5. Record build failures and their actual causes.
6. Avoid unnecessary experiments and random code changes.
7. Preserve the user's Windows installation during initial testing.
8. Use free development tools and GitHub Actions where possible.
9. Do not confuse a Debian-based prototype with the completed KARAXES OS.
10. Keep the project portable across compatible computers.

## 16. NEXT DEVELOPMENT STEPS

Priority order:

1. Achieve a successful ISO build.
2. Download and verify the ISO.
3. Boot it from USB without modifying Windows.
4. Verify hardware detection and basic system functions.
5. Establish the KARAXES visual design system.
6. Develop the original logo and icon set.
7. Build the custom desktop shell.
8. Develop the Control Center.
9. Develop System Monitor and Hardware Manager.
10. Develop Game Center.
11. Improve hardware compatibility and recovery.
12. Test and release a stable version.

## 17. PROJECT CONTINUITY

When continuing this project in a new conversation:

1. Read this document first.
2. Check the current GitHub repository and latest workflow.
3. Identify the latest completed development step.
4. Review the latest build result before modifying code.
5. Update this document whenever an important decision, feature, failure or milestone changes.

**Main objective: Build a real, functional and distinctive KARAXES OS X6 — not merely a customized Debian desktop.**
