from watchdog.observers import Observer
from watchdog.events import *
import time
from copyFile import copyFile
from datToJpg import datToJpg


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # def on_moved(self, event):
    #     if event.is_directory:
    #         print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
    #     else:
    #         print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory is False:
            # print("directory created:{0}".format(event.src_path))
            # else:
            if 'Tiny' in event.src_path:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/Tiny/')
            elif 'send' in event.src_path:
                print('Send file.')
            else:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/')

                # def on_deleted(self, event):
                #     if event.is_directory:
                #         print("directory deleted:{0}".format(event.src_path))
                #     else:
                #         print("file deleted:{0}".format(event.src_path))

                # def on_modified(self, event):
                #     if event.is_directory:
                #         print("directory modified:{0}".format(event.src_path))
                #     else:
                #         print("file modified:{0}".format(event.src_path))


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "C:/Users/admin/Documents/WeChat Files/xingqitiantsut99/Data", True)
    observer.start()
    print('Observer start.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
