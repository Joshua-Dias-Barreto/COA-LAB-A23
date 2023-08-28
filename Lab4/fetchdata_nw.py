files = [
    ["./needlemanwunsch/GTX480_gto/nw_GTX480_gto.txt", "./output/needlemanwunsch/nw_GTX480_gto_op.txt"],
    ["./needlemanwunsch/GTX480_lrr/nw_GTX480_lrr.txt", "./output/needlemanwunsch/nw_GTX480_lrr_op.txt"],
    ["./needlemanwunsch/GTX480_tl/nw_GTX480_tl.txt", "./output/needlemanwunsch/nw_GTX480_tl_op.txt"],
    ["./needlemanwunsch/Kepler_gto/nw_kepler_gto.txt", "./output/needlemanwunsch/nw_Kepler_gto_op.txt"],
    ["./needlemanwunsch/Kepler_lrr/nw_kepler_lrr.txt", "./output/needlemanwunsch/nw_Kepler_lrr_op.txt"],
    ["./needlemanwunsch/Kepler_tl/nw_kepler_tl.txt", "./output/needlemanwunsch/nw_Kepler_tk_op.txt"],
    ["./needlemanwunsch/QV100_gto/nw_qv100_gto.txt", "./output/needlemanwunsch/nw_qv100_gto_op.txt"],
    ["./needlemanwunsch/QV100_lrr/nw_qv100_lrr.txt", "./output/needlemanwunsch/nw_qv100_lrr_op.txt"],
    ["./needlemanwunsch/QV100_tl/nw_qv100_tl.txt", "./output/needlemanwunsch/nw_qv100_tl_op.txt"],
    ["./needlemanwunsch/RTX2060_gto/nw_rtx2060_gto.txt", "./output/needlemanwunsch/nw_rtx2060_gto_op.txt"],
    ["./needlemanwunsch/RTX2060_lrr/nw_rtx2060_lrr.txt", "./output/needlemanwunsch/nw_rtx2060_lrr_op.txt"],
    ["./needlemanwunsch/RTX2060_tl/nw_rtx2060_tl.txt", "./output/needlemanwunsch/nw_rtx2060_tl_op.txt"],
    ["./needlemanwunsch/TitanV_gto/nw_titanv_gto.txt", "./output/needlemanwunsch/nw_titanv_gto_op.txt"],
    ["./needlemanwunsch/TitanV_lrr/nw_titanv_lrr.txt", "./output/needlemanwunsch/nw_titanv_lrr_op.txt"],
    ["./needlemanwunsch/TitanV_tl/nw_titanv_tl.txt", "./output/needlemanwunsch/nw_titanv_tl_op.txt"],
    ["./needlemanwunsch/TitanX_gto/nw_titanx_gto.txt", "./output/needlemanwunsch/nw_titanx_gto_op.txt"],
    ["./needlemanwunsch/TitanX_lrr/nw_titanx_lrr.txt", "./output/needlemanwunsch/nw_titanx_lrr_op.txt"],
    ["./needlemanwunsch/TitanX_tl/nw_titanx_tl.txt", "./output/needlemanwunsch/nw_titanx_tl_op.txt"],
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
    "gpu_tot_ipc",
    "gpgpu_simulation_time"
]
fo=open("./output/needlemanwunsch/final_outputs.txt", "w")
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
    # fo.write(a[2])
    fo.write(a[2].split('_')[0].upper())
    fo.write(' ')
    fo.write(a[2].split('_')[1].upper())

    
    # fo.write(filepth[0])
    fo.write('\n')
    for m in dict.values():
        opfile.write(m.lstrip())
        fo.write(m.lstrip())
    # for each in opfile:
    #     fo.write(each)
    fo.write('\n')




# PathFinder_OUTPUT

# filesPF = [
#     ["./PathFinder_OUTPUT/GTX480/GTO/GTX480_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_GTX480_gto_op.txt"],
#     ["./PathFinder_OUTPUT/GTX480/LRR/GTX480_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_GTX480_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/GTX480/TL/GTX480_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_GTX480_tl_op.txt"],
#     ["./PathFinder_OUTPUT/Kepler_Titan/GTO/keplerTitan_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_Kepler_gto_op.txt"],
#     ["./PathFinder_OUTPUT/Kepler_Titan/LRR/keplerTitan_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_Kepler_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/Kepler_Titan/TL/keplerTitan_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_Kepler_tk_op.txt"],
#     ["./PathFinder_OUTPUT/QV100/GTO/QV100_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_qv100_gto_op.txt"],
#     ["./PathFinder_OUTPUT/QV100/LRR/QV100_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_qv100_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/QV100/TL/QV100_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_qv100_tl_op.txt"],
#     ["./PathFinder_OUTPUT/RTX2060/GTO/RTX2060_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_rtx2060_gto_op.txt"],
#     ["./PathFinder_OUTPUT/RTX2060/LRR/RTX2060_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_rtx2060_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/RTX2060/TL/RTX2060_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_rtx2060_tl_op.txt"],
#     ["./PathFinder_OUTPUT/TitanV/GTO/TitanV_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_titanv_gto_op.txt"],
#     ["./PathFinder_OUTPUT/TitanV/LRR/TitanV_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_titanv_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/TitanV/TL/TitanV_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_titanv_tl_op.txt"],
#     ["./PathFinder_OUTPUT/TitanX/GTO/TitanX_pathFinder_gto.txt", "./A4_extracted_data/pf_app/nw_titanx_gto_op.txt"],
#     ["./PathFinder_OUTPUT/TitanX/LRR/TitanX_pathFinder_lrr.txt", "./A4_extracted_data/pf_app/nw_titanx_lrr_op.txt"],
#     ["./PathFinder_OUTPUT/TitanX/TL/TitanX_pathFinder_tl.txt", "./A4_extracted_data/pf_app/nw_titanx_tl_op.txt"],
# ]


