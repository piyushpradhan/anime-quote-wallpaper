#!/bin/sh

# Fetch a quote in English 
quote_english=$(curl --silent https://animechan.vercel.app/api/random | jq ".quote" | tr '\"' ' ')

# echo "${quote_english}"

# Converting the quote in Japanese
quote_japanese=$(trans :ja "${quote_english}" | sed -n 3p)
quote_japanese=$(echo "${quote_japanese}" | sed -r "s/\x1B\[[0-9;]*[a-zA-Z]//g")

quote="${quote_japanese}\n${quote_english}"

# Creating a picture from this text
$HOME/projects/anime-quote-wallpaper/text_to_image.py "${quote_japanese}" "${quote_english}"

# Set wallpaper 
feh --bg-center $HOME/projects/anime-quote-wallpaper/result.png

