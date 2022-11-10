#!/bin/sh

# Inspiration: https://unix.stackexchange.com/questions/230673/how-to-generate-a-random-string
rand=$(base64 < /dev/urandom | head -c 6 | tr -cd "[:alnum:]"; echo '')

echo "" > "include-me-${rand}.txt"
