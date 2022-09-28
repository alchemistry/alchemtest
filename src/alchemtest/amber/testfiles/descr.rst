Amber: invalid/incomplete output files 
======================================================

Here we collected some invalid/incomplete amber output files that can be used to test specific part of the amber parser.

Notes
-----

- no_atomic_section.out.tar.bz2: amberoutput file without the ATOMIC section
- no_control_data.out.tar.bz2: amberoutput file without the '2.  CONTROL  DATA  FOR  ' section
- no_dHdl_data_points.out.tar.bz2: amberoutput file with TI active, but no DV/DL values,
- no_free_energy_info.out.tar.bz2: amberoutput file without the settings regarding the free energy calculation
- no_results_section.out.tar.bz2: amberoutput file without the RESULT section
- no_temp0_setted.out.tar.bz2: amberoutput file with temp0 not setted
- no_useful_data.out.tar.bz2: amberoutput file without useful data, truncated after the header
- none_in_mbar.out.tar.bz2: amberoutput file with a wrongly formatted MBAR section. Specifically, a lambda value in a MBAR section has been altered, so it dowsn't match with the other MBAR sections and the expected lambda values (0.2500 --> 0.2550)
- not_finished_run.out.tar.bz2: amberoutput file from an unterminated run


.. versionadded:: 0.7.0
