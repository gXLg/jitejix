import sys
import curses

try : file = open ( sys.argv [ 1 ], "r" ).read ( )
except :
  print ( "Failed opening file" )
  exit ( 1 )

file = file.replace ( "\n", " " )

def programm ( screen ) :
  curses.curs_set ( 0 )
  curses.init_pair ( 1, 0, curses.COLOR_RED )
  curses.init_pair ( 2, 0, curses.COLOR_YELLOW )
  y, x = screen.getmaxyx ( )
  ff = [ file [ i : i + x - 2 ]
      for i in range ( 0, len ( file ), x - 2 )]
  output_ = curses.newwin ( y // 4 - 1, x - 1, y // 2, 0 )
  output = curses.newwin ( y // 4 - 3, x - 3, y // 2 + 1, 1 )
  debug = curses.newwin ( y // 2 - 1, x - 1, 0, 0 )
  prog_ = curses.newwin ( y // 4 - 1, x - 1, y // 4 * 3, 0 )
  prog = curses.newwin ( y // 4 - 3, x - 3, y // 4 * 3 + 1, 1 )

  # setup
  bottle = [ i for i in range ( 256 )]
  c = 0
  st = 0
  out = ""
  yellow = [ ]
  i = 0

  def draw ( i ) :
    y, x = screen.getmaxyx ( )

    output_.clear ( )
    output_.box ( )
    screen.refresh ( )
    output_.refresh ( )

    output.addstr ( 0, 0, out + "_" )
    output.refresh ( )

    prog_.clear ( )
    prog_.box ( )
    screen.refresh ( )
    prog_.refresh ( )

    m = ( y // 4 - 3 ) * ( x - 3 ) - 1
    off = i // m
    prog.addstr ( 0, 0, file [ off * m : off * m + m ])
    j = i % m
    prog.addch ( j // ( x - 3 ),
      j % ( x - 3 ),
      file [ i ], curses.color_pair ( 1 ))
    prog.refresh ( )

    debug.clear ( )
    debug.box ( )
    try :
      for i in range ( 256 ) :
        x = ( i % 16 ) * 4
        y = ( i // 16 )
        color = ( 1 if i == c else ( 2 if i in yellow else 0 ))
        debug.addstr ( 1 + y, 1 + x,
                       str ( bottle [ i ]), curses.color_pair ( color ))
      color = ( 2 if "st" in yellow else 0 )
      debug.addstr ( 17, 1, "[" + str ( st ) + "]", curses.color_pair ( color ))
    except : debug.addstr ( 1, 1, "Could not display" )
    screen.refresh ( )
    debug.refresh ( )

  draw ( i )

  while i < len ( file ) :
    yellow.clear ( )
    char = file [ i ]
    key = screen.getch ( )
    if key == 17 : return
    if not key == 32 : continue
    if char == "+" :
      bottle [ ( c + 1 ) % 256 ] += 1
      bottle [ ( c + 1 ) % 256 ] %= 256
      yellow.append ( ( c + 1 ) % 256 )
      bottle [ ( c - 1 ) % 256 ] += 1
      bottle [ ( c - 1 ) % 256 ] %= 256
      yellow.append ( ( c - 1 ) % 256 )
    elif char == "-" :
      bottle [ ( c + 1 ) % 256 ] -= 1
      bottle [ ( c + 1 ) % 256 ] %= 256
      yellow.append ( ( c + 1 ) % 256 )
      bottle [ ( c - 1 ) % 256 ] -= 1
      bottle [ ( c - 1 ) % 256 ] %= 256
      yellow.append ( ( c - 1 ) % 256 )
    elif char == "&" :
      bottle [ ( c + 1 ) % 256 ], bottle [ ( c - 1 ) % 256 ] =\
        bottle [ ( c - 1 ) % 256 ], bottle [ ( c + 1 ) % 256 ]
      yellow.append ( ( c + 1 ) % 256 )
      yellow.append ( ( c - 1 ) % 256 )
    elif char == "/" :
      yellow.append ( "st" )
      st += bottle [ c ]
      st %= 256
    elif char == "\\" :
      yellow.append ( "st" )
      bottle [ c ] = st
    elif char == "*" :
      bottle [ c ] +=\
        bottle [ ( c + 1 ) % 256 ] * bottle [ ( c - 1 ) % 256 ]
      bottle [ c ] %= 256
      yellow.append ( ( c + 1 ) % 256 )
      yellow.append ( ( c - 1 ) % 256 )
    elif char == "%" :
      bottle [ c ] = c
    elif char == "_" :
      bottle [ c ] = 0
    elif char == "?" :
      if not bottle [ c ] :
        while not file [ i ] == ":" : i += 1
    elif char == "#" :
      if not st :
        while not file [ i ] == ":" : i += 1
    elif char == "!" :
      out += chr ( bottle [ c ])
    elif char == ">" :
      yellow.append ( c )
      c += 1
      c %= 256
    elif char == "<" :
      yellow.append ( c )
      c -= 1
      c %= 256
    elif char == "^" :
      yellow.append ( c )
      c += st
      c %= 256
    elif char == "@" :
      yellow.append ( c )
      c = bottle [ c ]
    elif char == "~" :
      yellow.append ( "st" )
      st -= 1
      st %= 256
    elif char == "$" :
      while not file [ i + 1 ] in "?#" : i -= 1

    draw ( i )
    i += 1


curses.wrapper ( programm )
curses.flushinp ( )
