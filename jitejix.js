const fs = require ( "fs" )

var file
try { file = fs.readFileSync ( process.argv [ 2 ]).toString ( )}
catch {
  console.log ( "Failed opening file" )
  process.exit ( 1 )
}

// setup
var bottle = [ ]
for ( var i = 0; i < 256; i ++ ) bottle.push ( i )
var c = 0
var st = 0

function print ( b ) {
  process.stdout.write ( String.fromCharCode ( b ))
}

// programm handling
var i = 0
while ( i < file.length ) {
  var char = file [ i ]
  switch ( char ) {
  case "+" :
    bottle [ ( c + 1 ) % 256 ] ++
    bottle [ ( c + 1 ) % 256 ] %= 256
    bottle [ ( c - 1 ) % 256 ] ++
    bottle [ ( c - 1 ) % 256 ] %= 256
    break
  case "-" :
    bottle [ ( c + 1 ) % 256 ] --
    bottle [ ( c + 1 ) % 256 ] %= 256
    bottle [ ( c - 1 ) % 256 ] --
    bottle [ ( c - 1 ) % 256 ] %= 256
    break
  case "&" :
    var x = bottle [ ( c + 1 ) % 256 ]
    bottle [ ( c + 1 ) % 256 ] = bottle [ ( c - 1 ) % 256 ]
    bottle [ ( c - 1 ) % 256 ] = x
    break
  case "/" :
    st += bottle [ c ]
    st %= 256
    break
  case "\\" :
    bottle [ c ] = st
    break
  case "*" :
    bottle [ c ] += bottle [ ( c + 1 ) % 256 ] * bottle [ ( c - 1 ) % 256 ]
    bottle [ c ] %= 256
    break
  case "%" :
    bottle [ c ] = c
    break
  case "_" :
    bottle [ c ] = 0
    break
  case "?" :
    if ( ! bottle [ c ])
      while ( file [ i ] != ":" ) i ++
    break
  case "#" :
    if ( ! st )
      while ( file [ i ] != ":" ) i ++
    break
  case "!" :
    print ( bottle [ c ])
    break
  case ">" :
    c ++
    c %= 256
    break
  case "<" :
    c --
    c %= 256
    break
  case "^" :
    c += st
    c %= 256
    break
  case "@" :
    c = bottle [ c ]
    break
  case "~" :
    st --
    st %= 256
    break
  case "$" :
    while ( file [ i + 1 ] != "?" ) i --
    break
  }
  i ++
}
