gnuplot -e " plot 'data.txt' using 1:2 title 'gain' with lines; set term png;set xlabel 'freq_GHz';set ylabel 'gain_dB'; set output 'plot.png';set title '3126_dipole'; set grid; replot"
