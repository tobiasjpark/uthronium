from tkinter import messagebox
try:
    import sys
    from cx_Freeze import setup, Executable
    build_exe_options = {"excludes": ["turtle"], 'include_files' : ['photos.dat', '5.gif', '6.gif', 'Instructions.gif', 'Resign.gif', 'Rules.gif', 'Donate.gif', 'Accessories.gif', 'storeback.gif', 'tr.gif', 'puzzle.gif', 'frame1.gif', 'frame2.gif', 'frame3.gif', 'hammer.gif', '0p.gif', '1p.gif', '2p.gif', '3p.gif', '4p.gif', '6p.gif', 'frame1.gif', 'frame2.gif', 'frame3.gif', 'whitespace.gif', 'whitespacedon.gif', 'whitespaceacc.gif', 'guest.gif', 'blackspace.gif', 'blackspace2.gif', 'murphy.gif', 'murphypreview.gif', 'cp1.gif', 'cp2.gif', 'cp3.gif', 'cp4.gif', 'cp5.gif', 'cp6.gif', 'cp7.gif', 'cp8.gif', 'cp9.gif','uthronium.ico']}
    
    #bdist_msi_options = {"upgrade_code" : "Vm0jto2Rjkomm2Itqnbounce"}
    base = None
    if sys.platform == "win32":
        base = "Win32GUI"
    setup(  name = "uThronium Final Preview",
            version = "1.0",
            description = "Check out the last preview before the release of uThronium!",
            author="blueberry432",
            author_email = 'emcpark@gmail.com',
            options = {"build_exe": build_exe_options}, #, "bdist_msi" : bdist_msi_options},
            executables = [Executable("uthronium.pyw", shortcutName = "uThronium Final Preview", shortcutDir="DesktopFolder", icon="uThronium.ico", appendScriptToExe=True, base=base)])
except Exception as err:
    messagebox.showerror("Error", "Error: {0}" .format(err))
