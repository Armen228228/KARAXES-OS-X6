#!/usr/bin/python3
"""KARAXES OS X6 — M3 premium desktop shell. Real controls, honest diagnostics."""
import os, re, shutil, subprocess, datetime
import gi
gi.require_version('Gtk','4.0')
from gi.repository import Gtk, GLib, Gdk
APP='KARAXES OS X6'
CSS=b"""
* { font-family: 'Noto Sans', sans-serif; }
window { background: #09090d; color: #eee9e8; }
.top { background: #101015; border-bottom: 1px solid #64202a; padding: 9px 16px; }
.brand { color: #e7c982; font-weight: 900; letter-spacing: 3px; }
.subbrand { color: #89858c; font-size: 10px; letter-spacing: 2px; }
.panel { background: linear-gradient(145deg,#1a171c,#111116); border: 1px solid #3d3036; border-radius: 15px; padding: 16px; }
.panel:hover { border-color: #87404a; }
.gold { color: #d8bb78; } .red { color: #e05a65; }
.muted { color: #a7a0a6; } .metric { color: #f0dadd; font-size: 23px; font-weight: 800; }
.nav { background: #111116; border: 1px solid #30262d; border-radius: 15px; padding: 12px; }
.nav button { text-align: left; background: transparent; border: 1px solid transparent; color: #d9d3d6; padding: 11px; }
.nav button:hover, .nav button:checked { background: #351820; border-color: #75303d; color: #fff; }
button { background: #28232a; color: #f2e9eb; border: 1px solid #51404a; border-radius: 9px; padding: 8px 12px; }
button:hover { background: #46202a; border-color: #a34b58; }
entry { background: #211d24; color: white; border: 1px solid #58434d; border-radius: 9px; padding: 8px; }
.hero { background: linear-gradient(115deg,#211017,#111117 55%,#251a1d); border: 1px solid #63303b; border-radius: 19px; padding: 24px; }
.hero-title { font-size: 30px; font-weight: 900; color: #f2dfe0; }
.pill { background: #351b23; border: 1px solid #753642; border-radius: 20px; padding: 5px 10px; color: #e9c7cb; }
.dock { background: #151219; border: 1px solid #4a343d; border-radius: 18px; padding: 8px; }
.dock button { min-width: 48px; min-height: 44px; font-size: 18px; background: #211b23; }
.section-title { font-size: 25px; font-weight: 850; color: #f0d6d8; }
.warning { color: #e6c27d; }
"""

def run(args, timeout=5):
    try:
        x=subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return (x.stdout or '').strip() if x.returncode==0 else ((x.stderr or x.stdout or '').strip() or 'Unavailable')
    except Exception as e: return 'Unavailable'
def read(path, default='Unavailable'):
    try: return open(path,encoding='utf-8',errors='replace').read().strip() or default
    except OSError: return default
def cpu():
    s=read('/proc/cpuinfo','')
    for line in s.splitlines():
        if line.lower().startswith('model name'): return line.split(':',1)[1].strip()
    return 'Unavailable'
def mem():
    d={}
    for line in read('/proc/meminfo','').splitlines():
        m=re.match(r'(MemTotal|MemAvailable):\s+(\d+)',line)
        if m:d[m.group(1)]=int(m.group(2))
    if len(d)<2:return 'Unavailable'
    t,a=d['MemTotal'],d['MemAvailable'];return f'{(t-a)/1048576:.1f} / {t/1048576:.1f} GB'
