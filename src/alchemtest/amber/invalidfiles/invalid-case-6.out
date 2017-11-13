
          -------------------------------------------------------
          Amber 16 PMEMD                              2016
          -------------------------------------------------------

| PMEMD implementation of SANDER, Release 16

| Run on 09/25/2017 at 15:27:20

|   Executable path: /software/amber16_latest_patched/bin/pmemd.cuda
| Working directory: /free_energy/17124-1~18637-1/solvated/charge/0.00
|          Hostname: stxcompute013

  [-O]verwriting output

File Assignments:
|   MDIN: ti.in                                                                 
|  MDOUT: ti-0.00.out                                                           
| INPCRD: heat-0.00.rst7                                                        
|   PARM: ti.parm7                                                              
| RESTRT: ti-0.00.rst7                                                          
|   REFC: heat-0.00.rst7                                                        
|  MDVEL: mdvel                                                                 
|   MDEN: ti-0.00.en                                                            
|  MDCRD: ti-0.00.nc                                                            
| MDINFO: ti-0.00.info                                                          
|  MDFRC: mdfrc                                                                 


 Here is the input file:

TI/FEP, NpT, charge transformation                                             
 &cntrl                                                                        
 ! please adjust namelist parameters to your needs!                            
                                                                               
 ! parameters for general MD                                                   
 imin = 0, nstlim = 500000, irest = 1, ntx = 5, dt = 0.002,                    
 ntt = 3, temp0 = 298.0, gamma_ln = 2.0, ig = -1,                              
 ntb = 2,                                                                      
 ntp = 1, barostat = 2, pres0 = 1.01325, taup = 2.0,                           
 ntwe = 1000, ntwx = 10000, ntpr = 1000, ntwr = 50000, ntave = 50000,          
 ioutfm = 1, iwrap = 1, ntxo = 2,                                              
                                                                               
 ! parameters for alchemical free energy simulation                            
 ntc = 2, ntf = 1,                                                             
 noshakemask = ':1,2',                                                         
                                                                               
 icfe = 1, ifsc = 0, clambda = 0.00, scalpha = 0.5, scbeta = 12.0,             
 ifmbar = 0, bar_intervall = 500, bar_l_min = 0.0, bar_l_max = 1.0,            
 bar_l_incr = 0.1,   ! ntpr = bar_intervall for alchemical analysis tool       
                                                                               
 timask1=':1', timask2=':2',                                                   
scmask1='',                                                                    
scmask2='',                                                                    
 crgmask = '',                                                                 
 /                                                                             
 &ewald                                                                        
 /                                                                             


Note: ig = -1. Setting random seed to   914176 based on wallclock time in 
      microseconds.
| irandom = 1, using AMBER's internal random number generator (default).
 
|--------------------- INFORMATION ----------------------
| GPU (CUDA) Version of PMEMD in use: NVIDIA GPU IN USE.
|                    Version 16.0.0
| 
|                      02/25/2016
| 
| Implementation by:
|                    Ross C. Walker     (SDSC)
|                    Scott Le Grand     (nVIDIA)
| 
| Precision model in use:
|      [SPFP] - Single Precision Forces, 64-bit Fixed Point
|               Accumulation. (Default)
| 
|--------------------------------------------------------
 
|----------------- CITATION INFORMATION -----------------
|
|    When publishing work that utilized the CUDA version
|    of AMBER, please cite the following in addition to
|    the regular AMBER citations:
|
|  - Romelia Salomon-Ferrer; Andreas W. Goetz; Duncan
|    Poole; Scott Le Grand; Ross C. Walker "Routine
|    microsecond molecular dynamics simulations with
|    AMBER - Part II: Particle Mesh Ewald", J. Chem.
|    Theory Comput., 2013, 9 (9), pp3878-3888,
|    DOI: 10.1021/ct400314y.
|
|  - Andreas W. Goetz; Mark J. Williamson; Dong Xu;
|    Duncan Poole; Scott Le Grand; Ross C. Walker
|    "Routine microsecond molecular dynamics simulations
|    with AMBER - Part I: Generalized Born", J. Chem.
|    Theory Comput., 2012, 8 (5), pp1542-1555.
|
|  - Scott Le Grand; Andreas W. Goetz; Ross C. Walker
|    "SPFP: Speed without compromise - a mixed precision
|    model for GPU accelerated molecular dynamics
|    simulations.", Comp. Phys. Comm., 2013, 184
|    pp374-380, DOI: 10.1016/j.cpc.2012.09.022
|
|--------------------------------------------------------
 
