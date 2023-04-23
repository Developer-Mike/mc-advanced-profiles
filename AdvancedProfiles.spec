# -*- mode: python ; coding: utf-8 -*-

main_block_cipher = None
main = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("d:/programme/wpy64-3830/python-3.8.3.amd64/lib/site-packages/customtkinter", "customtkinter/"), # Change this to your customtkinter path
        ("assets", "assets/")
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=main_block_cipher,
    noarchive=False,
)
main_pyz = PYZ(main.pure, main.zipped_data, cipher=main_block_cipher)
main_exe = EXE(
    main_pyz,
    main.scripts,
    [],
    exclude_binaries=True,
    name='AdvancedProfiles',
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
    icon=['assets/icon.ico'],
)

interferer_block_cipher = None
interferer = Analysis(
    ['interferer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=interferer_block_cipher,
    noarchive=False,
)
interferer_pyz = PYZ(interferer.pure, interferer.zipped_data, cipher=interferer_block_cipher)
interferer_exe = EXE(
    interferer_pyz,
    interferer.scripts,
    [],
    exclude_binaries=True,
    name='interferer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True, # change to False for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon-interferer.ico'],
)

coll = COLLECT(
    main_exe,
    main.binaries,
    main.zipfiles,
    main.datas,

    interferer_exe,
    interferer.binaries,
    interferer.zipfiles,
    interferer.datas,

    strip=False,
    upx=True,
    upx_exclude=[],
    name='AdvancedProfiles',
)

# Debug
import shutil
shutil.copytree("config", "dist/AdvancedProfiles/config")