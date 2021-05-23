import threading


class threader(threading.Thread):
    def __init__(self, function, **arguments):
        threading.Thread.__init__(self)
        self.func = function
        self.arguments = arguments
        self.return_val = None

    def run(self):
        self.return_val = self.func(**self.arguments)

    def join(self):
        threading.Thread.join(self)
        return self.return_val