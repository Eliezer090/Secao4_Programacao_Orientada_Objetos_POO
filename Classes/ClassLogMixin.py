class LogMixin:
    @staticmethod
    def white(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.white(f'INFO: {msg}')

    def log_error(self, msg):
        self.white(f'ERROR: {msg}')
