# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\测试文件\\测试工具\\版本控制\\Wjdr\\old\\wjdr_release.py'],
    pathex=[],
    binaries=[],
    #datas=[],
    datas=[('E:\\测试文件\\测试工具\\AirtestIDE\\airtest', 'airtest')],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['E:\\测试文件\\测试工具\\版本控制\\Wjdr\\old\\icon\\log.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
