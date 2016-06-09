from datetime import datetime
from octoprint.filemanager.analysis import GcodeAnalysisQueue 

def valid_event(event):
	"""
	Makes sure that event is valid for mixpanel. Returns booleans.
	"""
	return event in [
		'Error',
		'PrintStarted',
		'PrintFailed',
		'PrintDone',
		'PrintCancelled',
	]

def volumetric_data():
	d = GcodeAnalysisQueue()
	return d['filament']['tool1']['volume']

def generate_mixpanel_payload (event, payload):
	"""
	Helper function. generates and returns the mixpanel payload from the printer's event data.
	"""
	special_events = ['PrintStarted']
	
	if not valid_event(event):
		return None

	dt = datetime.utcnow()
	payload['date'] = dt.date()
	payload['time'] = dt.time()

	if event in special_events:
		payload['volume'] = volumetric_data()

	return payload
