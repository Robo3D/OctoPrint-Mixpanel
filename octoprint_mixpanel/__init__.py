# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from mixpanel import Mixpanel
from datetime import datetime
# from octoprint.filemanager.analysis import GcodeAnalysisQueue 

###HELPER FUNCTIONS###################
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
	# TODO Is GcodeAnalysisQueue the best way to get this data? HOw 
	pass
	d = GcodeAnalysisQueue()
	return d['filament']['tool1']['volume']

def generate_mixpanel_payload (event, payload):
	"""
	Helper function. generates and returns the mixpanel payload based on the printer's event.
	There are 2 types of payloads. Standard and Special. Standard payloads are subject to the same processing. For example, Standard payloads will include the key-values octoprint created plus a date and time key. Special payloads will include the key-values of Standard plus their own special key-value pairs unique to that event. For example, a PrintStart event will have a volumetric data included.

	TODO: Hook that appends special payload. 
	"""
	special_events = ['PrintStarted']
	
	if not valid_event(event):
		return None

	dt = datetime.utcnow()
	payload['date'] = str(dt.date())
	payload['time'] = str(dt.time())

	# if event in special_events:
	# 	payload['volume'] = volumetric_data()

	return payload
#################################

class MixpanelPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.EventHandlerPlugin,octoprint.plugin.SettingsPlugin):
	"""
	It responds to events, generates mixpanel data and registers it to mixpanel server
	"""
	def on_after_startup(self):
		self._logger.info("Hello World! I want to log events!")

	def on_event(self,event,payload):
		if not hasattr(self, 'mp'):
			# Attach static but essential mixpanel information to this Plugin instance if not already. The 2 pieces of static data are the token that links to the specific mixpanel project and the printer's id to which printer event will be correlated.

			# token = self._settings.get(['token'])
			token = '9b06295006e9455aa2d1114c1a6fa556'
			self.printer_id = 'RoboTest'
			# self.printer_id = self._settings.get(['printer_id'])
			self.mp = Mixpanel(token)

		mixpanel_payload = generate_mixpanel_payload(event, payload)
		if mixpanel_payload:
			self.mp.track(self.printer_id, event, mixpanel_payload)
		else:
			return 

__plugin_implementation__ = MixpanelPlugin()