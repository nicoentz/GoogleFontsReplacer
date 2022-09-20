# GoogleFontsReplacer
Some code snippets for automizing replacement of cdn hosted google fonts with local hosted copys of these fonts

Assuming you have given a css file "fonts.css" containing all @font-face {} definitions with references to woff2 font files hosted on the google CDN.

Dependencies: UNIX-like shell, installed python3 interpreter

1.) Copy the script "get_gfonts.sh" and the python source file "replace.py" to the directory where the "fonts.css" is located.

2.) Make sure the shell script is executable by issuing "chmod +x get_gfonts.sh" in a terminal

3.) Execute the shell script using "./get_gfonts.sh"

4.) The shell script will find all reference to woff2 font files hosted by google, download them into the subfolder "fonts/". The python script will be executed and replaces all references to external hosted woff2-files in the given "fonts.css" with the corresponding local copy of the file. The old "fonts.css" is automatically backupped in the file "fonts_old.css".

5.) Now your webpage using "fonts.css" will use only local hosted fonts
