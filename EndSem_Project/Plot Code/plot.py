import matplotlib.pyplot as plt
# from google.colab import files

# Example data
applications = ['PF', 'HS','3DCV', '3MM','BFS', 'NN', 'NW', 'Average']

lrr_pf=677.49
gto_pf=707.84
kaws_pf=718.95

lrr_hs=2310.1
gto_hs=2558.4 
kaws_hs=2616.7

lrr_3dcv=250.77
gto_3dcv=263.58
kaws_3dcv=271.08

lrr_3mm=208.57
gto_3mm=201.89
kaws_3mm=214.55

lrr_bfs=98.82
gto_bfs=101.51
kaws_bfs=103.33

lrr_nn=159.97
gto_nn=158.96
kaws_nn=159.55

lrr_nw=11.57
gto_nw=11.59
kaws_nw=11.65

lrr_average=531.04
gto_average=572.11
kaws_average=585.37

title="IPC Comparison with Different Warp Schedulers"


lrr = [
        lrr_pf,
        lrr_hs ,
        lrr_3dcv ,
        lrr_3mm ,
        lrr_bfs,
        lrr_nn ,
        lrr_nw ,
        lrr_average
    ]

gto = [
        gto_pf,
        gto_hs,
        gto_3dcv ,
        gto_3mm ,
        gto_bfs,
        gto_nn ,
        gto_nw ,
        gto_average
    ]

kaws = [
        kaws_pf,
        kaws_hs ,
        kaws_3dcv ,
        kaws_3mm ,
        kaws_bfs,
        kaws_nn ,
        kaws_nw ,
        kaws_average
    ]
gto= [(100*value)/float(lrr[index]) for index,value in enumerate(gto)]
kaws= [(100*value)/float(lrr[index]) for index,value in enumerate(kaws)]
lrr= [(100*value)/float(lrr[index]) for index,value in enumerate(lrr)]
plt.figure(figsize=(15, 10))

bar_width = 0.29  # Width of the bars
index = range(len(applications))  # Index for x-axis positioning

# Plot IPC for Scheduler 1

# Plot IPC for Scheduler 2

bars1 = plt.bar(index, lrr, width=bar_width, label='LRR')
bars2 = plt.bar([i + bar_width for i in index], gto, width=bar_width, label='GTO')
# Plot IPC for Scheduler 3
bars3 = plt.bar([i + 2 * bar_width for i in index], kaws, width=bar_width, label='KAWS+WS')

# Add height labels inside the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        va = 'bottom' if bars == bars3 else 'bottom'
        if bars != bars1 :
         plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:0.2f}',
                  ha='center', va=va, fontsize=8)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Adjust x-axis labels and tick positions
plt.xlabel('Application')
plt.ylabel('Instruction per Cycle (IPC) Normalized to LRR')
plt.title(title)
plt.xticks([i + bar_width for i in index], applications)
plt.legend(loc='upper left',bbox_to_anchor=(1,1))

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()