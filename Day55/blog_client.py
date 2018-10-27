import uplink
import requests

class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://consumer_services_api.talkpython.fm')


    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """ Get's all blog entries from the server. """


    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Get's a specific  blog entry from the server. """
