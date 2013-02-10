import Tkinter as tk
import Ant.py

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
        self.pieces[name] = (row, column)
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



if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    player1 = tk.PhotoImage(data=imagedata)

    board.addpiece("wa1", player1, 0,3)
    board.addpiece("wa2", player1, 1,3)
    board.addpiece("wa3", player1, 2,4)
    board.addpiece("wa4", player1, 2,5)
    board.addpiece("wa5", player1, 3,6)
    board.addpiece("wa6", player1, 3,7)
    board.addpiece("wa7", player1, 4,8)
    board.addpiece("wa8", player1, 4,9)
    board.addpiece("wa9", player1, 5,10)
    board.addpiece("wa10", player1, 5,11)
    board.addpiece("wa11", player1, 6,11)
    board.addpiece("wa12", player1, 7,11)
    board.addpiece("wa13", player1, 8,11)
    board.addpiece("wa14", player1, 9,11)
    board.addpiece("wa15", player1, 10,11)
    board.addpiece("wa16", player1, 11,12)
    board.addpiece("wa17", player1, 11,13)
    board.addpiece("wa18", player1, 11,14)
    board.addpiece("wa19", player1, 10,15)
    board.addpiece("wa20", player1, 9,16)
    board.addpiece("wa21", player1, 8,17)
    board.addpiece("wa22", player1, 7,18)
    board.addpiece("wa23", player1, 7,19)


    board.addpiece("wa50", player1, 4,0)
    board.addpiece("wa51", player1, 5,1)
    board.addpiece("wa52", player1, 5,2)
    board.addpiece("wa53", player1, 6,3)
    board.addpiece("wa54", player1, 7,4)
    board.addpiece("wa55", player1, 7,5)
    board.addpiece("wa56", player1, 8,6)
    board.addpiece("wa57", player1, 9,7)
    board.addpiece("wa58", player1, 10,7)
    board.addpiece("wa59", player1, 11,7)
    board.addpiece("wa60", player1, 11,7)
    board.addpiece("wa61", player1, 12,8)
    board.addpiece("wa62", player1, 13,9)
    board.addpiece("wa63", player1, 14,10)
    board.addpiece("wa64", player1, 15,11)
    board.addpiece("wa65", player1, 15,12)
    board.addpiece("wa66", player1, 15,13)
    board.addpiece("wa67", player1, 15,14)
    board.addpiece("wa68", player1, 15,15)
    board.addpiece("wa69", player1, 14,16)
    board.addpiece("wa70", player1, 13,17)
    board.addpiece("wa71", player1, 12,18)
    board.addpiece("wa72", player1, 11,19)



    root.mainloop()