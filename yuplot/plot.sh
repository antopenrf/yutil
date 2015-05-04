gnuplot -e " plot 'data.txt' using 1:2 title 'gain' with lines; set term png;set xlabel 'x';set ylabel 'y'; set output 'plot.png';set title 'plot'; set grid; replot"
