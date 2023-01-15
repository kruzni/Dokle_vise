import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "MyExecutable",
    options = {"build_exe": {"packages":["tkinter"], 
                             "include_files":["CrudeBolnica.py","CrudeBolnicaObicanZaposlenik.py",
                                              "CrudeBolnicaZaposlenikSaOvlastima.py", 
                                              "CrudeDarivateljObicanZaposlenik.py","CrudeDarivateljZaposlenikSaOvlastima.py","CrudePrijevoznikObicanZaposlenik.py",
                                              "CrudePrijevoznikZaposlenikSaOvlastima.py", 
                                              "CrudeZaposlenik.py","CrudeZaposlenikObicanZaposlenik.py","CrudeZaposlenikZaposlenikSaOvlastima.py", 
                                              "DarivateljCrude.py","PrijevoznikCrude.py"]}},
    executables = executables
)
