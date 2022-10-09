import threading


class DownloaderThread(threading.Thread):

    def __init__(self, num):
        self.num =num
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread execution started')
            for x in range(self.num):
                print(x)
        except Exception as e:
            print(e)