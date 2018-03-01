from watchdog.observers import Observer
from watchdog.events import *
import time
from copyFile import copyFile


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.copyable = False

    def on_created(self, event):
        if event.is_directory is False:
            if 'Tiny' in event.src_path:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/Tiny/')
            elif 'send' in event.src_path:
                print('Send file.')
            else:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/')

    #def on_deleted(self, event):


    #def on_modified(self, event):



if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "C:/Users/admin/Documents/WeChat Files/xingqitiantsut99/Data", True)
    observer.start()
    print('Observer start.', time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
