if status is-interactive
    # Commands to run in interactive sessions can go here
	set fish_greeting #surpresses fish's intro message
	alias ll='exa -l -g --icons'
	alias lla='exa -l -g -a --icons'
	alias llt='exa --tree'
	alias llat='exa -a --tree'
	alias v='nvim'
	alias py='python'
	alias redr='redshift -l 55.7:12.6 -t 2000:2000 &'
	alias redgtk='redshift-gtk -l 55.7:12.6 -t 2000:2000 &'

end
