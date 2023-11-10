import matplotlib.pyplot as plt
# from google.colab import files

# Example data
applications = ['PF', 'HS','3DCV', '3MM']

lrr_pf=18813
gto_pf=18316
kaws_pf=18249

lrr_hs=7159
gto_hs=6929
kaws_hs=6686

lrr_3dcv=7146
gto_3dcv=7146
kaws_3dcv=7135

lrr_3mm=58522
gto_3mm=60143
kaws_3mm=58484

title="IPC Comparison with Different Warp Schedulers"


lrr = [
        lrr_pf,
        lrr_hs ,
        lrr_3dcv ,
        lrr_3mm ,
    ]

gto = [
        gto_pf,
        gto_hs,
        gto_3dcv ,
        gto_3mm ,
    ]

kaws = [
        kaws_pf,
        kaws_hs ,
        kaws_3dcv ,
        kaws_3mm ,
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