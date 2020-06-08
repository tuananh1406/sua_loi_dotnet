import os
import subprocess
from shutil import rmtree


duongdan = 'C:\Windows'
tencu = 'SoftwareDistribution'
subprocess.call('sc config "wuauserv" start= demand')
subprocess.call('net stop wuauserv')
duongdanhientai = os.path.abspath('./')
tenfiledotnet = ('dotnet40.exe')
duongdandotnet = os.path.join(duongdanhientai, tenfiledotnet)
sys32 = 'System32'
tep_api = 'api-ms-win-crt-runtime-l1-1-0.dll'
vs64 = 'vc_res64.exe'
vs32 = 'vc_res32.exe'
vcres64 = os.path.join(duongdanhientai, vs64)
vcres32 = os.path.join(duongdanhientai, vs32)

if not os.path.exists(os.path.join(duongdan, sys32, tep_api)):
    try:
        os.environ["PROGRAMFILEX86"]
        subprocess.call('%s /passive' % (vcres64))
    except:
        subprocess.call('%s /passive' % (vcres32))

if os.path.exists(os.path.join(duongdan,tencu)):
    duongdancu = os.path.join(duongdan, tencu)
    if os.path.exists(os.path.join(duongdan, '1234')):
        rmtree(os.path.join(duongdan, '1234'))
    duongdanmoi = os.path.join(duongdan, '1234')
    os.rename(duongdancu, duongdanmoi)
subprocess.call('net start wuauserv')
subprocess.call('%s /passive /promtrestart' % (duongdandotnet))
