if !has('python3')
  echo "Error: VimTLJ vim compiled with +python3"
  finish
endif

let s:vimtlj_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
vimtlj_root_dir = vim.eval('s:vimtlj_root_dir')
python_root_dir = normpath(join(vimtlj_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import vimtlj
EOF

function! VimTLJAddDiaryEntry()
    python3 vimtlj.create_diary_entry()
endfunction
command! -nargs=0 VimTLJAddDiaryEntry call VimTLJAddDiaryEntry()