|------------------- GPU DEVICE INFO --------------------
|
|            CUDA_VISIBLE_DEVICES: 2
|   CUDA Capable Devices Detected:      1
|           CUDA Device ID in use:      0
|                CUDA Device Name: GeForce GTX 1080 Ti
|     CUDA Device Global Mem Size:  11172 MB
| CUDA Device Num Multiprocessors:     28
|           CUDA Device Core Freq:   1.58 GHz
|
|--------------------------------------------------------
 
 
| Conditional Compilation Defines Used:
| PUBFFT
| BINTRAJ
| CUDA
| EMIL

| Largest sphere to fit in unit cell has radius =    17.062

| New format PARM file being parsed.
| Version =    1.000 Date = 09/25/17 Time = 14:56:00

| Note: 1-4 EEL scale factors are being read from the topology file.

| Note: 1-4 VDW scale factors are being read from the topology file.
| Duplicated    0 dihedrals

| Duplicated    0 dihedrals

--------------------------------------------------------------------------------
   1.  RESOURCE   USE: 
--------------------------------------------------------------------------------

 getting box info from netcdf restart file
 NATOM  =    5986 NTYPES =      15 NBONH =    5926 MBONA  =      62
 NTHETH =      94 MTHETA =      84 NPHIH =     149 MPHIA  =     130
 NHPARM =       0 NPARM  =       0 NNB   =    8354 NRES   =    1962
 NBONA  =      62 NTHETA =      84 NPHIA =     130 NUMBND =      20
 NUMANG =      30 NPTRA  =      21 NATYP =      16 NPHB   =       1
 IFBOX  =       1 NMXRS  =      53 IFCAP =       0 NEXTRA =       0
 NCOPY  =       0

| Coordinate Index Table dimensions:     9    9    7
| Direct force subcell size =     4.5418    4.7790    4.8749

     BOX TYPE: RECTILINEAR

--------------------------------------------------------------------------------
   2.  CONTROL  DATA  FOR  THE  RUN
--------------------------------------------------------------------------------

INT                                                                             

General flags:
     imin    =       0, nmropt  =       0

Nature and format of input:
     ntx     =       5, irest   =       1, ntrx    =       1

Nature and format of output:
     ntxo    =       2, ntpr    =    1000, ntrx    =       1, ntwr    =   50000
     iwrap   =       1, ntwx    =   10000, ntwv    =       0, ntwe    =    1000
     ioutfm  =       1, ntwprt  =       0, idecomp =       0, rbornstat=      0

Potential function:
     ntf     =       1, ntb     =       2, igb     =       0, nsnb    =      25
     ipol    =       0, gbsa    =       0, iesp    =       0
     dielc   =   1.00000, cut     =   8.00000, intdiel =   1.00000

Frozen or restrained atoms:
     ibelly  =       0, ntr     =       0

Molecular dynamics:
     nstlim  =    500000, nscm    =      1000, nrespa  =         1
     t       =   0.00000, dt      =   0.00200, vlimit  =  -1.00000

Langevin dynamics temperature regulation:
     ig      =  914176
     temp0   = 298.00000, tempi   =   0.00000, gamma_ln=   2.00000

Pressure regulation:
     ntp     =       1
     pres0   =   1.01325, comp    =  44.60000, taup    =   2.00000
     Monte-Carlo Barostat:
     mcbarint  =     100

SHAKE:
     ntc     =       2, jfastw  =       0
     tol     =   0.00001

Free energy options:
     icfe    =       1, ifsc    =       0, klambda =       1
     clambda =  0.0000, scalpha =  0.5000, scbeta  = 12.0000
     sceeorder =       2
     dynlmb =  0.0000 logdvdl =       0

| Intermolecular bonds treatment:
|     no_intermolecular_bonds =       1

| Energy averages sample interval:
|     ene_avg_sampling =       1

Ewald parameters:
     verbose =       0, ew_type =       0, nbflag  =       1, use_pme =       1
     vdwmeth =       1, eedmeth =       1, netfrc  =       1
     Box X =   40.877   Box Y =   43.011   Box Z =   34.124
     Alpha =   90.000   Beta  =   90.000   Gamma =   90.000
     NFFT1 =   48       NFFT2 =   48       NFFT3 =   36
     Cutoff=    8.000   Tol   =0.100E-04
     Ewald Coefficient =  0.34864
     Interpolation order =    4
     TI Mask 1 :1; matches     53 atoms
     TI Mask 2 :2; matches     53 atoms
     TI region 1:    5933 atoms
     TI region 2:    5933 atoms
     Checking for mismatched coordinates.
 Noshake mask :1,2; matches     106 atoms.
