class MoveError(object):

    def __init__(self, msg):
        self.error_msg = msg

    def get_error(self):
        return self.error_msg