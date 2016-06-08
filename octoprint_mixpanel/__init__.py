# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class MixpanelPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.EventHandlerPlugin):
	"""
	A class used to test plugin integration with Octoprint
	"""
	def on_after_startup(self):
		self._logger.info("Hello World! I want to log events!")

	def on_event(self,event,payload):
		if event=="PrintCancelled":
			p = payload['file']
			self._logger.info("File Cancelled: {}".format(p))
	

__plugin_name__ = "Mixpanel"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Hello World! I am a mixpanel integration plugin"
__plugin_implementation__ = MixpanelPlugin()