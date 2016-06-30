from configloader import load_config, get_config

def getKeys():
	#key_list = ['port', 'u', 'd', 'transfer_enable', 'passwd', 'enable' ]
	key_list = ['port', 'flow_up', 'flow_down', 'transfer', 'sspwd', 'enable' ]
	if get_config().API_INTERFACE == 'sspanelv3':
		key_list += ['method']
	elif get_config().API_INTERFACE == 'sspanelv3ssr':
		key_list += ['method', 'obfs', 'protocol']
	return key_list
	#return key_list + ['plan'] # append the column name 'plan'

def isTurnOn(row):
	return True
	#return row['plan'] == 'B' # then judge here

