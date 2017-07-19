import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Custom_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'custom_theme')
        toolkit.add_template_directory(config_, 'templates')
