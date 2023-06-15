#!/bin/sh

# Shell script using Linux commands to create a random string
# Presumably alphanumeric
# Trim and Head?

# pipe makes the output of the left the input of the right
# less than is an input redirect which sends the part to the right as the input to the program on the left?
# greater than is an output redirect which
# ; separates commands

# head -c 6
# prints the first 6 bytes

# tr -cd "[:alnum]" 
# translate command
# -c # first complement SET1
# -d # delete characters in SET1, do not translate
# "[:alnum:]" all numbers and digits

# Is the string inside the name as well as inside the file? 

# Inspiration: https://unix.stackexchange.com/questions/230673/how-to-generate-a-random-string
rand=$(base64 < /dev/urandom | head -c 6 | tr -cd "[:alnum:]"; echo '')

echo "" > "include-me-${rand}.txt"
