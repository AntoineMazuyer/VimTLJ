import vim
import datetime
import os

def check_if_main_dir_exists():
    if not int(vim.eval('exists("g:vimtlj_main_dir")')):
        raise Exception(""" Main directory for vim-tlj is not set yet. Please
                            define let g:vimtlj_main_dir = 'path/to/dir/' in your
                            .vimrc """ )
    main_dir = os.path.expanduser(vim.eval("g:vimtlj_main_dir"))
    if not os.path.exists(main_dir):
        raise Exception(""" Main directory does not exist """ )
    return main_dir

def create_diary_entry():
    main_dir = check_if_main_dir_exists()
    now = datetime.datetime.now()
    year_dir = os.path.join(main_dir, str(now.year))
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
    month_dir = os.path.join(year_dir, str(now.month))
    if not os.path.exists(month_dir):
        os.mkdir(month_dir)
    day_file = os.path.join(month_dir, str(now.day) + ".md")
    if not os.path.exists(day_file):
        os.mknod(day_file)
    

