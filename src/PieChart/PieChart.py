from Tkinter import *
from Pie import *
from InputParser import *
import random


class PieChart:

        def __init__(self, data, colors=list()):
                self.data = clean_data(data, colors) if data is not None else None
                      
                self.master = Tk()
                self.master.resizable(0,0)
                self.master.title("PieGraph")  #eventually set by user

                self.pie = get_pie(self.master)
                self.canvas_size = int(self.pie.cget("height"))
                self.current_percent = 0      #will go around the pie, making slices

                slices = len(self.data)
                while(len(colors) < slices):
                        colors.append('yellow')

                self._build_chart(self.data, colors)

        def _get_slice(self, percent, color):
                #get a random three bit hexadecimal number.
                #n/4096 chance of printing same number, shouldn't be a problem.
                start=self.current_percent*360
                extent=percent*360
                if( 359 < extent + start < 360): extent = 360 - start
                self.pie.create_arc(self.canvas_size/4, self.canvas_size/4,
                                    self.canvas_size*3/4, self.canvas_size*3/4,
                                    outline='black', 
                                    start=start,
                                    extent=percent*360,
                                    style=PIESLICE,
                                    fill=color)
                self.current_percent += percent
                return
                
        #get a random three bit hexadecimal number.
        #n/4096 chance of printing same number, shouldn't be a problem.
        def _gen_color(self):
                color = "#%03x" % random.randint(0, 0xFFF)
                return color
        
        def _build_chart(self, data, colors):
                for i in range(len(data)):
                        self._get_slice(data[i]['fraction'], colors[i])
                return
                        
                        
        
if __name__ == '__main__':

        colors = ['red', 'white', 'blue']
        data = [("five percent", 5) , ("ten percent", 10), ("85 percent", 10)]
        PieChart(data, colors)
        mainloop()
