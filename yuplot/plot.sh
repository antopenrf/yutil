gnuplot -e " plot 'data.txt' using 1:2 title '1' with lines; set term png;set xlabel 'x';set ylabel 'y'; set output 'plot.png';set title 'plot'; set grid; replot"
