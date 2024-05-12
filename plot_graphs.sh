#!/bin/bash

rm -rf plots
mkdir plots
gnuplot plotting/mustache_in.gpi
gnuplot plotting/linear_in.gpi
gnuplot plotting/errors_in.gpi
gnuplot plotting/mustache_out.gpi
gnuplot plotting/linear_out.gpi
gnuplot plotting/errors_out.gpi
gnuplot plotting/compare_errors.gpi