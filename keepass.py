from common import download
import os

downloads = [
'http://sourceforge.net/projects/keepass/files/KeePass%202.x/2.28/KeePass-2.28.zip/download',
#'https://bitbucket.org/HexRx/kpdatasave/downloads/KPDataSave-0.0.6_for_KeePass-2.19_and_higher.zip',
'http://sourceforge.net/projects/webautotype/files/v3.7/WebAutoType-v3.7.zip/download',
'http://downloads.sourceforge.net/keepass/KeePass-2.28-Russian.zip'
]


#target_dir = "keepass"

target_dir = os.path.join(os.path.dirname(__file__), 'keepass')

for url in downloads:
    download.save_zip(url, target_dir)

download.save_to_dir('https://dl.dropboxusercontent.com/u/21534588/keepass/keepass_triggers.xml', target_dir)
