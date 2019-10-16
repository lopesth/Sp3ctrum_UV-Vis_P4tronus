# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

import numpy as np

class Gaussian_Convolution(object):

    def __init__ (self, osc_map, std_wl_cm):
        self.osc_map = osc_map
        self.std_wl = std_wl_cm

    def make_spectrum(self, start, end, number_of_points):
        std_wl_nm = 1 / self.std_wl
        std_wl_cm = np.power(10, 7) / self.std_wl
        A = 2.174*np.power(10, 8)
        self.final_map = {}
        total_map = {}
        epslon_list = []
        osc_list = []

        for wl_ref in self.osc_map.keys():
            for f_i in self.osc_map[wl_ref]:
                osc_list.append(f_i)
                for wl in np.arange(start, end, (end - start)/number_of_points):
                    freq_ref = 1 / wl_ref
                    freq = 1 / wl
                    B = f_i / std_wl_cm
                    C = (np.power(((freq_ref - freq) / std_wl_nm), 2))
                    epslon = A*B*np.exp(-2.7726*C)
                    if wl in total_map.keys():
                        x = total_map[wl]
                        x.append(epslon)
                        total_map.update({wl : x})
                    else:
                        total_map.update({wl:[epslon]})

        for wl in total_map.keys():
            y = 0
            for values_osc_str in total_map[wl]:
                y += values_osc_str
            self.final_map.update({wl : y})
            epslon_list.append(y)

        return [sorted(epslon_list)[-1], sorted(osc_list)[-1]]

    def write_spectrum(self, file_to_write):
        file_target_gauss = open(file_to_write + "_spectrum.dat", "w")
        sorted_keys = sorted(self.final_map.keys())

        for wl in sorted_keys:
            file_target_gauss.write("%10.2f %35.5f\n" %(wl, self.final_map[wl]))
        file_target_gauss.close()

        file_to_write_lits = open(file_to_write + "_rawData.dat", "w")

        for wl_ref in self.osc_map.keys():
            for f_ref in self.osc_map[wl_ref]:
                file_to_write_lits.write("%10.5f %10.5f\n" %(wl_ref, f_ref))
        file_to_write_lits.close()
