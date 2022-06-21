"""MockApi handler"""

import falcon
import random


class MockApi:
    """MockApi handler"""

    def on_get(self, req, resp):
        """Get handler for ping endpoint"""

        member_id = int(req.get_param('member_id', default=1))
        resp.media = {
            "deductible": self.generate_values(member_id),
            "stop_loss": self.generate_values(member_id),
            "oop_max": self.generate_values(member_id),
        }
        resp.status = falcon.HTTP_200

    def generate_values(self, member_id) -> int:
        return random.randint(1, member_id) * 1000
