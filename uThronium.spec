# -*- mode: python -*-

block_cipher = None


a = Analysis(['uthronium.pyw'],
             pathex=['c:\\Users\\Tobias\\Documents\\Python\\uthronium'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='uThronium',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='uthronium.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='uThronium')
