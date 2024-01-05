import tkinter as tk
from tkinter import ttk
from math import *
import numpy as np

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Obciążenie wiatrem wiaty jednospadowej PN-EN 1991-1-4")
        
        # Create Entry Variables
        self.v_b0 = tk.DoubleVar()
        self.v_b0.set(22.0)
        self.v_b0.trace_add('write', self.calculations)        

        self.d = tk.DoubleVar()
        self.d.set(4.11)
        self.d.trace_add('write', self.calculations)

        self.b = tk.DoubleVar()
        self.b.set(0.86)
        self.b.trace_add('write', self.calculations)

        self.h = tk.DoubleVar()
        self.h.set(2.8)
        self.h.trace_add('write', self.calculations)

        self.alpha = tk.DoubleVar()
        self.alpha.set(30.0)
        self.alpha.trace_add('write', self.calculations)

        self.phi = tk.DoubleVar()
        self.phi.set(0.0)
        self.phi.trace_add('write', self.calculations)

        self.t = tk.IntVar()
        self.t.set(25)
        self.t.trace_add('write', self.calculations)

        # Create Entry Lists
        self.terrain_categories = [
            '0',
            'I',
            'II',
            'III',
            'IV',
            # 'Custom peak velocity pressure'
        ]

        self.consequence_classes = [
            'CC1',
            'CC2',
            'CC3'
        ]

        # Create Angle List
        self.angles = [
            0,
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60
        ]

        # Create Frames
        self.frame_input = tk.Frame(root).grid(row=0, column=0)

        # Create Description Labels
        tk.Label(root, text='Kategoria terenu', font=('Segoe UI Variable', 11)).grid(row=0, column=0, sticky='w')
        tk.Label(root, text='Bazowa prędkość wiatru', font=('Segoe UI Variable', 11)).grid(row=1, column=0, sticky='w')
        tk.Label(root, text='Wymiar konstrukcji równoległy do kierunku wiatru', font=('Segoe UI Variable', 11)).grid(row=2, column=0, sticky='w')
        tk.Label(root, text='Szerokość konstrukcji (wymiar powierzchni prostopadłej do kierunku wiatru', font=('Segoe UI Variable', 11)).grid(row=3, column=0, sticky='w')
        tk.Label(root, text='Wysokość wiaty od podłoża do maksymalnego poziomu dachu', font=('Segoe UI Variable', 11)).grid(row=4, column=0, sticky='w')
        tk.Label(root, text='Kąt nachylenia dachu', font=('Segoe UI Variable', 11)).grid(row=5, column=0, sticky='w')
        tk.Label(root, text='Stopień ograniczenia przepływu pod wiatą', font=('Segoe UI Variable', 11)).grid(row=6, column=0, sticky='w')
        tk.Label(root, text='Okres użytkowania konstrukcji', font=('Segoe UI Variable', 11)).grid(row=7, column=0, sticky='w')
        tk.Label(root, text='Charakterystyczne szczytowe ciśnienie prędkości wiatru', font=('Segoe UI Variable', 11)).grid(row=8, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=9, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=10, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=11, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=12, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=13, column=0, sticky='w')
        tk.Label(root, text='Ciśnienie wiatru na powierzchnię zewnętrzną wiaty', font=('Segoe UI Variable', 11)).grid(row=14, column=0, sticky='w')
        tk.Label(root, text='Siła wypadkowa', font=('Segoe UI Variable', 11)).grid(row=15, column=0, sticky='w')
        tk.Label(root, text='Siła wypadkowa', font=('Segoe UI Variable', 11)).grid(row=16, column=0, sticky='w')

        # Create Denotation Labels
        tk.Label(root, text='=', font=('Segoe UI Variable', 15)).grid(row=0, column=1)
        tk.Label(root, text='vb =', font=('Segoe UI Variable', 15)).grid(row=1, column=1)
        tk.Label(root, text='d =', font=('Segoe UI Variable', 15)).grid(row=2, column=1)
        tk.Label(root, text='b =', font=('Segoe UI Variable', 15)).grid(row=3, column=1)
        tk.Label(root, text='h =', font=('Segoe UI Variable', 15)).grid(row=4, column=1)
        tk.Label(root, text='\N{GREEK SMALL LETTER ALPHA} =', font=('Segoe UI Variable', 15)).grid(row=5, column=1)
        tk.Label(root, text='\N{GREEK SMALL LETTER PHI} =', font=('Segoe UI Variable', 15)).grid(row=6, column=1)
        tk.Label(root, text='t =', font=('Segoe UI Variable', 15)).grid(row=7, column=1)
        tk.Label(root, text='qp(ze) =', font=('Segoe UI Variable', 15)).grid(row=8, column=1)
        tk.Label(root, text='wmaxA =', font=('Segoe UI Variable', 15)).grid(row=9, column=1)  
        tk.Label(root, text='wmaxB =', font=('Segoe UI Variable', 15)).grid(row=10, column=1) 
        tk.Label(root, text='wmaxC =', font=('Segoe UI Variable', 15)).grid(row=11, column=1)  
        tk.Label(root, text='wminA =', font=('Segoe UI Variable', 15)).grid(row=12, column=1) 
        tk.Label(root, text='wminB =', font=('Segoe UI Variable', 15)).grid(row=13, column=1)
        tk.Label(root, text='wminC =', font=('Segoe UI Variable', 15)).grid(row=14, column=1)
        tk.Label(root, text='Fwmax =', font=('Segoe UI Variable', 15)).grid(row=15, column=1)
        tk.Label(root, text='Fwmin =', font=('Segoe UI Variable', 15)).grid(row=16, column=1)        

        # Create Entries
        self.combobox_terrain_cat = ttk.Combobox(root, values=self.terrain_categories, font=('Segoe UI Variable', 11))
        self.combobox_terrain_cat.current(3)
        self.combobox_terrain_cat.grid(row=0, column=2)
        self.combobox_terrain_cat.bind('<<ComboboxSelected>>', self.calculations)

        self.entry_vb0 = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.v_b0)
        self.entry_vb0.grid(row=1, column=2)

        self.entry_d = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.d)
        self.entry_d.grid(row=2, column=2)

        self.entry_b = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.b)
        self.entry_b.grid(row=3, column=2)

        self.entry_h = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.h)
        self.entry_h.grid(row=4, column=2)

        self.entry_alpha = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.alpha)
        self.entry_alpha.grid(row=5, column=2)

        self.entry_phi = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.phi)
        self.entry_phi.grid(row=6, column=2)

        entry_t = tk.Entry(root, font=('Segoe UI Variable', 11), textvariable=self.t)
        entry_t.grid(row=7, column=2)

        # Create Unit Labels
        tk.Label(root, text='', font=('Segoe UI Variable', 11)).grid(row=0, column=3)
        tk.Label(root, text='m/s', font=('Segoe UI Variable', 11)).grid(row=1, column=3)
        tk.Label(root, text='m', font=('Segoe UI Variable', 11)).grid(row=2, column=3)
        tk.Label(root, text='m', font=('Segoe UI Variable', 11)).grid(row=3, column=3)
        tk.Label(root, text='m', font=('Segoe UI Variable', 11)).grid(row=4, column=3)
        tk.Label(root, text='\N{DEGREE SIGN}', font=('Segoe UI Variable', 11)).grid(row=5, column=3)
        tk.Label(root, text='', font=('Segoe UI Variable', 11)).grid(row=6, column=3)
        tk.Label(root, text='lat(a)', font=('Segoe UI Variable', 11)).grid(row=7, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=8, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=9, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=10, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=11, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=12, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=13, column=3)
        tk.Label(root, text='kN/m2', font=('Segoe UI Variable', 11)).grid(row=14, column=3)
        tk.Label(root, text='kN', font=('Segoe UI Variable', 11)).grid(row=15, column=3)
        tk.Label(root, text='kN', font=('Segoe UI Variable', 11)).grid(row=16, column=3)

        # Create Result Labels        
        self.q_p = tk.DoubleVar()
        self.label_q_p = tk.Label(root, text=self.q_p, font=('Segoe UI Variable', 20), textvariable=self.q_p).grid(row=8, column=2)

        self.w_maxA = tk.DoubleVar()
        self.label_w_maxA = tk.Label(root, text=self.w_maxA, font=('Segoe UI Variable', 20), textvariable=self.w_maxA).grid(row=9, column=2)

        self.w_maxB = tk.DoubleVar()
        self.label_w_maxB = tk.Label(root, text=self.w_maxB, font=('Segoe UI Variable', 20), textvariable=self.w_maxB).grid(row=10, column=2)

        self.w_maxC = tk.DoubleVar()
        self.label_w_maxC = tk.Label(root, text=self.w_maxC, font=('Segoe UI Variable', 20), textvariable=self.w_maxC).grid(row=11, column=2)

        self.w_minA = tk.DoubleVar()
        self.label_w_minA = tk.Label(root, text=self.w_minA, font=('Segoe UI Variable', 20), textvariable=self.w_minA).grid(row=12, column=2)

        self.w_minB = tk.DoubleVar()
        self.label_w_minB = tk.Label(root, text=self.w_minB, font=('Segoe UI Variable', 20), textvariable=self.w_minB).grid(row=13, column=2)

        self.w_minC = tk.DoubleVar()
        self.label_w_minC = tk.Label(root, text=self.w_minC, font=('Segoe UI Variable', 20), textvariable=self.w_minC).grid(row=14, column=2)  

        self.F_wmax = tk.DoubleVar()
        self.label_F_wmax = tk.Label(root, text=self.F_wmax, font=('Segoe UI Variable', 20), textvariable=self.F_wmax).grid(row=15, column=2)

        self.F_wmin = tk.DoubleVar()
        self.label_F_wmin = tk.Label(root, text=self.F_wmin, font=('Segoe UI Variable', 20), textvariable=self.F_wmin).grid(row=16, column=2)     
        
        #################################
        # Net Wind Pressure Calculation #
        #################################

    def calculations(self, *args):
        
        # Assign Entry Data
        v_b0 = self.v_b0.get()
        d = self.d.get()
        b = self.b.get()
        z = self.h.get()
        alpha = self.alpha.get()
        phi = self.phi.get()
        t = self.t.get()
        terrain_cat = self.combobox_terrain_cat.current()

        c_dir = 1.0
        c_season = 1.0
        p = 1/t
        K = 0.2
        n = 0.5
        c_prob = ((1-K*log(-log(1-p)))/(1-K*log(-log(0.98))))**n        
        v_b = c_dir*c_season*v_b0*c_prob

        z_0_list = [
            0.003,
            0.01,
            0.05,
            0.3,
            1.0
        ]

        z_min_list = [
            1,
            1,
            2,
            5,
            10
        ]

        z_max_list = [
            200,
            200,
            300,
            400,
            500
        ]

        z_0 = z_0_list[terrain_cat]
        z_min = z_min_list[terrain_cat]
        z_max = z_max_list[terrain_cat]

        k_r = 0.19 * (z_0 / 0.05)**0.07

        if z_min <= z <= z_max:
            c_r = k_r * log(z / z_0)
        elif z < z_min:
            c_r = k_r * log(z_min / z_0)
        
        c_0 = 1.0
        v_m = c_r*c_0*v_b
        k_1 = 1.0

        if z_min <= z <= z_max:
            I_v = k_1 / (c_0 * log(z / z_0))
        elif z < z_min:
            I_v = k_1 / (c_0 * log(z_min / z_0))
        
        rho = 1.25

        q_p = (1 + 7 * I_v) * 1 / 2 * rho * v_m**2 / 1000
        self.q_p.set(round(q_p, 3))        

        c_pnetmax_table = [
            [0.5, 1.8, 1,1],
            [0.8, 2.1, 1.3],
            [1.2, 2.4, 1.6],
            [1.4, 2.7, 1.8],
            [1.7, 2.9, 2.1],
            [2.0, 3.1, 2.3],
            [2.2, 3.2, 2.4],
            [2.5, 3.3, 2.7],
            [2.8, 3.4, 2.9],
            [3.1, 3.5, 3.2],
            [3.4, 3.6, 3.4],
            [3.7, 3.7, 3.6],
            [4.0, 3.9, 3.8]
        ]

        c_pnetmin0_table = [
            [-0.6, -1.6, -1.4],
            [-1.1, -1.7, -1.8],
            [-1.5, -2.0, -2.1],
            [-1.8, -2.4, -2.5],
            [-2.2, -2.8, -2.9],
            [-2.6, -3.2, -3.2],
            [-3.0, -3.8, -3.6],
            [-3.4, -4.1, -4.0],
            [-3.8, -4.5, -4.3],
            [-4.2, -4.9, -4.7],
            [-4.6, -5.3, -5.0],
            [-4.9, -5.6, -5.4],
            [-5.3, -6.0, -5.8]
        ]

        c_pnetmin1_table = [
            [-1.5, -1.8, -2.2],
            [-1.6, -2.2, -2.5],
            [-2.1, -2.6, -2.7],
            [-1.6, -2.9, -3.0],
            [-1.6, -2.9, -3.0],
            [-1.5, -2.5, -2.8],
            [-1.5, -2.2, -2.7],
            [-1.5, -2.3, -2.8],
            [-1.5, -2.4, -2.9],
            [-1.4, -2.4, -3.0],
            [-1.4, -2.5, -3.0],
            [-1.4, -2.6, -3.1],
            [-1.4, -2.7, -3.2]
        ]

        # Interpolation between phi values
        
        rows = len(c_pnetmin0_table)
        cols = 3

        c_pnetmin_table = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                c_pnetmin_table[i][j] = (c_pnetmin1_table[i][j]-c_pnetmin0_table[i][j]) * phi + c_pnetmin0_table[i][j]



        # Get vertical columns (for A, B, C zones respectively) from cpnet tables
        c_pnetmaxA_list = self.get_column_from_table(c_pnetmax_table, 0)
        c_pnetmaxB_list = self.get_column_from_table(c_pnetmax_table, 1)
        c_pnetmaxC_list = self.get_column_from_table(c_pnetmax_table, 2)
        c_pnetminA_list = self.get_column_from_table(c_pnetmin_table, 0)
        c_pnetminB_list = self.get_column_from_table(c_pnetmin_table, 1)
        c_pnetminC_list = self.get_column_from_table(c_pnetmin_table, 2)

        # Interpolation between angle values
        c_pnetmaxA = np.interp(alpha, self.angles, c_pnetmaxA_list)
        c_pnetmaxB = np.interp(alpha, self.angles, c_pnetmaxB_list)
        c_pnetmaxC = np.interp(alpha, self.angles, c_pnetmaxC_list)        
        c_pnetminA = np.interp(alpha, self.angles, c_pnetminA_list)
        c_pnetminB = np.interp(alpha, self.angles, c_pnetminB_list)
        c_pnetminC = np.interp(alpha, self.angles, c_pnetminC_list)

        # Calculate w_max
        w_maxA = q_p*c_pnetmaxA
        w_maxB = q_p*c_pnetmaxB
        w_maxC = q_p*c_pnetmaxC
        w_minA = q_p*c_pnetminA
        w_minB = q_p*c_pnetminB
        w_minC = q_p*c_pnetminC

        # Set w_max Label variables
        self.w_maxA.set(round(w_maxA, 3))
        self.w_maxB.set(round(w_maxB, 3))
        self.w_maxC.set(round(w_maxC, 3))
        self.w_minA.set(round(w_minA, 3))
        self.w_minB.set(round(w_minB, 3))
        self.w_minC.set(round(w_minC, 3))

        ################################
        # Total wind force calculation #
        ################################

        c_fmax_list = [
            0.2,
            0.4,
            0.5,
            0.7,
            0.8,
            1.0,
            1.2,
            1.4,
            1.5,
            1.7,
            1.8,
            2.0,
            2.1
        ]

        c_fmin0_list = [
            -0.5,
            -0.7,
            -0.9,
            -1.1,
            -1.3,
            -1.6,
            -1.8,
            -2.0,
            -2.2,
            -2.4,
            -2.7,
            -2.9,
            -3.1
        ]

        c_fmin1_list = [
            -1.3,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.4,
            -1.5,
            -1.5
        ]

        c_fmin_list = []
        for i in range(len(c_fmin0_list)):
            c_fmin_list.append((c_fmin1_list[i] - c_fmin0_list[i]) * phi + c_fmin0_list[i])

        c_fmax = np.interp(alpha, self.angles, c_fmax_list)
        c_fmin = np.interp(alpha, self.angles, c_fmin_list)        

        A_ref = b * d / cos(radians(alpha))

        cscd = 1.0

        F_wmax = cscd * c_fmax * q_p * A_ref
        F_wmin = cscd * c_fmin * q_p * A_ref        

        self.F_wmax.set(round(F_wmax, 3))
        self.F_wmin.set(round(F_wmin, 3))

        ##############################
        # Friction force calculation #
        ##############################


                
    def get_column_from_table(self, table, col):
        c_pnet = []
        for i in range(len(table)):
            c_pnet.append(table[i][col])
        return c_pnet       
        
        


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = Application(root)    
    app.mainloop()
