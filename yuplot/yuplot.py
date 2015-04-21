#!/usr/bin/python

# author: yulung@linux.com
# date: created on April 21st

import sys
import os


class yuplot(object):

    def _xlog_on(self):
        if self.xlog == '0':
            return ''
        else:
            return "set logscale x;"

    def _ylog_on(self):
        if self.ylog == '0':
            return ''
        else:
            return "set logscale y;"

    def _add_xlabel(self):
        return "set xlabel '" + self.xlabel + "';"

    def _add_ylabel(self):
        return "set ylabel '" + self.ylabel + "';"

    def plot(self):
        self.plot_string = "gnuplot -e \" plot" + self._add_data() + ";" + " set term png;" + self._add_xlabel() + self._add_ylabel() + self._xlog_on() + self._ylog_on() + " set output 'plot.png'; replot\"\n"
        with open(self.shfile, 'w') as f:
            f.write(self.plot_string)

        os.system("sh plot.sh")
        os.system("open plot.png")

    def _add_data(self, ref = 1):
        strings_to_return = ''
        for n in range(self.columns_to_plot):
            strings_to_return += " '" + self.outputfile + "' using " + str(ref) + ":" + str(n + 2) + " title " + "'" + str(self.legends[n+1]) + "'" + " with lines"
            if n != self.columns_to_plot - 1:
                strings_to_return += ','
        return strings_to_return

    def __init__(self, inputfile = None, xlabel = 'x', ylabel = 'y', xlog = '0', ylog = '0',  outputfile = 'data.txt', shfile = 'plot.sh'):
        
        self.plot_string = None
        try:
            self.inputfile = sys.argv[1]
        except:
            self.inputfile = inputfile
        
        self.outputfile = outputfile
        self.shfile = shfile

        try:
            self.xlabel = sys.argv[2]
        except:
            self.xlabel = 'x'

        try:
            self.ylabel = sys.argv[3]
        except:
            self.ylabel = 'y'

        try:
            self.xlog = sys.argv[4]
        except:
            self.xlog = '0'

        try:
            self.ylog = sys.argv[5]
        except:
            self.ylog = '0'

        with open(self.inputfile, 'r') as f:
            all_lines = f.readlines()

        with open(self.outputfile, 'w') as f:
            for count,each in enumerate(all_lines):
                if count == 0:
                    each = each.replace("\r","")
                    each = each.replace(",", "\t")
                    self.columns_to_plot = len(each.split()) - 1
                    try:
                        float(each[0])
                        self.legends = range(self.columns_to_plot+1)
                    except ValueError:
                        each = each.replace("\r","")
                        each = each.replace(",", "\t")
                        self.legends = each.split()
                each = each.replace("\r","")
                each = each.replace(",", "\t")
                f.write(each)

        self.plot()


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Usage: python yuplot.py inputfile xlable ylabel [0 or 1 for x logscable] [0 or 1 for y logscable]/n")

    else:
        plotter = yuplot()

        
