import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np

machi = 0
# Local Libraries
#from libs import clean_data




LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)


style.use("ggplot")

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def animate(i):

    """

    try:
        plot_motor(machine,motor,currents_MACHINE_2016, currents_MACHINE_2015,currents_MACHINE_2017,\
                   aviable_2016_months, aviable_2016_months_as_number,\
                   aviable_2015_months, aviable_2015_months_as_number,\
                   aviable_2017_months, aviable_2017_months_as_number, kind = 3)
    except Exception as e:
        print("I can't this motor " +str(motor) + ' by this:', e)

    """
    #dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    #data = urllib.request.urlopen(dataLink)
    #data = data.read().decode("utf-8")
    #data = json.loads(data)

    
    #data = data["btc_usd"]
    #data = pd.DataFrame(data)

    #buys = data[(data['type']=="bid")]
    #buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
    #buyDates = (buys["datestamp"]).tolist()
    

    #sells = data[(data['type']=="ask")]
    #sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    #sellDates = (sells["datestamp"]).tolist()
    #a.plot(currents_WASHER['M9'][3],'-',linestyle='solid', color='0.15', label='Nominal:  %s' %currents_WASHER['M9'][3])
    #a.plot(currents_WASHER['M9'][0],'-', color='red', label='L1: %s' %currents_WASHER['M9'][0])
    ##.plot(currents_WASHER['M9'][1],'-', color='b', label='L2: %s' %currents_WASHER['M9'][1])
    #a.plot(currents_WASHER['M9'][2],'-', color='g', label='L3: %s' %currents_WASHER['M9'][2])
    #a.clear()
    
    
    #a.plot_date(buyDates, buys["price"], "#00A3E0", label="buys")
    #a.plot_date(sellDates, sells["price"], "#183A54", label="sells")

    #a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,         ncol=1, borderaxespad=0)

    #title = "BTC-e BTCUSD Prices\nLast Price: "+str(data["price"][1999])
    #a.set_title(title)
