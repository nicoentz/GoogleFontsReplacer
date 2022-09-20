import re

# Using readlines()
file1 = open('fonts.css', 'r')
Lines = file1.readlines()
pattern = "src: url\((.*?)\)"

# output file
file2 = open('fonts_repl.css', 'w')
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    message = line.strip()
    new_message_line = message
    if message.startswith('src:'):
        newmessage = re.search(pattern, message).group(1)
        message_array = newmessage.split("/");
        print(message)
        #print(newmessage)
        new_message_line = "src: url(/assets/css/fonts/"+message_array[-1]+") format('woff2');"
        print(new_message_line)
    file2.write(new_message_line+"\n")
