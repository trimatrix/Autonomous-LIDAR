#!C:\Anaconda3\Python.exe
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import multiprocessing, os, datetime, serial
import commands
class controlWindow:

    def __init__(self,master):
        self.com = None
        self.master = master
        self.master.title("Wood Bot V0.2")
        self.master.rowconfigure(1, weight = 1)
        self.master.columnconfigure(1, weight = 1)




        self.frmTop  = tk.Frame(self.master)
        self.lblComPort = tk.Label(self.frmTop, text = "Serial Port: ")
        self.entComPort = tk.Entry(self.frmTop)
        self.lblComBaud = tk.Label(self.frmTop, text = "Baud Rate: ")
        self.entComBaud = tk.Entry(self.frmTop)
        self.btnConnect = tk.Button(self.frmTop, text = "Connect",
                                    command = self.eveConnect)
        self.lblComPort.grid(column = 0, row = 0)
        self.entComPort.grid(column = 1, row = 0, sticky = tk.EW)
        self.lblComBaud.grid(column = 2, row = 0, sticky = tk.EW)
        self.entComBaud.grid(column = 3, row = 0, sticky = tk.EW)
        self.btnConnect.grid(column = 4, row = 0)




        self.frmTop.columnconfigure(1, weight = 1)
        self.frmTop.columnconfigure(3, weight = 1)
        self.frmTop.grid(row = 0, column = 0, columnspan = 3, sticky = tk.EW)




        self.frmLeft = tk.Frame(self.master)
        self.lblLMoto = tk.Label(self.frmLeft, text="Left Motor")
        self.lblLSpeed = tk.Label(self.frmLeft, text="speed")
        self.btnLFor = tk.Button(self.frmLeft,
                                 text="Forward",
                                 command = self.eveLForward)

        self.btnLStop = tk.Button(self.frmLeft,
                                  text="stop",
                                  command = self.eveLStop)
        self.btnLReverse = tk.Button(self.frmLeft,
                                     text="Reverse",
                                     command = self.eveLBackward)
        self.scaLSpeed = tk.Scale(self.frmLeft,
                                  from_=1500, to=0,
                                  command = self.syncLSpeed,
                                  orient=tk.VERTICAL)

        self.lblLMoto.grid(column=0, row=0)
        self.lblLSpeed.grid(column=1, row=0)
        self.btnLFor.grid(column=0, row=1, sticky=tk.NSEW)
        self.btnLStop.grid(column=0, row=2, sticky=tk.NSEW)
        self.btnLReverse.grid(column=0, row=3, sticky=tk.NSEW)
        self.scaLSpeed.grid(column=1, row=1, sticky=tk.NS, rowspan=3)

        self.frmLeft.rowconfigure(1, weight  = 1)
        self.frmLeft.rowconfigure(2, weight = 1)
        self.frmLeft.rowconfigure(3, weight = 1)
        self.frmLeft.grid(row = 1, column = 0, sticky = tk.NS)




        self.frmRight = tk.Frame(self.master)
        self.lblRMoto = tk.Label(self.frmRight, text="Right Motor")
        self.lblRSpeed = tk.Label(self.frmRight, text="speed")
        self.btnRFor = tk.Button(self.frmRight,
                                 text="Forward",
                                 command = self.eveRForward)
        self.btnRStop = tk.Button(self.frmRight,
                                  command = self.eveRStop,
                                  text="stop",)
        self.btnRReverse = tk.Button(self.frmRight,
                                     text="Reverse",
                                     command = self.eveRBackward)
        self.scaRSpeed = tk.Scale(self.frmRight,
                                  from_=1500, to=0,
                                  command  = self.syncRSpeed,
                                  orient=tk.VERTICAL)
        self.lblRSpeed.grid(column=1, row=0)
        self.lblRMoto.grid(column=2, row=0)
        self.btnRFor.grid(column=2, row=1, sticky=tk.NSEW)
        self.btnRStop.grid(column=2, row=2, sticky=tk.NSEW)
        self.btnRReverse.grid(column=2, row=3, sticky=tk.NSEW)
        self.scaRSpeed.grid(column=1, row=1, sticky=tk.NSEW, rowspan=3)

        self.frmRight.rowconfigure(1, weight  = 1)
        self.frmRight.rowconfigure(2, weight = 1)
        self.frmRight.rowconfigure(3, weight = 1)
        self.frmRight.grid(row = 1, column = 2, sticky = tk.NS)




        self.frmCenter = tk.Frame(self.master)

        self.frmCenterR = tk.Frame(self.frmCenter)
        self.lblRelaySign = tk.Label(self.frmCenterR, text = "Relay Control")
        self.lblRelays = []
        self.relays = []
        self.relayStatus = []

        for i in range(0,8):
            var = str(i+1)
            ttlButton = "Relay " + var
            self.lblRelays.append(tk.Label(self.frmCenterR,
                                           text = "Relay " + var,
                                           relief = tk.RIDGE))
            self.relayStatus.append(tk.BooleanVar())
            self.relays.append(tk.Checkbutton(self.frmCenterR,
                                              onvalue=False,
                                              offvalue=True,
                                              variable=self.relayStatus[i],
                                              command=self.eveRelay))

            self.lblRelays[i].grid(row = 1, column = i, sticky = tk.EW)
            self.relays[i].grid(row = 2, column = i, sticky = tk.EW)
            self.frmCenterR.columnconfigure(i, weight = 1)
        self.lblRelaySign.grid(row =0, column =


        0, columnspan =8, sticky =tk.EW)

        self.frmCenterR.rowconfigure(1, weight = 1)
        self.frmCenterR.rowconfigure(2, weight = 1)
        self.frmCenterR.grid(column = 0, row = 0, sticky = tk.EW)




        self.frmCenterT = tk.Frame(self.frmCenter)
        self.txtConsole = tk.Text(self.frmCenterT)
        self.txtConsole.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.frmCenterT.rowconfigure(0, weight = 1)
        self.frmCenterT.columnconfigure(0, weight = 1)
        self.frmCenterT.grid(column = 0, row = 1, sticky = tk.NSEW)




        self.frmCenterB = tk.Frame(self.frmCenter)
        self.bolSync = tk.BooleanVar()
        self.lblBoth = tk.Label(self.frmCenterB, text = "Control Both Motors?")
        self.rdbBothY = tk.Radiobutton(self.frmCenterB,
                                      text = "Yes",
                                      variable = self.bolSync,
                                      value = True)
        self.rdbBothN = tk.Radiobutton(self.frmCenterB,
                                      text = "No",
                                      variable = self.bolSync,
                                      value = False)
        self.btnSave = tk.Button(self.frmCenterB,
                                 command = self.eveSaveConsole,
                                 text = "Save console")
        self.btnExit = tk.Button(self.frmCenterB,
                                 text = "Exit",
                                 command = self.eveExit)

        self.lblBoth.grid(column = 0, row = 0, columnspan = 2, sticky = tk.EW)
        self.rdbBothY.grid(column = 0, row  = 1, sticky = tk.EW)
        self.rdbBothN.grid(column = 1, row =1, sticky = tk.EW)
        self.btnSave.grid(column = 0, row = 2, sticky = tk.EW)
        self.btnExit.grid(column = 1, row = 2, sticky = tk.EW)

        self.frmCenterB.columnconfigure(0, weight = 1)
        self.frmCenterB.columnconfigure(1, weight = 1)
        self.frmCenterB.grid(column = 0, row = 2, sticky = tk.NSEW)



        self.frmCenter.columnconfigure(0, weight = 1)
        self.frmCenter.rowconfigure(1, weight = 1)
        self.frmCenter.grid(column = 1, row = 1, sticky = tk.NSEW)

        self.scaLSpeed.set(1500)
        self.scaRSpeed.set(1500)
        self.entComPort.insert(0,'COM6')
        self.entComBaud.insert(0,'115200')
        self.bolSync.set(True)
        for i in range(0, 8):
            self.relays[i].deselect()
        self.txtConsole.insert(tk.END, str(datetime.datetime.now())+"\n")
        self.txtConsole.insert(tk.END, "Please connect controller and press connect button \n")


    def syncRSpeed(self,master):
        if (self.bolSync.get()==True):
            self.scaLSpeed.set(self.scaRSpeed.get())

    def syncLSpeed(self,master):
        if (self.bolSync.get()==True):
            self.scaRSpeed.set(self.scaLSpeed.get())

    def eveRelay(self):
        self.rcom = self.relayStatus[0].get() * 1   \
                   +self.relayStatus[1].get() * 2   \
                   +self.relayStatus[2].get() * 4   \
                   +self.relayStatus[3].get() * 8   \
                   +self.relayStatus[4].get() * 16  \
                   +self.relayStatus[5].get() * 32  \
                   +self.relayStatus[6].get() * 64  \
                   +self.relayStatus[7].get() * 128
        self.com.writeRelay(self.rcom)

        self.info = str(datetime.datetime.now())+" - relay "
        for i in range(0,8):
            if not self.relayStatus[i].get():
                self.info = self.info + str(i+1) + " "
        self.info = self.info + "is currently Active \n"

        self.txtConsole.insert(tk.END, self.info)

    def eveLForward(self):
        self.info = str(datetime.datetime.now())+" - "
        if (self.bolSync.get() == True):
            self.bolAccel = self.com.chBAccel(int(self.scaLSpeed.get()))
            self.bolSpeed = self.com.chBspeed(int(self.scaLSpeed.get()))
            self.bolStart = self.com.staBmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Both motors are forward with steps per second of "
                self.info = self.info + str(self.scaLSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolAccel = self.com.chLAccel(self.scaLSpeed.get())
            self.bolSpeed = self.com.chLspeed(self.scaLSpeed.get())
            self.bolStart = self.com.staLmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Left motors is forward with steps per second of "
                self.info = self.info + str(self.scaLSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")

    def eveLBackward(self):
        self.info = str(datetime.datetime.now())+" - "
        if (self.bolSync.get() == True):
            self.bolAccel = self.com.chBAccel(self.scaLSpeed.get())
            self.bolSpeed = self.com.chBspeed(self.scaLSpeed.get())
            self.bolStart = self.com.staRBmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Both motors are Backwards with steps per second of "
                self.info = self.info + str(self.scaLSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolAccel = self.com.chLAccel(self.scaLSpeed.get())
            self.bolSpeed = self.com.chLspeed(self.scaLSpeed.get())
            self.bolStart = self.com.staRLmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Left motors is Reverse with steps per second of "
                self.info = self.info + str(self.scaLSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")

    def eveLStop(self):
        if (self.bolSync.get() == True):
            self.bolStop = self.com.stoBmoto()
            self.info = str(datetime.datetime.now())+" - "
            if(self.bolStop):
                self.txtConsole.insert(tk.END, self.info + "Both Motors Stopped \n")
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolStop = self.com.stoLmoto()
            self.info = str(datetime.datetime.now())+" - "
            if(self.bolStop):
                self.txtConsole.insert(tk.END, self.info + "Left motor stopped \n")
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")

    def eveRForward(self):
        self.info = str(datetime.datetime.now())+" - "
        if (self.bolSync.get() == True):
            self.bolAccel = self.com.chBAccel(self.scaRSpeed.get())
            self.bolSpeed = self.com.chBspeed(self.scaRSpeed.get())
            self.bolStart = self.com.staBmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Both motors are forward with steps per second of "
                self.info = self.info + str(self.scaRSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolAccel = self.com.chRAccel(self.scaRSpeed.get())
            self.bolSpeed = self.com.chRspeed(self.scaRSpeed.get())
            self.bolStart = self.com.staRmoto()

            if(self.bolStop and self.bolAccel and self.bolStart):
                self.info = self.info + "Right motors is forward with steps per second of "
                self.info = self.info + str(self.scaRSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")

    def eveRBackward(self):
        self.info = str(datetime.datetime.now())+" - "
        if (self.bolSync.get() == True):
            self.bolAccel = self.com.chBAccel(self.scaRSpeed.get())
            self.bolSpeed = self.com.chBspeed(self.scaRSpeed.get())
            self.bolStart = self.com.staRBmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Both motors are Backwards with steps per second of "
                self.info = self.info + str(self.scaRSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolAccel = self.com.chRAccel(self.scaRSpeed.get())
            self.bolSpeed = self.com.chRspeed(self.scaRSpeed.get())
            self.bolStart = self.com.staRRmoto()

            if(self.bolSpeed and self.bolAccel and self.bolStart):
                self.info = self.info + "Right motors is Reverse with steps per second of "
                self.info = self.info + str(self.scaRSpeed.get())+ "\n"
                self.txtConsole.insert(tk.END, self.info)
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")


    def eveRStop(self):
        if (self.bolSync.get() == True):
            self.bolStop = self.com.stoBmoto()
            self.info = str(datetime.datetime.now())+" - "
            if(self.bolStop):
                self.txtConsole.insert(tk.END, self.info + "Both Motors Stopped \n")
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")
        else:
            self.bolStop = self.com.stoRmoto()
            self.info = str(datetime.datetime.now())+" - "
            if(self.bolStop):
                self.txtConsole.insert(tk.END, self.info + "Right motor stopped \n")
            else:
                self.txtConsole.insert(tk.END, "Error: command failed to send please reconnect \n")

    def eveConnect(self):
        try:
            self.com = commands.command(self.entComPort.get(), self.entComBaud.get())
            self.txtConsole.insert(tk.END, "Controller connected \n")
        except:
            self.txtConsole.insert(tk.END, "Something went wrong connecting to controller. \n \
try turning on a motor or relay to ensure a connection is established. \n \
If the cart is unresponsive to command, exit the program and reconnect  \n \
the controller and restart the program.")


    def eveSaveConsole(self):
        saveFile  = tk.filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
        if saveFile is None:
            return
        saveText = str(self.txtConsole.get(1.0, tk.END))
        saveFile.write(saveText)
        saveFile.close()

    def eveExit(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = controlWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
