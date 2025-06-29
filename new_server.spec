# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\WJDR_Project\\new_server.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
    a.binaries,
    a.datas,
    [],
    name='启动服务器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    #icon='your_icon.ico', # 可选，设置图标
    #version='version.txt', # 可选，设置版本信息文件
    company_name='猫耳', # 可选，设置公司名称
    product_name='猫耳1代', # 可选，设置产品名称
    #copyright='Copyright (c) 2023', # 可选，设置版权信息
    #target_arch=None, # 可选，设置目标架构，例如 'x86_64' 或 'ia32'
    #**{'argv_emulation': False} # 可选，禁用命令行参数模拟（在某些情况下需要）
)
