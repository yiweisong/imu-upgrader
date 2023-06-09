# -*- mode: python -*-
import sys
import os.path as osp
sys.setrecursionlimit(5000)

block_cipher = None
root_path = os.path.join(os.getcwd(),'src')

a = Analysis([os.path.join(root_path,'bootloader-3.py'),
         ],
         pathex=[root_path],
         binaries=[],
         datas=[
         ],
         hiddenimports=[],
         hookspath=[],
         runtime_hooks=[],
         excludes=[],
         win_no_prefer_redirects=False,
         win_private_assemblies=False,
         cipher=block_cipher,
         noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
         a.scripts,
         a.binaries,
         a.zipfiles,
         a.datas,
         [],
         name='imu-upgrader',
         debug=False,
         bootloader_ignore_signals=False,
         strip=False,
         upx=True,
         upx_exclude=[],
         runtime_tmpdir=None,
         console=True)
