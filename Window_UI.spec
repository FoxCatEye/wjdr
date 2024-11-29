# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\测试文件\\测试工具\\版本控制\\Wjdr\\new\\main\\Window_UI.py'],
    pathex=[],
    binaries=[],
    datas=[('E:\\main\\even\\Lib\\site-packages\\airtest', 'airtest')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='无尽冬日辅助',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['log.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='脚本2.0.4',
)
