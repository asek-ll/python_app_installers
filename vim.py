from common import download
import os
import shutil

target_dir = os.path.join(os.path.dirname(__file__), 'vim')
vim_dir = os.path.join(target_dir, 'vim/vim74')

download.save_zip('ftp://ftp.vim.org/pub/vim/pc/gvim74.zip', target_dir)
download.save_zip('ftp://ftp.vim.org/pub/vim/pc/vim74rt.zip', target_dir)

download.save_zip('http://wyw.dcweb.cn/vim/gvim74.zip', vim_dir)
download.save_to_dir('https://github.com/DeXP/xkb-switch-win/releases/download/1.0.0/libxkbswitch32.dll', vim_dir)

temp_lua_dir = os.path.join(target_dir, 'lua_temp')
download.save_zip('http://garr.dl.sourceforge.net/project/luabinaries/5.1.5/Tools%20Executables/lua-5.1.5_Win32_bin.zip', temp_lua_dir)

shutil.copyfile(os.path.join(temp_lua_dir, 'lua5.1.dll'), os.path.join(vim_dir, 'lua51.dll'))

shutil.rmtree(temp_lua_dir)
