# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from mixpanel import Mixpanel

class MixpanelPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.EventHandlerPlugin):
	"""
	It responds to events, generates mixpanel data and registers it
	"""
	def on_after_startup(self):
		self._logger.info("Hello World! I want to log events!")

	def on_event(self,event,payload):
		mp = Mixpanel('9b06295006e9455aa2d1114c1a6fa556')
		user_id = '12345'
		mp.people_set(user_id, {
			'$printer_name'    : 'AlphaRobo',
			})
		if event=="PrintCancelled":
			# p = payload['file']
			self._logger.info("File Cancelled: {}".format(p))
			mp.track(user_id, "File Cancellation", payload)



	

__plugin_implementation__ = MixpanelPlugin()