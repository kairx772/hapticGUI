import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from scipy import stats
import pandas as pd

#print (len(sys.argv))

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    csv_input = pd.read_csv(arg1)

if len(sys.argv) > 2:
    arg2 = sys.argv[2]
    csv_input2 = pd.read_csv(arg2)
else:
    arg2 = sys.argv[1]
    csv_input2 = pd.read_csv(arg2)


'''
csv_input['ID'] = np.log2((2*((((csv_input['sq_posx'] - csv_input['cur_posx'])**2 + (csv_input['sq_posy'] - csv_input['cur_posy'])**2)**(0.5))/csv_input['sq_wid'])))
csv_input.to_csv(arg1, index=False)
tips2 = csv_input
slope, intercept, r_value, p_value, std_err = stats.linregress(tips2['ID'],tips2['movtime'])

csv_input2['ID'] = np.log2((2*((((csv_input2['sq_posx'] - csv_input2['cur_posx'])**2 + (csv_input2['sq_posy'] - csv_input2['cur_posy'])**2)**(0.5))/csv_input2['sq_wid'])))
csv_input2.to_csv(arg2, index=False)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(csv_input2['ID'],csv_input2['movtime'])


ax = sns.regplot(x="ID", y="movtime", data=tips2, color='b', line_kws={'label':"y={:.3f}x+{:.3f}, {}".format(slope,intercept,arg1)})
ax.legend()




if len(sys.argv) > 2:
    ax2 = sns.regplot(x="ID", y="movtime", data=csv_input2, color='r', line_kws={'label':"y={:.3f}x+{:.3f}, {}".format(slope2,intercept2,arg2)})
    ax2.legend()pd

df=pd.DataFrame({'xvalues': range(1,101), 'yvalues': np.random.randn(100) })
'''

#csv_input['d_t'] = csv_input['time'] - 
#csv_input['time'].insert(0.1)
csv_input['d_t'] = csv_input.time.diff()
csv_input['d_x'] = csv_input.cur_x.diff()
csv_input['d_y'] = csv_input.cur_y.diff()
csv_input['cur_v'] = ((csv_input['d_x'])**2+(csv_input['d_y'])**2)**(0.5)/csv_input['d_t']
#csv_input['cur_v'] = ((csv_input['d_x'])**2+(csv_input['d_x'])**2)**(0.5)/csv_input['d_t'] 
csv_input.to_csv('testdata.ods', index=False)

# plotpd
plt.plot( 'time', 'd_t', data=csv_input)
#plt.plot( 'time', 'cur_x', data=csv_input)
plt.show()

