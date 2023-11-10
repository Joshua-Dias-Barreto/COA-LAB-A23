# COA End Semester Project - Group 10

## Group Members

- Ishan Mardani (21CS01023)
- Akshit Dudeja (21CS01026)
- Joshua Dias Barreto (21CS01075)
- Vishnu Tirth Bysani (21CS01077)
- Tushar Joshi (21CS01078)

# KAWS

## Kernel Aware Warp Scheduling

In normal scheduling policy, after the maximum number of CTAs (Cooperative Thread Arrays) have been issued to a SM, if a CTA finishes execution, there are no more CTAs left to be issued. This leads to resource underutilization. To prevent this we will use KAWS scheduling policy, which will do progress based scheduling after the last CTA has been issued to give more priority to processes with less progress or number instructions executed. This will help in finishing the execution of the last CTA faster and therfore, limit resource underutilisation.

 <img width="1000" src="images/coa_2.png">

# Warp Sharing Mechanism

A supplemental concept to KAWS, to reduce stall cycles, is to implement warp sharing. In this policy we utilize the available OCUs (Operand Collector Units) from all warp schedulers if the OCU corresponding to that specific warp instruction is not available in the scheduler that the process is currently allocated to.

<img width="1000" src="images/coa_1.png">

<br>

# Modifications in Code

To see the changes in code, search for "_KAWS-Changes_" in the files shader.cc, shader.h, abstract_hardware_model.h, scheduler_id.h and gpgpusim_entrypoint.cc in the /EndSem_Project/gpgpu-sim_distribution/src.

<br>

# Evaluation

# IPC (Instruction/Cycle)

|             | PF     | HS     | 3DCV   | 3MM    | BFS    | NN     | NW    |
| ----------- | ------ | ------ | ------ | ------ | ------ | ------ | ----- |
| **LRR**     | 677.49 | 2310.1 | 250.77 | 208.57 | 98.82  | 159.97 | 11.57 |
| **LRR+WS**  | 678.91 | 2322.3 | 251.09 | 211.82 | 99.02  | 159.27 | 11.58 |
| **GTO**     | 707.84 | 2558.4 | 263.58 | 201.89 | 101.51 | 158.96 | 11.59 |
| **GTO+WS**  | 708.92 | 2562.8 | 263.78 | 205.06 | 101.87 | 158.03 | 11.61 |
| **KAWS**    | 717.30 | 2612.2 | 270.88 | 211.36 | 102.71 | 159.55 | 11.63 |
| **KAWS+WS** | 718.95 | 2616.7 | 271.08 | 214.55 | 103.33 | 160.33 | 11.65 |

## IPC Performance of Different Warp Schedulers (Normalised to LRR)

<img width="1000" src="EndSem_img/IPC.png">

## With and Without Warp Sharing (Normalised to LRR without Warp Sharing)

### KAWS

|                                            | PF     | HS     | 3DCV   | 3MM    | BFS    | NN     | NW     |
| ------------------------------------------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| **With Warp Sharing**                      | 106.12 | 113.27 | 108.10 | 102.87 | 104.57 | 99.74  | 100.69 |
| **Without Warp Sharing**                   | 105.89 | 113.08 | 108.02 | 101.34 | 103.93 | 100.23 | 100.54 |
| **Performance Change due to Warp Sharing** | 0.23   | 0.19   | 0.08   | 1.53   | 0.64   | -0.49  | 0.15   |

### GTO

|                                            | PF     | HS     | 3DCV   | 3MM   | BFS    | NN    | NW     |
| ------------------------------------------ | ------ | ------ | ------ | ----- | ------ | ----- | ------ |
| **With Warp Sharing**                      | 104.64 | 110.94 | 105.19 | 98.32 | 103.09 | 98.79 | 100.34 |
| **Without Warp Sharing**                   | 104.48 | 110.75 | 105.11 | 96.80 | 102.73 | 99.37 | 100.17 |
| **Performance Change due to Warp Sharing** | 0.16   | 0.19   | 0.08   | 1.52  | 0.36   | -0.58 | 0.17   |

### LRR

|                                            | PF     | HS     | 3DCV   | 3MM    | BFS    | NN    | NW     |
| ------------------------------------------ | ------ | ------ | ------ | ------ | ------ | ----- | ------ |
| **With Warp Sharing**                      | 100.21 | 100.53 | 100.13 | 101.56 | 100.21 | 99.56 | 100.09 |
| **Without Warp Sharing**                   | 100    | 100    | 100    | 100    | 100    | 100   | 100    |
| **Performance Change due to Warp Sharing** | 0.21   | 0.53   | 0.13   | 1.56   | 0.21   | -0.44 | 0.09   |

<br>

# Stall Cycles

## Total Simulation Cycles (gpu_tot_sim_cycles)

(Normalised to LRR)

<img width="1000" src="EndSem_img/gpu_tot_sim_cycle.png">

Although our values of the evaluation metrics(IPC, Stall Cycles) do not completely match with that of the research paper, the values have a similar trend as given in the research paper. This is becuase we scaled down the inputs to the applications/benchmarks so that they execute faster. Hence, we can see a similar trend in our data if not the exact same values.
