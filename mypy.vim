
if v:version < 600
    syntax clear
"elseif exists('b:current_syntax')
    "finish
endif

syn keyword pythonKW		def class with from import as global
syn keyword pythonKW		if else elif while for break continue match case
syn keyword pythonKW		try except finally
syn keyword pythonKW		is not or and in

syn match pythonOP		':\|=\|:=\|==\|!=\|<\|>\|<=\|>=\|@\|->'
syn match pythonOP		'^\|&\||\|+\|+=\|-\|-=\|*\|*=\|/\|/=\|//\|//=\|%\|%='
syn match pythonOP		'(\|)\|\[\|\]\|{\|}\|,\|\.\|\W_\W'

syn region pythonCOM		start='#' end='\n'

syn keyword pythonBuiltin	None True False
syn keyword pythonBuiltin	__import__ abs all any bin callable chr classmethod compile complex delattr dir divmod enumerate eval filter format getattr globals hasattr hash help hex id input isinstance issubclass iter len locals map max memoryview min next oct open ord pow property range repr reversed round setattr slice sorted staticmethod sum super type vars zip

syn keyword pythonBuiltin    	object bool int float tuple str list dict set frozenset bytearray byte chr ord

syn keyword pythonBuiltin	ascii breakpoint exec print

syn match pythonNUM		/\<\d\+\>/
syn match pythonNUM		/\<\d\*.\d+\>/

syn region pythonSTR		start='"' end='"'
syn region pythonSTR		start='"""' end='"""'
syn region pythonSTR		start="'" end="'"
syn region pythonSTR		start="'''" end="'''"

hi pythonKW 			guifg=#118888
hi pythonOP 			guifg=#ccaa33
hi pythonCOM 			guifg=#999999
hi pythonBuiltin 		guifg=#664499
hi pythonNUM 			guifg=#3388ff
hi pythonSTR 			guifg=#dd6600

let b:current_syntax = 'python'

