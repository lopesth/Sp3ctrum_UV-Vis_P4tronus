# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "2.0.1"

from APP.control_sp3c_p4t import *
from APP.tools.sp3ctrum_gui import *
from tkinter import *


def control_the_flux(choice_interface, file_name):
    program = Sp3ctrum_UVvis_P4tronum(__version__)
    if choice_interface == "-file":
        program.run_fed_terminal(file_name)
    elif choice_interface == "-friendly":
        program.run_friendly_terminal()
    elif choice_interface == "-gui" or choice_interface == "":
        root = Tk()
        root.title("UV-Vis Sp3ctrum P4tronum 2.0")
        app = Application(root)
        mainloop()
    else:
        print("Unrecognized Keyword")
        print("Type -file, -friendly or -gui.")
        sys.exit()


if (__name__ == "__main__"):
    try:
        file_name = sys.argv[2]
        choice_interface = sys.argv[1]
    except:
        file_name = ""
        choice_interface = ""
    control_the_flux(choice_interface, file_name)


