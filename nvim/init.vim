" https://github.com/junegunn/vim-plug 
" more plugins here: https://www.manualdocodigo.com.br/vim-basico/
" plugins are loaded from /home/akame/.local/share/nvim/plugged
call plug#begin()
Plug 'sainnhe/sonokai' "Sonokai Color theme
Plug 'folke/tokyonight.nvim' "TokyoNight Color theme
Plug 'preservim/nerdtree'
call plug#end()

"NerdTree config 
nmap <C-a> :NERDTreeToggle<CR> 
" Shortcuts for split navigation
map <C-h> <C-w>h 
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l


" Color Scheme
colorscheme tokyonight


" Global sets for nevim

syntax on            " Enable syntax highlight
set nu               " Enable line numbers
set tabstop=4        " Show existing tab with 4 spaces width
set softtabstop=4    " Show existing tab with 4 spaces width
set shiftwidth=4     " When indenting with '>', use 4 spaces width
set expandtab        " On pressing tab, insert 4 spaces
set smarttab         " insert tabs on the start of a line according to shiftwidth
set smartindent      " Automatically inserts one extra level of indentation in some cases
set hidden           " Hides the current buffer when a new file is openned
set incsearch        " Incremental search
set ignorecase       " Ingore case in search
set smartcase        " Consider case if there is a upper case character
set scrolloff=8      " Minimum number of lines to keep above and below the cursor
set colorcolumn=100  " Draws a line at the given line to keep aware of the line size
set signcolumn=yes   " Add a column on the left. Useful for linting
set cmdheight=2      " Give more space for displaying messages
set updatetime=100   " Time in miliseconds to consider the changes
set encoding=utf-8   " The encoding should be utf-8 to activate the font icons
set nobackup         " No backup files
set nowritebackup    " No backup files
set splitright       " Create the vertical splits to the right
set splitbelow       " Create the horizontal splits below
set autoread         " Update vim after file update from outside
set mouse=a          " Enable mouse support
filetype on          " Detect and set the filetype option and trigger the FileType Event
filetype plugin on   " Load the plugin file for the file type, if any
filetype indent on   " Load the indent file for the file type, if any

" Colors Config 
if exists('+termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif

"if (has("nvim")) "Transparent background. Only for nvim
"    highlight Normal guibg=NONE ctermbg=NONE
"    highlight EndOfBuffer guibg=NONE ctermbg=NONE
"endif


" Remaps 
    "Buffers
"Create Tab    
nmap te :tabe<CR>
" Nagivate between tabs
nmap ty :bn<CR>
nmap tr :bp<CR>
" delete a tab
nmap td :bd<CR>
" Create splits
nmap th :split<CR>
nmap tv :vsplit<CR>
" Close splits and others
nmap tt :q<CR>

" AutomaticCommands


