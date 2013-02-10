import Tkinter as tk

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=20, columns=20, size=16, color1="white", color2="white"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[column + self.columns * row] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
imagedata = '''
    R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
    ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
    R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
    P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
    fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
    Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
    e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
    nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
    aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
    +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
    kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
    BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
    yxYYEAA7
'''
antimage = '''R0lGODlhDgAOAHAAACH5BAEAAPwALAAAAAAOAA4AhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAh3APcJFJNJoMBMYgwqEzgpobKFBAUqi1FwHxo0AACgSbgvU4x9FPcRy5hx4aQbBsXEIEkyxo16
BqERg7YiY4yHBnPuu2FTJ8ufP3NmYlkxp7JJxAzYJJZpocB6NzD+FHPDaQxi+8SwTEjsIwCn+1gq
BKAzLFmdAQEAOw=='''

wallimage = '''R0lGODlhDgAOAHAAACH5BAEAAPwALAAAAAAOAA4AhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAgzAN0JHEiwoMGDCBPSE7gwocB2AyG6azjRIEWEEt1ldHhQ4kWOGwXOi8ix5MCPBRduvBgQADs='''

if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    wall = tk.PhotoImage(data=wallimage)

    board.addpiece("wa1", wall, 0,3)
    board.addpiece("wa2", wall, 1,3)
    board.addpiece("wa3", wall, 2,3)
    board.addpiece("wa4", wall, 3,3)
    board.addpiece("wa5", wall, 4,3)
    board.addpiece("wa6", wall, 5,3)
    board.addpiece("wa7", wall, 5,4)
    board.addpiece("wa8", wall, 5,5)
    board.addpiece("wa9", wall, 5,6)
    board.addpiece("wa10", wall, 5,7)
    board.addpiece("wa11", wall, 5,8)
    board.addpiece("wa12", wall, 5,9)
    board.addpiece("wa13", wall, 5,10)
    board.addpiece("wa14", wall, 6,10)
    board.addpiece("wa15", wall, 7,10)
    board.addpiece("wa16", wall, 8,10)
    board.addpiece("wa17", wall, 9,10)
    board.addpiece("wa18", wall, 10,10)
    board.addpiece("wa19", wall, 11,10)
    board.addpiece("wa20", wall, 11,11)
    board.addpiece("wa21", wall, 11,12)
    board.addpiece("wa22", wall, 11,13)
    board.addpiece("wa23", wall, 11,14)
    board.addpiece("wa24", wall, 11,15)
    board.addpiece("wa25", wall, 11,16)
    board.addpiece("wa26", wall, 11,17)
    board.addpiece("wa27", wall, 11,18)
    board.addpiece("wa28", wall, 11,19)

    board.addpiece("wa50", wall, 8,0)
    board.addpiece("wa51", wall, 8,1)
    board.addpiece("wa52", wall, 8,2)
    board.addpiece("wa53", wall, 8,3)
    board.addpiece("wa54", wall, 8,4)
    board.addpiece("wa55", wall, 8,5)
    board.addpiece("wa56", wall, 8,6)
    board.addpiece("wa57", wall, 9,6)
    board.addpiece("wa58", wall, 10,6)
    board.addpiece("wa59", wall, 11,6)
    board.addpiece("wa60", wall, 12,6)
    board.addpiece("wa61", wall, 13,6)
    board.addpiece("wa62", wall, 14,6)
    board.addpiece("wa63", wall, 14,7)
    board.addpiece("wa64", wall, 14,8)
    board.addpiece("wa65", wall, 14,9)
    board.addpiece("wa66", wall, 14,9)
    board.addpiece("wa67", wall, 14,10)
    board.addpiece("wa68", wall, 14,11)
    board.addpiece("wa69", wall, 14,12)
    board.addpiece("wa70", wall, 14,13)
    board.addpiece("wa71", wall, 14,14)
    board.addpiece("wa72", wall, 14,15)
    board.addpiece("wa73", wall, 14,16)
    board.addpiece("wa74", wall, 14,17)
    board.addpiece("wa75", wall, 14,18)
    board.addpiece("wa76", wall, 14,19)

    board2  = [ [] for i in range(20) ]

    i = 0
    while i < 20:
        j = 0
        while j < 20:
            board2[i].append(j)
            j = j + 1
        i = i + 1

    i = 0
    while i < 20:
        j = 0
        while j < 20:
            board2[i][j] = 0
            j = j + 1
        i = i + 1

    board2[0][3] = 1
    board2[1][3] = 1
    board2[2][3] = 1
    board2[3][3] = 1
    board2[4][3] = 1
    board2[5][3] = 1
    board2[5][4] = 1
    board2[5][5] = 1
    board2[5][6] = 1
    board2[5][7] = 1
    board2[5][8] = 1
    board2[5][9] = 1
    board2[5][10] = 1
    board2[6][10] = 1
    board2[7][10] = 1
    board2[8][10] = 1
    board2[9][10] = 1
    board2[10][10] = 1
    board2[11][10] = 1
    board2[11][11] = 1
    board2[11][12] = 1
    board2[11][13] = 1
    board2[11][14] = 1
    board2[11][15] = 1
    board2[11][16] = 1
    board2[11][17] = 1
    board2[11][18] = 1
    board2[11][19] = 1

    board2[8][0] = 1
    board2[8][1] = 1
    board2[8][2] = 1
    board2[8][3] = 1
    board2[8][4] = 1
    board2[8][5] = 1
    board2[8][6] = 1
    board2[9][6] = 1
    board2[10][6] = 1
    board2[11][6] = 1
    board2[12][6] = 1
    board2[13][6] = 1
    board2[14][6] = 1
    board2[14][7] = 1
    board2[14][8] = 1
    board2[14][9] = 1
    board2[14][10] = 1
    board2[14][11] = 1
    board2[14][12] = 1
    board2[14][13] = 1
    board2[14][14] = 1
    board2[14][15] = 1
    board2[14][16] = 1
    board2[14][17] = 1
    board2[14][18] = 1
    board2[14][19] = 1

    antIMG = tk.PhotoImage(data=antimage)

    root.mainloop()