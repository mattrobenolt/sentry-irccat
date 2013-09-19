import socket

from django import forms
from sentry.plugins.bases.notify import NotificationPlugin, NotificationConfigurationForm
import sentry_irccat


class IRCCatConfigurationForm(NotificationConfigurationForm):
    host = forms.CharField(label='Host', required=False, help_text='irccat host')
    port = forms.IntegerField(label='Port', required=False, help_text='irccat port')
    channel = forms.CharField(label='Channel', required=False, help_text='channel')


class IRCCatMessage(NotificationPlugin):
    title = 'IRCCat'
    conf_key = 'irccat'
    slug = 'irccat'
    version = sentry_irccat.VERSION
    author = 'Russ Garrett'
    author_url = 'https://github.com/russss'
    project_conf_form = IRCCatConfigurationForm

    def is_configured(self, project):
        return all(self.get_option(k, project) for k in ('host', 'port', 'channel'))

    def notify_users(self, group, event, fail_silently=False):
        project = group.project

        link = group.get_absolute_url()
        message = '[sentry %s] %s (%s)' % (
            project.name.encode('utf-8'),
            event.message,
            link,
        )
        try:
            self.send_payload(project, message)
        except Exception:
            if fail_silently:
                return
            raise

    def send_payload(self, project,  message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.get_option('host', project), self.get_option('port', project)))
        msg = "%s %s\r\n" % (self.get_option('channel', project), message)
        sock.send(msg)
        sock.close()
