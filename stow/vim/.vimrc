syntax on

"	enable mouse support
set mouse=a

"	highlight current line
set cursorline
:highlight Cursorline cterm=bold ctermbg=black

set smartindent
set tabstop=4 
set softtabstop=4

set shiftwidth=4

set number "	show line numbers
set nowrap "	if it goes beyond the screen it doesn't wrap

" Reference chart of values:
"   Ps = 0  -> blinking block.
"   Ps = 1  -> blinking block (default).
"   Ps = 2  -> steady block.
"   Ps = 3  -> blinking underline.
"   Ps = 4  -> steady underline.
"   Ps = 5  -> blinking bar (xterm).
"   Ps = 6  -> steady bar (xterm).
let &t_SI = "\e[6 q" "		SI stands for insert mode
let &t_EI = "\e[1 q"

:imap ii <Esc>
