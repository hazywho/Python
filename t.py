import gradio as gr
import math
import matplotlib.pyplot as plt
import numpy as np
def m(a):
    return math.sin(a*math.pi/360)
def plotLine(x):
    x = np.array([m(a) for a in range(0,int(x))])
    fig = plt.figure()
    plt.plot(x,"-")
    return fig

demo = gr.Interface(
    plotLine,
    [
        gr.Slider(0,360,label="Value")
    ],
    gr.Plot(label="line"),
)

demo.launch(share=True)