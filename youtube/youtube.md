# one commnad
```
# en
 yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-auto-subs --sub-lang en --embed-subs https://www.youtube.com/watch?v=Un2Nw00oL2s

 for item in `cat urls.txt`;do yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-auto-subs --sub-lang en --embed-subs -f "bestvideo[height<=720]+bestaudio/best" $item;done

 # en, fa
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-subs --sub-lang en,fa --embed-subs https://www.youtube.com/watch?v=o5coAL7oE0o

# playlist
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-auto-subs --sub-lang en --embed-subs -f "bestvideo[height<=720]+bestaudio/best" -o "%(playlist_index)s-%(title)s.%(ext)s" <playlist_url>
```

# install and commands
```
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -U yt-dlp

pip3 install pycryptodome brotli
pip3 install -U yt-dlp

yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 -F https://www.youtube.com/watch?v=o5coAL7oE0o

# select quality
yt-dlp -F <video_url>
yt-dlp -f <format_code> <video_url>
yt-dlp -f "bestvideo[height<=720]+bestaudio/best" <video_url>

# subtitle
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-subs --sub-lang en --embed-subs https://www.youtube.com/watch?v=o5coAL7oE0o

-write-subs: Downloads subtitles if available.
-sub-lang en: Specifies the subtitle language (e.g., en for English). You can replace en with other language codes.
-embed-subs: Embeds the subtitles into the video file.
-cookies-from-browser firefox: Uses cookies from your Firefox browser to handle authentication.
-proxy http://127.0.0.1:2081: Uses the specified proxy (if needed).

# To List Available Subtitles
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --list-subs https://www.youtube.com/watch?v=o5coAL7oE0o

# -write-subs --sub-lang en,fa --embed-subs
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-subs --sub-lang en,fa --embed-subs https://www.youtube.com/watch?v=o5coAL7oE0o

# -write-auto-subs --sub-lang en,fa --embed-subs
yt-dlp --cookies-from-browser firefox --proxy http://127.0.0.1:2081 --write-auto-subs --sub-lang en,fa 
--embed-subs https://www.youtube.com/watch?v=o5coAL7oE0o
```