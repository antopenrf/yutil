#!/usr/bin/python

# author: yulung@linux.com
# date: created on April 21st

import sys
import os


class yuplot(object):

    def _wrt_plot_shell(self, content):
        with open(self.shfile, 'w') as f:
            f.write(content)


    def _add_data(self, ref = 1, column_to_plot = 2):
        return "plot '" + self.outputfile + "' using " + str(ref) + ":" + str(column_to_plot) + " title " + "'" + str(column_to_plot) + "'" + " with lines"

        

    def __init__(self, inputfile = None, outputfile = 'data.txt', shfile = 'plot.sh'):
        
        if len(sys.argv) != 2:
            print("Usage: python yuplot.py inputfile/n")

        else:
            self.inputfile = sys.argv[1]
            self.outputfile = outputfile
            self.shfile = shfile
            
            with open(self.inputfile, 'r') as f:
                all_lines = f.readlines()
                
            with open(self.outputfile, 'w') as f:
                for each in all_lines:
                    each = each.replace("\r","")
                    each = each.replace(",", "\t")
                    f.write(each)
                
            self.plot_string = "gnuplot -e \"" + self._add_data() + ";" + " set term png; set output 'plot.png'; replot\"\n"

            self._wrt_plot_shell(self.plot_string)
            

if __name__ == '__main__':
    plotter = yuplot()

    os.system("sh plot.sh")            
    os.system("open plot.png")

        
