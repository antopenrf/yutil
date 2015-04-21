gnuplot -e "plot 'data.txt' using 1:2 title '2' with lines,plot 'data.txt' using 1:3 title '3' with lines,plot 'data.txt' using 1:4 title '4' with lines; set term png; set output 'plot.png'; replot"
