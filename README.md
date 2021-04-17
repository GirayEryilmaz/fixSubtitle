# fixSubtitle
Fixes Windows-1252 encoded files' Turkish character problem.

Some Turkish characters ş, Ş, ı, I, ğ, Ğ and maybe more are converted to þ, Þ, ý, Ý, ð, Ð for some reason. Probably as a "work around" while reading the file.

I could not find a way to fix this using common tools so I wrote this simple script. 

It takes input file path and the output file path. Output file is utf-8 encoded. That's it.
Enjoy!
