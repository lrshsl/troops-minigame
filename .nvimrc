echo "Sourced"

augroup TROOPS_MINIGAME
	au!
	au BufRead,BufEnter		*.py	so mypy.vim
augroup END

