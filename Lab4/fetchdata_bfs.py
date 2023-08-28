
files = [
    ["./bfs/GTX480/GTO/GTX480_gto_bfs.txt", "./output/bfs/pf_GTX480_gto_op.txt"],
    ["./bfs/GTX480/LRR/GTX480_lrr_bfs.txt", "./output/bfs/pf_GTX480_lrr_op.txt"],
    ["./bfs/GTX480/TL/GTX480_tl_bfs.txt", "./output/bfs/pf_GTX480_tl_op.txt"],
    ["./bfs/KeplerTitan/GTO/gtxkeplerTitan_gto_bfs.txt", "./output/bfs/pf_Kepler_gto_op.txt"],
    ["./bfs/KeplerTitan/LRR/gtxkeplerTitan_lrr_bfs.txt", "./output/bfs/pf_Kepler_lrr_op.txt"],
    ["./bfs/KeplerTitan/TL/gtxkeplerTitan_tl_bfs.txt", "./output/bfs/pf_Kepler_tk_op.txt"],
    ["./bfs/QV100/GTO/QV100_gto_bfs.txt", "./output/bfs/pf_qv100_gto_op.txt"],
    ["./bfs/QV100/LRR/QV100_lrr_bfs.txt", "./output/bfs/pf_qv100_lrr_op.txt"],
    ["./bfs/QV100/TL/QV100_tl_bfs.txt", "./output/bfs/pf_qv100_tl_op.txt"],
    ["./bfs/RTX2060/GTO/RTX2060_gto_bfs.txt", "./output/bfs/pf_rtx2060_gto_op.txt"],
    ["./bfs/RTX2060/LRR/RTX2060_lrr_bfs.txt", "./output/bfs/pf_rtx2060_lrr_op.txt"],
    ["./bfs/RTX2060/TL/RTX2060_tl_bfs.txt", "./output/bfs/pf_rtx2060_tl_op.txt"],
    ["./bfs/TitanV/GTO/TitanV_gto_bfs.txt", "./output/bfs/pf_titanv_gto_op.txt"],
    ["./bfs/TitanV/LRR/TitanV_lrr_bfs.txt", "./output/bfs/pf_titanv_lrr_op.txt"],
    ["./bfs/TitanV/TL/TitanV_tl_bfs.txt", "./output/bfs/pf_titanv_tl_op.txt"],
    ["./bfs/TitanX/GTO/titanX_gto_bfs.txt", "./output/bfs/pf_titanx_gto_op.txt"],
    ["./bfs/TitanX/LRR/titanX_lrr_bfs.txt", "./output/bfs/pf_titanx_lrr_op.txt"],
    ["./bfs/TitanX/TL/titanX_tl_bfs.txt", "./output/bfs/pf_titanx_tl_op.txt"],
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
    "gpgpu_simulation_time",
    "gpu_tot_ipc"
]
fo=open("./output/bfs/final_outputs.txt", "w")
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

