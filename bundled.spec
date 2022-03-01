# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Python Projects\\gstr-json-2-excel'],
             binaries=[],
             datas=[('images/logo.png', 'gstr-utils-images'), ('images/logo.ico', 'gstr-utils-images'), ('fonts/Roboto-Bold.ttf', 'gstr-utils-fonts'), ('fonts/Roboto-Regular.ttf', 'gstr-utils-fonts')],
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
          name='Gstr Utils',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          version='version.txt',
          icon='D:\\Python Projects\\gstr-json-2-excel\\images\\logo.ico')
