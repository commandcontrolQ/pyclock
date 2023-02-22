from datetime import datetime as dt

class clock:
    def __init__(self, sfst=False): # init function runs first always, sfst: start from system time
        if not sfst:
            self.tlist = [0, 0, 0] # start from 00:00:00
        else:
            ct = dt.now()
            self.tlist = [ct.hour, ct.minute, ct.second] # start from the current system time
        self.ctime = f"{str(self.tlist[0]).zfill(2)}:{str(self.tlist[1]).zfill(2)}:{str(self.tlist[2]).zfill(2)}"
    def update(self): # update the clock
        __max_sm__ = 59 # define the maximum values for the seconds, minutes, and hours
        __max_h__ = 23
        if self.tlist[2] == __max_sm__:
            if self.tlist[1] == __max_sm__:
                if self.tlist[0] == __max_h__:
                    self.tlist = [0, 0, 0] # if the clock reads 23:59:59, loop back to 00:00:00
                else:
                    self.tlist[0] = self.tlist[0] + 1
                    self.tlist[1], self.tlist[2] = 0, 0 # increment hour, reset minutes and seconds
            else:
                self.tlist[1] = self.tlist[1] + 1
                self.tlist[2] = 0 # increment minute, reset seconds
        else:
            self.tlist[2] = self.tlist[2] + 1 # increment seconds, redefine full time
        self.ctime = f"{str(self.tlist[0]).zfill(2)}:{str(self.tlist[1]).zfill(2)}:{str(self.tlist[2]).zfill(2)}"

if __name__ == "__main__": # run the code in the if statement when this python file is run
    from time import sleep as pause
    loop = True
    while loop:
        choice = input("Display the clock in binary, hex, denary or octal (b/h/d/o): ")
        if choice not in ["b","h","d","o","B","H","D","O"]:
            print("Try again\n") # input sanitisation
            pause(2)
        else:
            break
    clk = clock(True) # refer to clock module as clk, by default sfst is True but this can be changed
    while True:
        clk.update()
        if choice in ["b","B"]:
            ctime = clk.ctime # format the clock to 6 digit binary
            ctime = f"{format(int(ctime[0:2]),'06b')}:{format(int(ctime[3:5]),'06b')}:{format(int(ctime[6:8]),'06b')}"
        elif choice in ["h","H"]:
            ctime = clk.ctime # format the clock to hexadecimal
            ctime = f"{'{0:0{1}X}'.format(int(ctime[0:2]),2)}:{'{0:0{1}X}'.format(int(ctime[3:5]),2)}:{'{0:0{1}X}'.format(int(ctime[6:8]),2)}"
        elif choice in ["d","D"]:
            ctime = clk.ctime # nothing, pass
        elif choice in ["o","O"]:
            ctime = clk.ctime # format the clock to octal
            ctime = f"{'{0:0{1}o}'.format(int(ctime[0:2]),2)}:{'{0:0{1}o}'.format(int(ctime[3:5]),2)}:{'{0:0{1}o}'.format(int(ctime[6:8]),2)}"
        print(ctime)
        pause(1) # loop
        

