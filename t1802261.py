from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os.path as Path


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print('Created', event.src_path, round(Path.getsize(event.src_path) / 1024, 2))

    def on_modified(self, event):
        print('modified', event.src_path, round(Path.getsize(event.src_path) / 1024, 2))

    def on_deleted(self, event):
        print('deleted', event.src_path)


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
