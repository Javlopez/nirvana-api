"""Ping handler"""

import falcon


class Ping:
    """Ping handler"""

    def on_get(self, req, resp):
        """Get handler for ping endpoint"""
        resp.media = {"ping": True}
        resp.status = falcon.HTTP_200
