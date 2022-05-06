import matplotlib.pyplot as plt
 
class GanttChart:
    def __init__(self):
        pass
    def __new(self):
        plt.close()
        # Declaring a figure "gnt"
        self.fig, self.gnt = plt.subplots()
        # Setting Y-axis limits
        #gnt.set_ylim(0, 50)
        # 
        ## Setting X-axis limits
        #gnt.set_xlim(0, 160)
        #
        # Setting labels for x-axis and y-axis
        self.gnt.set_xlabel('time')
        self.gnt.set_ylabel('Process')
        # Setting graph attribute
        self.gnt.grid(True)
    def show(self):
        plt.show()
    def save(self, fileName: str):
        plt.savefig(fileName)
    #
    def plot(self, procLs):
        self.__new()
        #-------------------------------------
        mp = {}
        Id2Name = {}
        n = 0
        for el in procLs:
            name,startT,runT = el
            if name not in mp:
                mp[name] = (n, (n+1)*10)
                Id2Name[n] = name
                n += 1
        cmap = plt.cm.get_cmap('hsv', n+2)
        #
        for el in procLs:
            name,startT,runT = el
            attr = mp[name]
            self.gnt.broken_barh([(startT, runT)], (attr[1], 10),
                    facecolors=cmap(attr[0]+1))

        #-------------------------------------
        # Setting ticks on y-axis
        self.gnt.set_yticks([(i+1)*10+5 for i in range(n)])
        # Labelling tickes of y-axis
        self.gnt.set_yticklabels([Id2Name[i] for i in range(n)])
        #
        #

