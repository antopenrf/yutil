<<<<<<< HEAD
gnuplot -e " plot 'data.txt' using 1:2 title 'gain' with lines; set term png;set xlabel 'freq_GHz';set ylabel 'gain_dB'; set output 'plot.png';set title '3126_dipole'; set grid; replot"
=======
gnuplot -e " plot 'data.txt' using 1:2 title '1' with lines; set term png;set xlabel 'freq (GHz)';set ylabel 'gain (dB)'; set output 'plot.png'; replot"
>>>>>>> 1b9a8d35607f7e2a15fe1409c2561e0d48c9f05d
