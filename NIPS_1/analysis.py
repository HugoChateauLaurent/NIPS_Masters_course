import matplotlib.pyplot as plt
import numpy as np

epochs = 50

loss_hist = np.load('models/loss_history_'+'{:03d}'.format(epochs)+'.npz')
for varName in loss_hist:
	loss_histories=loss_hist[varName]

exec('results='+str(loss_histories))

print len(results['validation']), len([x for x in results['validation'] if x==0])
for key in results:
	results[key] = [x for x in results[key] if x!=0]
	# print key
	plt.plot(range(len(results[key])), results[key], label=key)

plt.legend()
plt.show()
