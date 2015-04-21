gnuplot -e "plot 'data.txt' using 1:2 title '2' with lines; set term png; set output 'plot.png'; replot"
