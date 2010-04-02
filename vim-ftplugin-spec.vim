" Vim filetype plugin file
" Language: RPM spec file
" Author:   Elan Ruusamäe <glen@pld-linux.org>
" Copyright:    Copyright (c) 2005 PLD Linux
" Licence:  You may redistribute this under the same terms as Vim itself
"
" This sets up filetype specific options for RPM spec files.

"setlocal tw=70

map <F5> :!builder -5 %<CR>
map <F6> :!adapter %<CR>
map <F8> :!rpmbuild -bb %<CR>
map <F9> :!. /etc/shrc.d/rpm-build.sh; cvs diff -u % \| diffcol \| less -nR<CR>
map <F10> :!builder -bb -R -u %<CR>

" PLD specfiles are in UTF-8 encoding
setlocal fileencodings=utf-8
