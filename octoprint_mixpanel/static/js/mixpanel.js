/*
 * View model for OctoPrint-Mixpanel
 *
 * Author: Victor E Fimbres
 * License: TODO
 */
$(function() {
    function MixpanelViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        MixpanelViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_mixpanel, #tab_plugin_mixpanel, ...
        [ /* ... */ ]
    ]);
});
