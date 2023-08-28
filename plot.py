import matplotlib.pyplot as plt

# Example data
applications = ['BFS', 'Path Finder', 'Needleman Wunsch']
gpu="RTX2060"
fn=f"{gpu}_ipc"
gto_bfs=121.84
lrr_bfs=120.37
tl_bfs=122.26

gto_nw=3.64
lrr_nw=3.64
tl_nw=3.645

gto_pf=657.16
lrr_pf=638.54
tl_pf=642.20
title=f"IPC Comparison with Different Warp Schedulers for {gpu}"

gto = [
        gto_bfs,
        gto_pf,
        gto_nw
    ]
lrr = [
        lrr_bfs,
        lrr_pf,
        lrr_nw
    ]
ipc = [
        tl_bfs,
        tl_pf,
        tl_nw
    ]



# Create the plot
plt.figure(figsize=(10, 6))

bar_width = 0.2  # Width of the bars
index = range(len(applications))  # Index for x-axis positioning

# Plot IPC for Scheduler 1
bars1 = plt.bar(index, gto, width=bar_width, label='Greedy then Oldest (GTO)')

# Plot IPC for Scheduler 2
bars2 = plt.bar([i + bar_width for i in index], lrr, width=bar_width, label='Loose Round Robin (LRR)')

# Plot IPC for Scheduler 3
bars3 = plt.bar([i + 2 * bar_width for i in index], ipc, width=bar_width, label='Two Level (TL)')

# Add height labels inside the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{height:.2f}', ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Adjust x-axis labels and tick positions
plt.xlabel('Application')
plt.ylabel('Instruction per Cycle (IPC)')
plt.title(title)
plt.xticks([i + bar_width for i in index], applications)
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
# plt.show()

# save the plot as a file
plt.savefig(f'./Lab4/graphs/{fn}.png', bbox_inches='tight')