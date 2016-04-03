# Apply Prewitt filter
#
import sys, os
import numpy as np
from scipy.ndimage import prewitt
#
# Import the module with the I/O scaffolding of the External Attribute
#
sys.path.insert(0, os.path.join(sys.path[0], '..'))
import extattrib as xa

#
# These are the attribute parameters
#
xa.params = {
	'Input': 'Input',
	'Output': ['Average gradient', 'In-line gradient', 'Cross-line gradient', 'Z gradient'],
	'ZSampMargin' : {'Value': [-1,1], 'Hidden': True},
	'StepOut' : {'Value': [1,1], 'Hidden': True},
	'Help'    : 'https://gist.github.com/waynegm/84f323ec4aab3961c23d'
}
#
# Define the compute function
#
def doCompute():
#
# index of current trace position in Input numpy array
#
	ilndx = xa.SI['nrinl']//2
	crldx = xa.SI['nrcrl']//2
	while True:
		xa.doInput()
		xa.Output['In-line gradient'] = prewitt(xa.Input, axis=0)[ilndx,crldx,:]
		xa.Output['Cross-line gradient'] = prewitt(xa.Input, axis=1)[ilndx,crldx,:]
		xa.Output['Z gradient'] = prewitt(xa.Input, axis=2)[ilndx,crldx,:]
		xa.Output['Average gradient'] = (xa.Output['In-line gradient'] 
										+ xa.Output['Cross-line gradient'] 
										+ xa.Output['Z gradient'])/3
		xa.doOutput()
	
#
# Assign the compute function to the attribute
#
xa.doCompute = doCompute
#
# Do it
#
xa.run(sys.argv[1:])
  
