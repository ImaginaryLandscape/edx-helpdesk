from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings, PluginContexts
)

class HelpdeskConfig(AppConfig):
    name = 'helpdesk'
    verbose_name = "Helpdesk"
    # for Django 3.2 support:
    # see:
    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.default_auto_field
    default_auto_field = 'django.db.models.AutoField'

    # edx django app plugin configuration:
    # https://edx.readthedocs.io/projects/edx-django-utils/en/latest/plugins/how_tos/how_to_create_a_plugin_app.html
    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: 'helpdesk',
                PluginURLs.APP_NAME: 'helpdesk',
                PluginURLs.REGEX: r'^/helpdesk/',
                PluginURLs.RELATIVE_PATH: 'helpdesk.urls',
            },
        },
    }
