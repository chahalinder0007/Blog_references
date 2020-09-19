import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation



class CreateVideo:
    def __init__(self,fps = 15,writers = "ffmpeg",title = "Simulation",artist = "Maths",comment = "No Comment"):

        FFMpegWriter = animation.writers[writers]
        metadata = dict(title = title, artist = artist,comment = comment)
        self.writer = FFMpegWriter(fps=fps,metadata = metadata)


    def create_base(self,xlim=(-5,6000), ylim=(-60,60),markersize = 3,color="k"):
        #all details on what

        fig = plt.figure()

        #default color is k meaning the default color is black
        l, = plt.plot([],[],"k-o",markersize = markersize,color=color)

        plt.xlim(xlim[0],xlim[1])
        plt.ylim(ylim[0],ylim[1])
        
        #Setting up the game conditions in here
        plt.plot(list(range(xlim[1])),[50 for x in range(xlim[1])], color = "blue")
        plt.text(x=xlim[1]/2,y = 53,s="X Wins and Game Ends",color="blue")

        plt.plot(list(range(xlim[1])),[-50 for x in range(xlim[1])],color = "red")
        plt.text(x=xlim[1]/2,y = -47,s="X Lost and Game Ends",color="red")        


        return plt,l,fig,self.writer