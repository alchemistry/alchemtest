Amber: a collection of files used to test specific part of the amber parser.
============================================================================

no_atomic_section: amber output file without the ATOMIC section
no_control_data: amber output file without the '2.  CONTROL  DATA  FOR  ' section
no_dHdl_data_points: amber output file with TI active, but no DV/DL values,
no_free_energy_info: amber output file without the settings regarding the free energy calculation
no_results_section: amber output file without the RESULT section
no_temp0_setted: amber output file with temp0 not setted
no_useful_data: amber output file without useful data, truncated after the header
none_in_mbar: amber output file with a wrongly formatted MBAR section. Specifically, a lambda value in a MBAR section has been altered, so it dowsn't match with the other MBAR sections and the expected lambda values (0.2500 --> 0.2550)
not_finished_run: amber output file from an unterminated run
