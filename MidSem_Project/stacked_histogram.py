# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create data
df = pd.DataFrame([['Input_1', 9.529832, 1.292300, 0.241597, 54.818694, 34.117577], ['Input_2', 9.982542, 1.323413, 0.19508, 61.831175, 26.743362], ['Input_3', 10.338198, 1.360554, 0.095865, 65.696828, 22.508554]],
                  columns=['', 'Issued', 'XALU','XMEM','Waiting', 'Other'])

colors = ['#39FF14', 'yellow', 'red', 'cyan', 'magenta']
df.plot(x='', kind='bar', stacked=True,
        title='Warps State Breakdown', rot = 0, color=colors)
plt.xlim([-0.5, 4])

plt.yticks(np.arange(0, 101, 10))
plt.show()
plt.savefig("/content/warps_state_breakdown.png")