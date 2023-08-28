
files = [
    ["./pathfinder/GTX480/GTO/GTX480_pathFinder_gto.txt", "./output/pathfinder/pf_GTX480_gto_op.txt"],
    ["./pathfinder/GTX480/LRR/GTX480_pathFinder_lrr.txt", "./output/pathfinder/pf_GTX480_lrr_op.txt"],
    ["./pathfinder/GTX480/TL/GTX480_pathFinder_tl.txt", "./output/pathfinder/pf_GTX480_tl_op.txt"],
    ["./pathfinder/Kepler_Titan/GTO/keplerTitan_pathFinder_gto.txt", "./output/pathfinder/pf_Kepler_gto_op.txt"],
    ["./pathfinder/Kepler_Titan/LRR/keplerTitan_pathFinder_lrr.txt", "./output/pathfinder/pf_Kepler_lrr_op.txt"],
    ["./pathfinder/Kepler_Titan/TL/keplerTitan_pathFinder_tl.txt", "./output/pathfinder/pf_Kepler_tk_op.txt"],
    ["./pathfinder/QV100/GTO/QV100_pathFinder_gto.txt", "./output/pathfinder/pf_qv100_gto_op.txt"],
    ["./pathfinder/QV100/LRR/QV100_pathFinder_lrr.txt", "./output/pathfinder/pf_qv100_lrr_op.txt"],
    ["./pathfinder/QV100/TL/QV100_pathFinder_tl.txt", "./output/pathfinder/pf_qv100_tl_op.txt"],
    ["./pathfinder/RTX2060/GTO/RTX2060_pathFinder_gto.txt", "./output/pathfinder/pf_rtx2060_gto_op.txt"],
    ["./pathfinder/RTX2060/LRR/RTX2060_pathFinder_lrr.txt", "./output/pathfinder/pf_rtx2060_lrr_op.txt"],
    ["./pathfinder/RTX2060/TL/RTX2060_pathFinder_tl.txt", "./output/pathfinder/pf_rtx2060_tl_op.txt"],
    ["./pathfinder/TitanV/GTO/TitanV_pathFinder_gto.txt", "./output/pathfinder/pf_titanv_gto_op.txt"],
    ["./pathfinder/TitanV/LRR/TitanV_pathFinder_lrr.txt", "./output/pathfinder/pf_titanv_lrr_op.txt"],
    ["./pathfinder/TitanV/TL/TitanV_pathFinder_tl.txt", "./output/pathfinder/pf_titanv_tl_op.txt"],
    ["./pathfinder/TitanX/GTO/TitanX_pathFinder_gto.txt", "./output/pathfinder/pf_titanx_gto_op.txt"],
    ["./pathfinder/TitanX/LRR/TitanX_pathFinder_lrr.txt", "./output/pathfinder/pf_titanx_lrr_op.txt"],
    ["./pathfinder/TitanX/TL/TitanX_pathFinder_tl.txt", "./output/pathfinder/pf_titanx_tl_op.txt"],
]



# matches = ["L1D_total_cache_accesses", "L1D_total_cache_misses", "L1D_total_cache_miss_rate","L2_total_cache_accesses", "L2_total_cache_misses", "L2_total_cache_miss_rate", "avg_icnt2mem_latency", "avg_icnt2sh_latency", "averagemflatency"]
matches = [
    "L1D_total_cache_accesses",
    "L1D_total_cache_misses",
    "L1D_total_cache_miss_rate",
    "L2_total_cache_accesses",
    "L2_total_cache_misses",
    "L2_total_cache_miss_rate",
    "(inst/sec)",
    "(cycle/sec)",
    "gpgpu_simulation_time"
]
fo=open("./output/pathfinder/final_outputs.txt", "w")
for filepth in files:
    file = open(filepth[0], 'r')
    opfile = open(filepth[1], 'w')
    dict={}
    for each in file:
        for m in matches:
            if m in each:
                dict[m]=each
    a=filepth[0].split('/')
    fo.write(a[1].upper())
    fo.write(' ')
    fo.write(a[2].upper())
    fo.write(' ')
    fo.write(a[3].upper())

    # fo.write(filepth[0])
    fo.write('\n')
    for m in dict.values():
        opfile.write(m.lstrip())
        fo.write(m.lstrip())
    # for each in opfile:
    #     fo.write(each)
    fo.write('\n')