"""    for motor in aviable_motors:
        try:
        
            a.figure(figsize=(20,10))
            a.plot(currents_WASHER[motor][3],'-',linestyle='solid', color='0.15', label='Nominal:  %s' %currents_WASHER[motor][3])

            #plt.plot(currents_WASHER[motor][0],'-', color='red', label='L1:')
            #plt.plot(currents_WASHER[motor][1],'-', color='b', label='L2:')
            #plt.plot(currents_WASHER[motor][2],'-', color='g', label='L3:')

            a.plot(currents_WASHER[motor][0],'-', color='red', label='L1: %s' %currents_WASHER[motor][0])
            a.plot(currents_WASHER[motor][1],'-', color='b', label='L2: %s' %currents_WASHER[motor][1])
            a.plot(currents_WASHER[motor][2],'-', color='g', label='L3: %s' %currents_WASHER[motor][2])

            #plt.plot(currents_[motor][0],'-', color='red', label='L1')
            #plt.plot(currents_conveyor[motor][1],'-', color='b', label='L2')
            #plt.plot(currents_conveyor[motor][2],'-', color='g', label='L3')

            a.legend();

            a.axes().set(xlim=(0,6),label='Months', ylabel='currents [A]',title='A Simple Plot %s'%motor);

   
        
           
        except:
            pass
"""
            

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Motor Tracking App")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)


        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label = "Tick",
                           command=lambda: changeTimeFrame('tick'))
        dataTF.add_command(label = "1 Day",
                           command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label = "3 Day",
                           command=lambda: changeTimeFrame('3d'))
        dataTF.add_command(label = "1 Week",
                           command=lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label = "Data Time Frame", menu = dataTF)

       

               
        tk.Tk.config(self, menu=menubar)



        self.frames = {}

        for F in (StartPage, Conveyor, Bake_Oven, Plot):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""ALPHA Motor track application
        use at your own risk. There is no promise
        of warranty."""), font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Conveyor",
                            command=lambda: controller.show_frame(Conveyor))
        button1.pack()

        button2 = ttk.Button(self, text='Bake Oven',
        					command=lambda: controller.show_frame(Bake_Oven))
        button2.pack()

        button3 = ttk.Button(self, text="Exit",
                            command=quit)
        button3.pack()


from libs.parsing_data import machine

class Bake_Oven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page BakeOven!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        machi = 'BAKEN OVEN'
        currents_MACHINE_2015, currents_MACHINE_2016, currents_MACHINE_2017,\
        aviable_2017_months, aviable_2017_months_as_number, \
        aviable_2016_months, aviable_2016_months_as_number, \
        aviable_2015_months, aviable_2015_months_as_number,\
        aviable_2017_motors, aviable_2016_motors,aviable_2015_motors  = machine(machi)

        for value in aviable_2017_motors:
            button = ttk.Button(self, text='%s' %value,\
                    command=lambda: controller.show_frame(Plot))
            button.pack()            


class Conveyor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Conveyor Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        
        
        button1.pack()
        
        
        
         # SCROLLBAR
        scrollbar = ttk.Scrollbar(self)
        
        
        scrollbar.pack( side = RIGHT, fill=Y )
        
        
        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

       
        scrollbar.config( command = canvas )


class Plot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PLOT!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        
        
        button1.pack()
        
        F = Figure(figsize=(20,10), dpi = 100)
        a = F.add_subplot(111)
        a.plot([1,2,3,4,5],[5,4,3,2,1])

        #a.plot.legend(loc = 9, fancybox = True, shadow = True)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




def plot_motor(machine, motor, current_MACHINE_YEAR_1, current_MACHINE_YEAR_2,current_MACHINE_YEAR_3, aviable_YEAR_months, aviable_YEAR_months_as_number,\
      aviable_YEAR_months_2, aviable_YEAR_months_as_number_2,aviable_YEAR_months_3, aviable_YEAR_months_as_number_3, kind):


    if kind ==3: # Line Chart

        years_as_months = {1:'ENE 2015',2:'FEB 2015',3:'MAR 2015',4:'ABR 2015',5:'MAY 2015',6:'JUN 2015',7:'JUL 2015',8:'AUG 2015',9:'SEP 2015',10:'OCT 2015',11:'NOV 2015',12:'DIC 2015',\
             13:'ENE 2016',14:'FEB 2016',15:'MAR 2016',16:'ABR 2016',17:'MAY 2016',18:'JUN 2016',19:'JUL 2016',20:'AUG 2016',21:'SEP 2016',22:'OCT 2016',23:'NOV 2016',24:'DIC 2016',\
             25:'ENE 2017',26:'FEB 2017', 27:'MAR 2017', 28:'ABR 2017',29:'MAY 2017'}

        L1_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][0] ]
        L2_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][1] ]
        L3_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][2] ]



        L1_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][0] ]
        L2_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][1] ]
        L3_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][2] ]


        L1_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][0] ]
        L2_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][1] ]
        L3_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][2] ]

        L1 = L1_2015 + L1_2016 + L1_2017
        L2 = L2_2015 + L2_2016 + L2_2017
        L3 = L3_2015 + L3_2016 + L3_2017


        plt.figure(figsize=(25,10))




        l1 = aviable_YEAR_months_as_number
        l2 = aviable_YEAR_months_as_number_2
        l3 = aviable_YEAR_months_as_number_3

        l4 = l2 +[value + 12 for value in l1] + [value +24 for value in l3]

        n = ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_1[motor][3])]+\
        ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_2[motor][3])]+\
        ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_3[motor][3])]
        print(n)
    def get_aviable_months_L(month_data):
        aviable_months_name = []
        aviable_months_number = []

        for keys in years_as_months.keys():
            if keys in month_data:
                aviable_months_name.append(years_as_months[keys])
                aviable_months_number.append(keys)
        aviable_months_number = sorted(aviable_months_number, key=int)
        return aviable_months_name, aviable_months_number

    months_name,months_name_number = get_aviable_months_L(l4)
    plt.xticks(months_name_number, months_name)

    plt.plot( months_name_number, n,'-',linestyle='solid', color='0.20', label='Nominal:  %s' %n)

    plt.plot( months_name_number,L1,'-', color='red', label='L1: %s' %L1)
    plt.plot( months_name_number,L2,'-', color='b', label='L2:  %s' %L2)
    plt.plot( months_name_number,L3,'-', color='g', label='L3: %s' %L3)

           
    plt.legend(loc = 9, fancybox = True, shadow = True)

    plt.axes().set(xlim=(1,28),label='Months', ylabel='currents [A]',title='A Simple Plot %s'%motor+' -- '+str(current_MACHINE_YEAR_1[motor][4][-1]))
    plt.savefig(path_to_save +"\_"+ machi +'_%s.jpg' %motor)




app = SeaofBTCapp()
app.geometry("800x600")
#ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()

#if __name__ == '__main__':

#    #libs.main(["test_ieee_cases.py","-xs"])
#    return os.chdir(original_path+'\excel_data\CORRIENTES %s' %year)

