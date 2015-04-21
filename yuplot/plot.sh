gnuplot -e " plot 'data.txt' using 1:2 title '1st' with lines, 'data.txt' using 1:3 title '2nd' with lines, 'data.txt' using 1:4 title '3rd' with lines, 'data.txt' using 1:5 title '4th' with lines; set term png;set xlabel 'x_axis';set ylabel 'y_axis';set logscale x; set output 'plot.png'; replot"
