gnuplot -e " plot 'data.txt' using 1:2 title '1' with lines; set term png;set xlabel 'freq (GHz)';set ylabel 'gain (dB)'; set output 'plot.png'; replot"
