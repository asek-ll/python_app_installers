from common import download
import os

target_dir = os.path.join(os.path.dirname(__file__), 'vim')
vim_dir = os.path.join(target_dir, 'vim/vim74')

download.save_zip('ftp://ftp.vim.org/pub/vim/pc/gvim74.zip', target_dir)
download.save_zip('ftp://ftp.vim.org/pub/vim/pc/vim74rt.zip', target_dir)

download.save_zip('http://wyw.dcweb.cn/vim/gvim74.zip', vim_dir)
download.save_to_dir('https://github.com/DeXP/xkb-switch-win/releases/download/1.0.0/libxkbswitch32.dll', vim_dir)