def state(cmd, default='Unavailable'): return run(cmd) if shutil.which(cmd[0]) else default
class Shell(Gtk.Application):
 def __init__(self):
  super().__init__(application_id='org.karaxes.osx6');self.page='Home';self.nav={};self.stack=None;self.clock=None;self.status=None
 def do_activate(self):
  prov=Gtk.CssProvider();prov.load_from_data(CSS);Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),prov,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
  self.win=Gtk.ApplicationWindow(application=self,title=APP);self.win.set_default_size(1440,900);self.win.set_size_request(1050,680);self.win.maximize()
  outer=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0);self.win.set_child(outer)
  top=Gtk.Box(spacing=12);top.add_css_class('top');outer.append(top)
  dragon=Gtk.Label(label='♜');dragon.add_css_class('gold');top.append(dragon)
  brandbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0);top.append(brandbox)
  b=Gtk.Label(label='KARAXES');b.add_css_class('brand');brandbox.append(b);s=Gtk.Label(label='SOVEREIGN INTERFACE  /  X6');s.add_css_class('subbrand');brandbox.append(s)
  top.append(Gtk.Box(hexpand=True))
  self.net=Gtk.Label(label='◉ NET');self.net.add_css_class('muted');top.append(self.net)
  self.sound=Gtk.Label(label='♫ AUDIO');self.sound.add_css_class('muted');top.append(self.sound)
  self.clock=Gtk.Label();self.clock.add_css_class('gold');top.append(self.clock)
  body=Gtk.Box(spacing=16);body.set_margin_top(16);body.set_margin_bottom(12);body.set_margin_start(16);body.set_margin_end(16);body.set_vexpand(True);outer.append(body)
  side=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5);side.add_css_class('nav');side.set_size_request(205,-1);body.append(side)
  st=Gtk.Label(label='COMMAND DECK',xalign=0);st.add_css_class('gold');side.append(st)
  for name,ico in [('Home','⌂'),('Control Center','◈'),('Hardware','▦'),('Drivers','⚙'),('Performance','⌁'),('System Monitor','▥'),('Game Center','▶'),('Settings','✧')]:
   bt=Gtk.Button(label=f'{ico}   {name}');bt.connect('clicked',lambda _b,n=name:self.show(n));side.append(bt);self.nav[name]=bt
  side.append(Gtk.Box(vexpand=True));self.status=Gtk.Label(label='LIVE SESSION  •  SAFE MODE',xalign=0,wrap=True);self.status.add_css_class('muted');side.append(self.status)
  self.stack=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=14);self.stack.set_hexpand(True);body.append(self.stack)
  bottom=Gtk.Box();bottom.set_halign(Gtk.Align.CENTER);bottom.add_css_class('dock');outer.append(bottom)
  for label,cmd,ico in [('Files','thunar','▤'),('Browser','firefox-esr','◎'),('Terminal','xfce4-terminal','>_'),('Network','nm-connection-editor','◉'),('Sound','pavucontrol','♫'),('Settings','xfce4-settings-manager','⚙')]:
   bt=Gtk.Button(label=ico);bt.set_tooltip_text(label);bt.connect('clicked',lambda _b,c=cmd:self.launch(c));bottom.append(bt)
  self.show('Home');self.tick();GLib.timeout_add_seconds(2,self.tick);self.win.present()
 def clear(self):
  c=self.stack.get_first_child()
  while c:n=c.get_next_sibling();self.stack.remove(c);c=n
 def heading(self,title,desc=''):
  h=Gtk.Label(label=title,xalign=0);h.add_css_class('section-title');self.stack.append(h)
  if desc:
   l=Gtk.Label(label=desc,xalign=0,wrap=True);l.add_css_class('muted');self.stack.append(l)
 def card(self,title,value,detail=''):
  b=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=7);b.add_css_class('panel');b.set_hexpand(True)
  a=Gtk.Label(label=title.upper(),xalign=0);a.add_css_class('gold');b.append(a)
  v=Gtk.Label(label=value,xalign=0,wrap=True);v.add_css_class('metric');b.append(v)
  if detail:
   d=Gtk.Label(label=detail,xalign=0,wrap=True);d.add_css_class('muted');b.append(d)
  return b
 def row(self,*widgets):
  r=Gtk.Box(spacing=12);r.set_homogeneous(True)
  for w in widgets:r.append(w)
  self.stack.append(r);return r
 def note(self,title,body):
  b=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5);b.add_css_class('panel')
  h=Gtk.Label(label=title,xalign=0);h.add_css_class('gold');b.append(h)
  d=Gtk.Label(label=body,xalign=0,wrap=True,selectable=True);d.add_css_class('muted');b.append(d);self.stack.append(b);return b
 def action(self,title,desc,callback):
  r=Gtk.Box(spacing=12);r.add_css_class('panel');r.set_hexpand(True)
  v=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=4);v.set_hexpand(True);r.append(v)
  t=Gtk.Label(label=title,xalign=0);t.add_css_class('gold');v.append(t)
  d=Gtk.Label(label=desc,xalign=0,wrap=True);d.add_css_class('muted');v.append(d)
  bt=Gtk.Button(label='OPEN / CONTROL');bt.connect('clicked',lambda _b:callback());r.append(bt);self.stack.append(r)
 def launch(self,cmd):
  if shutil.which(cmd):subprocess.Popen([cmd],start_new_session=True)
  else:self.note('Not installed',f'{cmd} is not available in this build.')
 def show(self,name):
  self.page=name;self.clear()
  for k,b in self.nav.items():b.set_sensitive(k!=name)
  if name=='Home':
   hero=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=9);hero.add_css_class('hero')
   tag=Gtk.Label(label='THE DRAGON AWAKENS  •  X6 DEVELOPMENT BUILD',xalign=0);tag.add_css_class('gold');hero.append(tag)
   title=Gtk.Label(label='POWER IN YOUR HANDS',xalign=0);title.add_css_class('hero-title');hero.append(title)
   desc=Gtk.Label(label='A sovereign desktop built around your hardware. Diagnostics are live; unsupported capabilities are never fabricated.',xalign=0,wrap=True);desc.add_css_class('muted');hero.append(desc);self.stack.append(hero)
   self.row(self.card('Processor',cpu(),'Kernel-reported CPU'),self.card('Memory',mem(),'Used / total'),self.card('Kernel',run(['uname','-r']),'Running kernel'))
   self.row(self.card('Network',run(['nmcli','-t','-f','STATE','general']) if shutil.which('nmcli') else 'Unavailable','NetworkManager status'),self.card('Audio',run(['wpctl','status'])[:100] if shutil.which('wpctl') else 'Unavailable','PipeWire status'))
   self.note('System integrity','Live session. Disk formatting and installation are not launched from the desktop. First boot should be tested from USB.')
   self.action('Quick settings','Open real network, sound and display controls.',lambda:self.show('Control Center'))
  elif name=='Control Center':
   self.heading('Control Center','Standard controls use the installed Linux services. Advanced configuration opens native tools.')
   self.action('Wi-Fi & Network','View connections and configure Wi-Fi / Ethernet.',lambda:self.launch('nm-connection-editor'))
   self.action('Sound','Select output/input devices and adjust volume.',lambda:self.launch('pavucontrol'))
   self.action('Bluetooth','Manage paired devices.',lambda:self.launch('blueman-manager'))
   self.action('Display','Resolution, refresh rate and monitor layout.',lambda:self.launch('xfce4-display-settings'))
   self.action('Power & Performance','Power profiles and session options.',lambda:self.launch('xfce4-power-manager-settings'))
   self.action('Keyboard & Language','Keyboard layout and input configuration.',lambda:self.launch('xfce4-keyboard-settings'))
   self.action('System settings','Open native settings manager.',lambda:self.launch('xfce4-settings-manager'))
   self.note('Advanced tools','Native system tools are used here; a bespoke settings backend and unified Control Center are still under development.')
  elif name=='Hardware':
   self.heading('Hardware Intelligence','Live inventory collected from kernel and standard diagnostic utilities.')
   self.note('CPU',cpu());self.note('Memory',mem());self.note('PCI devices',run(['lspci','-nnk']));self.note('USB devices',run(['lsusb']));self.note('Storage',run(['lsblk','-o','NAME,MODEL,SIZE,TYPE,FSTYPE,MOUNTPOINTS']));self.note('Audio devices',run(['sh','-c','aplay -l 2>&1; echo; arecord -l 2>&1']));self.note('Network devices',run(['sh','-c','ip -brief link; echo; nmcli device status 2>&1']))
  elif name=='Drivers':
   self.heading('Driver Intelligence','Detection and verification first. No unverified third-party driver installation.')
   self.note('Kernel driver binding',run(['lspci','-nnk']));self.note('Firmware packages','Debian non-free-firmware and common Intel / Realtek / Atheros / Broadcom firmware are included where available.')
   self.note('GTX 550 Ti','NVIDIA Fermi generation. Initial test uses kernel nouveau where supported. Proprietary legacy driver is not assumed compatible with the installed kernel/Xorg.')
   self.note('LB-LINK Wi-Fi','Chipset is unknown. Run the hardware report and identify USB VID:PID before choosing firmware or driver.')
  elif name=='Performance':
   self.heading('Performance','Only exposed kernel and service data is shown. No artificial speed promises.')
   self.note('Load average',read('/proc/loadavg'));self.note('CPU frequency',run(['sh','-c','cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null || echo Unavailable']));self.note('Power profiles',run(['powerprofilesctl','list']));self.note('GPU',run(['sh','-c','lspci -nnk | grep -A4 -Ei "VGA|3D|Display"']))
  elif name=='System Monitor':
   self.heading('System Monitor','Refreshes automatically. Missing sensors are explicitly reported as unavailable.')
   cards=[self.card('Load average',read('/proc/loadavg').split()[0],'1 minute'),self.card('Memory',mem(),'Used / total'),self.card('Root disk',run(['sh','-c',"df -hP / | awk 'NR==2 {print $3 \" / \" $2 \" (\" $5 \")\"}'"]),'Filesystem'),self.card('Temperature',self.temps(),'Thermal zones')];self.row(*cards)
   proc=self.note('Top processes',run(['sh','-c','ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 12']))
   def refresh():
    if self.page!='System Monitor':return False
    vals=[read('/proc/loadavg').split()[0],mem(),run(['sh','-c',"df -hP / | awk 'NR==2 {print $3 \" / \" $2 \" (\" $5 \")\"}'"]),self.temps()]
    for c,v in zip(cards,vals):c.get_first_child().get_next_sibling().set_text(v)
    return True
   GLib.timeout_add_seconds(3,refresh)
  elif name=='Game Center':
   self.heading('Game Center','A safe launcher and compatibility workspace.')
   self.action('Steam','Launch Steam if installed.',lambda:self.launch('steam'))
   self.action('Wine configuration','Open Wine configuration if installed.',lambda:self.launch('winecfg'))
   self.note('Compatibility','Per-game prefixes, compatibility database, backups and game update confirmation are not implemented yet. No piracy or DRM bypass.')
  elif name=='Settings':
   self.heading('System Settings','Session, language, privacy and personalization.')
   self.note('Languages','English / Russian / Armenian locales are configured as available. Full translation coverage remains in progress.')
   self.note('Sign-in','Live session automatic login. Password/PIN and screen-lock behavior must be configured before a persistent install.')
   self.note('Sleep','Sleep defaults disabled by project specification; use native power manager to configure behavior.')
   self.action('Appearance','Open appearance settings.',lambda:self.launch('xfce4-appearance-settings'))
   self.action('Keyboard','Open keyboard settings.',lambda:self.launch('xfce4-keyboard-settings'))
 def temps(self):
  out=[]
  try:
   for n in os.listdir('/sys/class/thermal'):
    if n.startswith('thermal_zone'):
     x=read('/sys/class/thermal/'+n+'/temp','')
     if x.isdigit():out.append(f'{int(x)/1000:.1f} °C')
  except OSError:pass
  return ', '.join(out) if out else 'Unavailable'
 def tick(self):
  self.clock.set_text(datetime.datetime.now().strftime('%a  %d %b   %H:%M'))
  ns=run(['nmcli','-t','-f','STATE','general']) if shutil.which('nmcli') else 'Unavailable'
  self.net.set_text('◉ '+('ONLINE' if 'connected' in ns.lower() else 'NETWORK'))
  self.sound.set_text('♫ AUDIO' if shutil.which('wpctl') else '♫ AUDIO N/A')
  return True
if __name__=='__main__':Shell().run(None)
