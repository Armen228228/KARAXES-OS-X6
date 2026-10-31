
#!/bin/bash
set -euo pipefail

echo "Preparing KARAXES Shell..."

# Add GTK4 and Python dependencies to the Live system
cat >> config/package-lists/karaxes.list.chroot <<'EOF'
python3
python3-gi
gir1.2-gtk-4.0
EOF

# Install KARAXES Shell source
mkdir -p config/includes.chroot/usr/local/bin
mkdir -p config/includes.chroot/usr/share/applications

install -m 755 karaxes-shell.py \
  config/includes.chroot/usr/local/bin/karaxes-shell.py

install -m 644 karaxes-shell.desktop \
  config/includes.chroot/usr/share/applications/karaxes-shell.desktop

echo "KARAXES Shell files prepared successfully."
