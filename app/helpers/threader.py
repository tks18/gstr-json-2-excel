import threading


class threader(threading.Thread):
    def __init__(self, function, **arguments):
        threading.Thread.__init__(self)
        self.func = function
        self.arguments = arguments
        self.return_val = None
        self.error = None

    def run(self):
        try:
            self.return_val = self.func(**self.arguments)
        except Exception as error:
            self.error = error

    def join(self):
        threading.Thread.join(self)
        return self.return_val

    def get_status(self):
        return_value = {"alive": threading.Thread.is_alive(self), "error": self.error}
        return return_value
