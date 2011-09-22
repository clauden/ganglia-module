import os
import random

def get_instrumentation(name):
	return random.random()

def metric_init(params):
	x = {
		'name'		: 'foo',
		'call_back'	: get_instrumentation,
		'time_max'	: 60,
		'value_type'	: 'float',
		'units'		: '',
		'slope'		: 'both',
		'format'	: '%f',
		'description'	: 'some random metric'
	}

	return [x]

def metric_cleanup():
	pass


if __name__ == '__main__':
	metric_init(None)
	print instrumentation()

