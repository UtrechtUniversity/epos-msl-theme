#import types
#from logging import getLogger

from sqlalchemy.util import OrderedDict

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Custom_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    plugins.implements(plugins.IFacets, inherit=True)
    #if toolkit.check_ckan_version(min_version='2.5.0'):


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'custom_theme')
        toolkit.add_template_directory(config_, 'templates')

    # package_type is 'dataset' for Dataset menu option
    def dataset_facets(self, facets_dict, package_type):
        #return facets_dict

        if package_type == 'harvest':
            return facets_dict # + [('organization', 'Organization')]
        else:
            return OrderedDict([('frequency', 'Frequency'),
                            ('source_type',package_type),
                            ('organization', 'OrganisationLab'),
                            ('groups', 'Subdomain'),
			    ('keywords', 'Keywordssss'),
                            ('Publisher', 'CF publisher')
                           ])

