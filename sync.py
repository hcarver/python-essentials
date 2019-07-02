import requests
import os
import json
import hashlib
import time

WATCHED_EXTS = [".py"]
IGNORE_DIRS = [".git"]

def swsync():
    print("  _____ _    _ _ _            __          ___           _      ")
    print(" / ____| |  (_) | |           \\ \\        / / |         | |     ")
    print("| (___ | | ___| | | ___ _ __   \\ \\  /\\  / /| |__   __ _| | ___ ")
    print(" \\___ \\| |/ / | | |/ _ \\ '__|   \\ \\/  \\/ / | '_ \\ / _` | |/ _ \\")
    print(" ____) |   <| | | |  __/ |       \\  /\\  /  | | | | (_| | |  __/")
    print("|_____/|_|\\_\\_|_|_|\\___|_|        \\/  \\/   |_| |_|\\__,_|_|\\___| ")
    print("")
    attendanceId = input(
            "Please copy and paste your ID from the course page here and press enter.\n"
            )
    print("")
    print("Great! We're going to start watching this directory for changes so that the trainer can see your progress.")
    print("Hit Ctrl+C to stop.")

    watcher = Watcher(attendanceId)
    while True:
        watcher.pollDirectoryForChanges(".")
        time.sleep(1)

class Watcher:
    def __init__(self, attendanceId):
        self.attendanceId = attendanceId
        self.fileHashes = {}

    def putUpdate(self, path):
        with open(path, "r") as f:
            data = json.dumps({
                "relative_path": path,
                "contents": f.read()
                })

            hostname = os.environ.get('SERVER_URL', "https://train.skillerwhale.com")
            path = "/attendances/%s/file_snapshots" % self.attendanceId
            uri = requests.compat.urljoin(hostname, path)

            headers = {
                    "Content-Type": "application/json",
                    "Content-Length": str(len(data))
                    }

            response = requests.post(uri, data=data, headers=headers)
            print(response.status_code)
            txt = response.text
            if txt:
                print(txt)

    def hashFile(self, path):
        with open(path, "r") as f:
            contents = f.read()
            return hashlib.md5(contents.encode("utf-8")).hexdigest()

    def pollDirectoryForChanges(self, dirPath):
        if os.path.basename(dirPath) in IGNORE_DIRS:
            return
        for filename in os.listdir(dirPath):
            newPath = os.path.join(dirPath, filename)
            if not os.path.isfile(newPath):
              self.pollDirectoryForChanges(newPath)
            else:
                _, extname = os.path.splitext(newPath)
                if extname in WATCHED_EXTS:
                    hashed = self.hashFile(newPath)
                    if newPath in self.fileHashes:
                      oldHash = self.fileHashes.get(newPath)
                      if oldHash != hashed:
                          print("File changed, uploading: %s" % newPath)
                          self.putUpdate(newPath)
                    self.fileHashes[newPath] = hashed

if __name__ == "__main__":
    swsync()
