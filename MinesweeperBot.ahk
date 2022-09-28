#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^1:: ; Easy Minesweeper
loop 100{
     x=747
     y=435
     click,87,54,1
     sleep,2000
     click,524,587,1
     sleep,2000
     click,745,368,0
     sleep,500
     click,745,368,1
     sleep,1000
     click,757,400,1
     sleep,1000
     click,747,435,1
     sleep,1000

     PixelGetColor, color, %x%,%y%
     FileAppend, %color%- , %A_ScriptDir%\Easydata.txt
     loop 7{
          loop 9{
               x+=45
               PixelGetColor, color, %x%, %y%
               FileAppend, %color%- , %A_ScriptDir%\Easydata.txt
	       sleep,50
           }
          x-=405
          y+=45
          PixelGetColor, color,%x%,%y%
          FileAppend, %color%- , %A_ScriptDir%\Easydata.txt
          sleep,50
     }
     loop 9{
          x+=45
          PixelGetColor, color, %x%, %y%
          FileAppend, %color%- ,%A_ScriptDir%\Easydata.txt
          sleep,50
     }
     loop 2{
          FileAppend, `n ,%A_ScriptDir%\Easydata.txt
     }
     sleep,1000
}
return


^2::  ; medium minesweeper
loop 500{
     x=702
     y=405
     click,87,54,1
     sleep,2000
     click,524,587,1
     sleep,1000
     click,702,405,1
     sleep,1000

     PixelGetColor, color, %x%,%y%
     FileAppend, %color%- , %A_ScriptDir%\Meddata.txt
     loop 13{
          loop 17{
               x+=30
               PixelGetColor, color, %x%, %y%
               FileAppend, %color%- , \Meddata.txt
	       sleep,50
           }
          x-=510
          y+=30
          PixelGetColor, color,%x%,%y%
          FileAppend, %color%- , %A_ScriptDir%\Meddata.txt
          sleep,50
     }
     loop 17{
          x+=30
          PixelGetColor, color, %x%, %y%
          FileAppend, %color%- , %A_ScriptDir%\Meddata.txt
          sleep,50
     }
     loop 2{
          FileAppend, `n , %A_ScriptDir%\Meddata.txt
     }
     sleep,1000
}
return


^3::  ; hard minesweeper
loop 100{
     x=666
     y=363
     click,87,54,1
     sleep,2000
     click,524,587,1
     sleep,2000
     click,745,368,0
     sleep,500
     click,745,368,1
     sleep,1000
     click,738,445,1
     sleep,1000
     click,666,363,1
     sleep,1000

     PixelGetColor, color, %x%,%y%
     FileAppend, %color%- , %A_ScriptDir%\Harddata.txt
     loop 19{
          loop 23{
               x+=25
               PixelGetColor, color, %x%, %y%
               FileAppend, %color%- , %A_ScriptDir%\Harddata.txt
	       sleep,50
           }
          x-=575
          y+=25
          PixelGetColor, color,%x%,%y%
          FileAppend, %color%- , %A_ScriptDir%\Harddata.txt
          sleep,50
     }
     loop 23{
          x+=25
          PixelGetColor, color, %x%, %y%
          FileAppend, %color%- , %A_ScriptDir%\Harddata.txt
          sleep,50
     }
     loop 2{
          FileAppend, `n , %A_ScriptDir%\Harddata.txt
     }
     sleep,1000
}
return





^0:: ; coins
loop 7{
click,96,59,1
sleep,5000
click,515,330,0
PixelGetColor, color, 515, 330
FileAppend, %color%- ,C:\Users\Zack's PC\Desktop\Stats\Coins\CoinData.txt
sleep,100
}


