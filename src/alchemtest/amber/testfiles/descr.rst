Amber: invalid/incomplete output files 
======================================================

Here we collected some invalid/incomplete AMBER output files that can be used to test specific part of the amber parser.

Notes
-----

- no_atomic_section.out.bz2: AMBER output file without the ATOMIC section
- no_control_data.out.bz2: AMBER output file without the '2.  CONTROL  DATA  FOR  ' section
- no_dHdl_data_points.out.bz2: AMBER output file with TI active, but no DV/DL values,
- no_free_energy_info.out.bz2: AMBER output file without the settings regarding the free energy calculation
- no_results_section.out.bz2: AMBER output file without the RESULT section
- no_temp0_set.out.bz2: AMBER output file with temp0 not set
- no_useful_data.out.bz2: AMBER output file without useful data, truncated after the header
- none_in_mbar.out.bz2: AMBER output file with a wrongly formatted MBAR section. Specifically, a lambda value in a MBAR section has been altered, so it dowsn't match with the other MBAR sections and the expected lambda values (0.2500 --> 0.2550)
- not_finished_run.out.bz2: AMBER output file from an unterminated run


.. versionadded:: 0.7.0
