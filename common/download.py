import urllib.request, zipfile, os
import sys
import time
 
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    if duration > 0:
      speed = int(progress_size / (1024 * duration))
    else:
      speed = -1
    if total_size > 0:
      percent = int(count * block_size * 100 / total_size)
    else:
      percent = 100

    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    print("download %s to %s" % (url, filename))
    urllib.request.urlretrieve(url, filename, reporthook)
    print("")

def save_to_dir(url, dirname):
    filename = os.path.basename(url)
    save(url, os.path.join(dirname, filename))

def save_zip(url, filename):
  temp_file = os.path.join(os.path.dirname(__file__),'..', 'tempfile')
  save(url, temp_file);
  with zipfile.ZipFile(temp_file, "r") as z:
      z.extractall(filename)
  os.remove(temp_file)
