gnuplot -e "plot 'data.txt' using 1:2 title '2'with linespoints; set term png; set output 'plot.png'; replot"
