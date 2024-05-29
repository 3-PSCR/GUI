import tkinter as tk
from tkinter import font
import time
start = time.time()
x = 1000
y = 650
from serialcom import board

class GUISet():

    def labelSegs(self, segCents):
        
        # Define segment label array
        segLabs = [
            tk.Label(text="Segment 1", font=font.Font(weight="bold")),
            tk.Label(text="Segment 2", font=font.Font(weight="bold")),
            tk.Label(text="Segment 3", font=font.Font(weight="bold"))
            ]
        
        # Define segment status array
        self.segInfo = [
            tk.Label(text="S1"),
            tk.Label(text="S2"),
            tk.Label(text="S3")
        ]

        # Define nested chamber label array
        self.chamLabs = [
            [
                tk.Label(text="CH1"),
                tk.Label(text="CH2"),
                tk.Label(text="CH3"),
            ],
            [
                tk.Label(text="CH4"),
                tk.Label(text="CH5"),
                tk.Label(text="CH6"),
            ],
            [
                tk.Label(text="CH7"),
                tk.Label(text="CH8"),
                tk.Label(text="CH9"),
            ]
        ]

        # Draw labels to window
        for i in range(3):
            segCent = segCents[i] # Centre of current segment

            segLabs[i].place(x = segCent[0]-150, y = segCent[1] - 12, anchor = "center")
            self.segInfo[i].place(x = segCent[0]-150, y = segCent[1] + 12, anchor = "center")

            self.chamLabs[i][0].place(x = segCent[0], y = segCent[1] - 70, anchor = "center")
            self.chamLabs[i][1].place(x = segCent[0] + 80, y = segCent[1] + 40, anchor = "center")
            self.chamLabs[i][2].place(x = segCent[0] - 80, y = segCent[1] + 40, anchor = "center")

    def labelTabsGeneric(self, tabTLs):
        starter = 1
        
        for tabTL in tabTLs:
            tk.Label(
                text="SetP",
                font=font.Font(weight="bold")
                ).place(x = tabTL[0] + 66, y = tabTL[1], anchor = "s")
            tk.Label(
                text="Update",
                font=font.Font(weight="bold")
                ).place(x = tabTL[0] + 121, y = tabTL[1], anchor = "s")
            tk.Label(
                text=str(starter),
                font=font.Font(weight="bold", size=10),
                # height=0.9
                ).place(x = tabTL[0] + 19, y = tabTL[1] + 2, anchor = "n")
            tk.Label(
                text=str(starter + 1),
                font=font.Font(weight="bold", size=10),
                # height=0.9
                ).place(x = tabTL[0] + 19, y = tabTL[1] + 23, anchor = "n")
            tk.Label(
                text=str(starter + 2),
                font=font.Font(weight="bold", size=10),
                # height=0.9
                ).place(x = tabTL[0] + 19, y = tabTL[1] + 44, anchor = "n")
            starter += 3

    def labelTabs(self, tabTLs):

        # Create array of set pressure labels
        self.tabSPs = [
            [
                tk.Label(text="SP11",font=font.Font(size=10)),
                tk.Label(text="SP12",font=font.Font(size=10)),
                tk.Label(text="SP13",font=font.Font(size=10))
            ],
            [
                tk.Label(text="SP21",font=font.Font(size=10)),
                tk.Label(text="SP22",font=font.Font(size=10)),
                tk.Label(text="SP23",font=font.Font(size=10))
            ],
            [
                tk.Label(text="SP31",font=font.Font(size=10)),
                tk.Label(text="SP32",font=font.Font(size=10)),
                tk.Label(text="SP33",font=font.Font(size=10))
            ]
        ]

        # Create array of new pressure entries
        self.tabNPs = [
            [
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5)
            ],
            [
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5)
            ],
            [
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5),
                tk.Entry(font=font.Font(size=6), width=5)
            ]
        ]

        # Create array of copy buttons
        tabButs = [
            tk.Button(text="Copy", font=font.Font(size=10), command=lambda:self.copy(1)),
            tk.Button(text="Copy", font=font.Font(size=10), command=lambda:self.copy(2)),
            tk.Button(text="Copy", font=font.Font(size=10), command=lambda:self.copy(3)),
        ]

        # Place labels and entries on table
        for i in range(3):
            tabTL = tabTLs[i] # Get current table top left

            self.tabSPs[i][0].place(x = tabTL[0] + 66, y = tabTL[1] + 2, anchor = "n")
            self.tabSPs[i][1].place(x = tabTL[0] + 66, y = tabTL[1] + 23, anchor = "n")
            self.tabSPs[i][2].place(x = tabTL[0] + 66, y = tabTL[1] + 44, anchor = "n")

            self.tabNPs[i][0].place(x = tabTL[0] + 121, y = tabTL[1] + 2, anchor = "n")
            self.tabNPs[i][1].place(x = tabTL[0] + 121, y = tabTL[1] + 23, anchor = "n")
            self.tabNPs[i][2].place(x = tabTL[0] + 121, y = tabTL[1] + 44, anchor = "n")

            tabButs[i].place(x = tabTL[0] + 75, y = tabTL[1] + 80, anchor = "center")

    def buttons(self, y):
        start = [824, 554]
        tk.Button(
            text="Copy",
            command=lambda:self.copy(4)
        ).place(x = start[0] - 3, y = start[1], anchor = "e")

        tk.Button(
            text="Reset",
            command=lambda:self.copy(5)
        ).place(x = start[0] + 3, y = start[1], anchor = "w")

        tk.Button(
            text="GO",
            command = lambda:self.pushPress()
        ).place(x = start[0], y = start[1] + 30, anchor = "center")

        tk.Button(
            text="S UP",
            command = lambda:board.send(self.seg["setP"] + [1])
        ).place(x = 60, y = (y/2)-15, anchor = "center")

        tk.Button(
            text="S DN",
            command = lambda:board.send(self.seg["setP"] + [2])
        ).place(x = 60, y = (y/2)+15, anchor = "center")

        tk.Button(
            text="L UP",
            command = lambda:board.send(self.seg["setP"] + [3])
        ).place(x = 60, y = (y/2)-45, anchor = "center")

        tk.Button(
            text="L DN",
            command = lambda:board.send(self.seg["setP"] + [4])
        ).place(x = 60, y = (y/2)+45, anchor = "center")

    def copy(self, seg):
        match seg:
            case 1:
                input = self.tabNPs[0][0].get()
                replace(self.tabNPs[0][1], input)
                replace(self.tabNPs[0][2], input)
            case 2:
                input = self.tabNPs[1][0].get()
                replace(self.tabNPs[1][1], input)
                replace(self.tabNPs[1][2], input)
            case 3:
                input = self.tabNPs[2][0].get()
                replace(self.tabNPs[2][1], input)
                replace(self.tabNPs[2][2], input)
            case 4:
                input = self.tabNPs[0][0].get()
                replace(self.tabNPs[0][1], input)
                replace(self.tabNPs[0][2], input)
                replace(self.tabNPs[1][0], input)
                replace(self.tabNPs[1][1], input)
                replace(self.tabNPs[1][2], input)
                replace(self.tabNPs[2][0], input)
                replace(self.tabNPs[2][1], input)
                replace(self.tabNPs[2][2], input)
            case 5:
                input = "-1"
                replace(self.tabNPs[0][0], input)
                replace(self.tabNPs[0][1], input)
                replace(self.tabNPs[0][2], input)
                replace(self.tabNPs[1][0], input)
                replace(self.tabNPs[1][1], input)
                replace(self.tabNPs[1][2], input)
                replace(self.tabNPs[2][0], input)
                replace(self.tabNPs[2][1], input)
                replace(self.tabNPs[2][2], input)

    def update(self):
        # Lookup for chamber state words
        status = ["Deflate", "Creep", "Inflate", "Lock"]
        
        while True:
            try:
                self.seg = board.get(self.seg)

                for i in range(3):
                    # Valve States
                    self.segInfo[i].config(text = self.seg["valveState"][i] + " PWM: " + str(self.seg["PWM"][i]))

                    # Chamber & table labels
                    for j in range(3):
                        k = 3*i + j
                        self.chamLabs[i][j].config(text = str(round(self.seg["chamPress"][k], 1)) + " kPa \n" + status[self.seg["status"][k]])

                        if self.seg["setP"][k] < 0:
                            self.tabSPs[i][j].config(text = "LOCK")
                        else:
                            self.tabSPs[i][j].config(text = str(self.seg["setP"][k]) + " kPa")
                        
                self.brdTime.config(text = str(round(self.seg["boardTime"] / 1000, 1)) + " s")
            
            except Exception as e:
                # print(e)
                print("Data out of date " + str(round(time.time() - start, 1)))

    def pushPress(self):
        ary = []

        # Append entered pressure, windowed to 0 <= P <= 100
        for i in range(3):
            for j in range(3):
                try:
                    NsetP = int(str(self.tabNPs[i][j].get()))
                    if NsetP > 100 or NsetP < -1:
                        NSetP = max(min(NSetP, 100), 0)
                        print("Set pressure has been clipped to 0 <= setP <= 100")
                    ary.append(NsetP)
                except:
                    print("Non-integer pressure supplied")
                    ary.append(self.seg["setP"][3*i + j])
                
        board.send(ary + [0])

    def __init__(self, x, y):
        # Create window
        self.window = tk.Tk()
        self.window.geometry(str(x) + "x" + str(y))
        self.window.title("PSCR Control")
        self.rig = tk.PhotoImage(file = "BackImageLQ.png") #.subsample(4, 4)

        # Background
        tk.Label(self.window, image = self.rig).place(x = 0,y = 0)

        tabTLs = [[749, 444], [749, 110], [749, 277]]
        segCents = [[587, 470], [587, 136], [587, 303]]

        self.labelSegs(segCents)
        self.labelTabsGeneric(tabTLs)
        self.labelTabs(tabTLs)
        self.buttons(y)
        self.copy(5)

        tk.Label(text="Board Time:", font=font.Font(weight="bold")).place(x = 587, y = 580, anchor='center')
        self.brdTime = tk.Label()
        self.brdTime.place(x = 587, y = 600, anchor='center')

        self.seg = board.get(0)

def replace(object, input):
    object.delete(0, tk.END)
    object.insert(0, input)
