gnuplot -e " plot 'data.txt' using 1:2 title 'v' with lines; set term png;set xlabel 'twtsts';set ylabel 'yyyyyy';set logscale x; set output 'plot.png'; replot"
