Set WshShell = CreateObject("WScript.Shell")
WshShell.Run("""E:\Test\Second_Processing_app\Second_Processing_app.pde""")
WScript.Sleep 7000
WshShell.SendKeys "^+r"