| MONTE CARLO BAROSTAT IMPORTANT NOTE:
|   The Monte-Carlo barostat does not require the virial to adjust the system volume.
|   Since it is an expensive calculation, it is skipped for efficiency. A side-effect
|   is that the reported pressure is always 0 because it is not calculated.

--------------------------------------------------------------------------------
   3.  ATOMIC COORDINATES AND VELOCITIES
--------------------------------------------------------------------------------

INT                                                                             
 begin time read from input coords =    20.000 ps

 
 Number of triangulated 3-point waters found:     1960
   Removing shake constraints from C30   INT   1 -- H52   INT   1
   Removing shake constraints from C30   INT   1 -- H53   INT   1
   Removing shake constraints from C30   INT   1 -- H51   INT   1
   Removing shake constraints from C26   INT   1 -- H47   INT   1
   Removing shake constraints from C26   INT   1 -- H48   INT   1
   Removing shake constraints from C26   INT   1 -- H49   INT   1
   Removing shake constraints from C24   INT   1 -- H46   INT   1
   Removing shake constraints from N27   INT   1 -- H50   INT   1
   Removing shake constraints from C21   INT   1 -- H45   INT   1
   Removing shake constraints from C20   INT   1 -- H42   INT   1
   Removing shake constraints from C20   INT   1 -- H43   INT   1
   Removing shake constraints from C20   INT   1 -- H44   INT   1
   Removing shake constraints from C16   INT   1 -- H40   INT   1
   Removing shake constraints from C16   INT   1 -- H41   INT   1
   Removing shake constraints from N13   INT   1 -- H39   INT   1
   Removing shake constraints from N9    INT   1 -- H38   INT   1
   Removing shake constraints from N9    INT   1 -- H37   INT   1
   Removing shake constraints from C7    INT   1 -- H36   INT   1
   Removing shake constraints from C2    INT   1 -- H34   INT   1
   Removing shake constraints from C2    INT   1 -- H35   INT   1
   Removing shake constraints from C1    INT   1 -- H31   INT   1
   Removing shake constraints from C1    INT   1 -- H32   INT   1
   Removing shake constraints from C1    INT   1 -- H33   INT   1
   Removing shake constraints from C30   L1    2 -- H52   L1    2
   Removing shake constraints from C30   L1    2 -- H53   L1    2
   Removing shake constraints from C30   L1    2 -- H51   L1    2
   Removing shake constraints from C26   L1    2 -- H47   L1    2
   Removing shake constraints from C26   L1    2 -- H48   L1    2
   Removing shake constraints from C26   L1    2 -- H49   L1    2
   Removing shake constraints from C24   L1    2 -- H46   L1    2
   Removing shake constraints from N27   L1    2 -- H50   L1    2
   Removing shake constraints from C21   L1    2 -- H45   L1    2
   Removing shake constraints from C20   L1    2 -- H42   L1    2
   Removing shake constraints from C20   L1    2 -- H43   L1    2
   Removing shake constraints from C20   L1    2 -- H44   L1    2
   Removing shake constraints from C16   L1    2 -- H40   L1    2
   Removing shake constraints from C16   L1    2 -- H41   L1    2
   Removing shake constraints from N13   L1    2 -- H39   L1    2
   Removing shake constraints from N9    L1    2 -- H38   L1    2
   Removing shake constraints from N9    L1    2 -- H37   L1    2
   Removing shake constraints from C7    L1    2 -- H36   L1    2
   Removing shake constraints from C2    L1    2 -- H34   L1    2
   Removing shake constraints from C2    L1    2 -- H35   L1    2
   Removing shake constraints from C1    L1    2 -- H31   L1    2
   Removing shake constraints from C1    L1    2 -- H32   L1    2
   Removing shake constraints from C1    L1    2 -- H33   L1    2
 Number of shake restraints removed:       46

     Sum of charges for TI region  1 =   0.00001100
     Forcing neutrality...


     Sum of charges for TI region  2 =  -0.00001000
     Forcing neutrality...

| Dynamic Memory, Types Used:
| Reals              428736
| Integers           234688

| Nonbonded Pairs Initial Allocation:      999811

| GPU memory information (estimate):
| KB of GPU memory in use:     34113
| KB of CPU memory in use:      8001

