# COA End Semester Project - Group 10
## Group Members
- Ishan Mardani (21CS01023)
- Akshit Dudeja (21CS01026)
- Joshua Dias Barreto (21CS01075)
- Vishnu Tirth Bysani (21CS01076)
- Tushar Joshi (21CS01078)

## IPC Performance of Different Warp Schedulers Normalised to LRR
<img width="1000" src="endsem_img/endsem_img1.png">

## KAWS with and without Warp Sharing (Normalised to LRR without Warp Sharing)
|       | PF    | HS    | 3DCV     | 3MM    |
|-------|------|------|-------|------|
| **With Warp Sharing** | 106.12  | 113.27  | 108.02  | 102.87  |
| **Without Warp Sharing** | 105.89 | 113.08 | 108.10 | 101.34 |
| **Performance Increment with Warp Sharing** | 0.23 | 0.19 | -0.08 | 1.53 |

## GTO with and without Warp Sharing (Normalised to LRR without Warp Sharing)
|       | PF    | HS    | 3DCV     | 3MM    |
|-------|------|------|-------|------|
| **With Warp Sharing** | 104.56  | 110.94  | 105.11  | 98.32  |
| **Without Warp Sharing** | 104.48 | 110.75 | 105.19 | 96.80 |
| **Performance Increment with Warp Sharing** | 0.08 | 0.19 | -0.08 | 1.52 |

## LRR with and without Warp Sharing (Normalised to LRR without Warp Sharing)
|       | PF    | HS    | 3DCV     | 3MM    |
|-------|------|------|-------|------|
| **With Warp Sharing** | 100.21  | 100.53  | 100.13  | 101.56  |
| **Without Warp Sharing** | 100 | 100 | 100 | 100 |
| **Performance Increment with Warp Sharing** | 0.21 | 0.53 | 0.13 | 0.156 |
