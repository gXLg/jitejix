import sys

try : file = open ( sys.argv [ 1 ], "r" ).read ( )
except :
  print ( "Failed opening file" )
  exit ( 1 )

# setup
bottle = [ i for i in range ( 256 )]
c = 0
st = 0

# programm handling
i = 0
while i < len ( file ) :
  char = file [ i ]
  if char == "+" :
    bottle [ ( c + 1 ) % 256 ] += 1
    bottle [ ( c + 1 ) % 256 ] %= 256
    bottle [ ( c - 1 ) % 256 ] += 1
    bottle [ ( c - 1 ) % 256 ] %= 256
  elif char == "-" :
    bottle [ ( c + 1 ) % 256 ] -= 1
    bottle [ ( c + 1 ) % 256 ] %= 256
    bottle [ ( c - 1 ) % 256 ] -= 1
    bottle [ ( c - 1 ) % 256 ] %= 256
  elif char == "&" :
    bottle [ ( c + 1 ) % 256 ], bottle [ ( c - 1 ) % 256 ] =\
      bottle [ ( c - 1 ) % 256 ], bottle [ ( c + 1 ) % 256 ]
  elif char == "/" :
    st += bottle [ c ]
    st %= 256
  elif char == "\\" :
    bottle [ c ] = st
  elif char == "*" :
    bottle [ c ] +=\
      bottle [ ( c + 1 ) % 256 ] * bottle [ ( c - 1 ) % 256 ]
    bottle [ c ] %= 256
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
    print ( chr ( bottle [ c ]), end = "" )
  elif char == ">" :
    c += 1
    c %= 256
  elif char == "<" :
    c -= 1
    c %= 256
  elif char == "^" :
    c += st
    c %= 256
  elif char == "@" :
    c = bottle [ c ]
  elif char == "~" :
    st -= 1
    st %= 256
  elif char == "$" :
    while not file [ i + 1 ] == "?" : i -= 1
  i += 1

#print ( bottle )
