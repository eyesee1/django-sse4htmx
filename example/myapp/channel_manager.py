from django_eventstream.channelmanager import DefaultChannelManager


class MyChannelManager(DefaultChannelManager):
    def can_read_channel(self, user, channel):
        return True
