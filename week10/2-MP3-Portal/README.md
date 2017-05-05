# MP3 Portal

Your task is to implement a simple django webpage that converts a youtube video to a MP3 file and sends it your email.

In order to achieve that make 3 celery tasks:

- Download the video from youtube. 
- Convert the video to a MP3 file.
- Send a link to the file via email.

Useful tips:
- Use pytube to download a youtube video - <https://github.com/nficano/pytube>
- Use ffmpeg to convert mp4 to mp3 - <https://askubuntu.com/questions/84584/converting-mp4-to-mp3>
- Use any free transactional email service like sendgrid.
- Here is an example project that is live on the internet - <https://www.youtubeadl.com/>
- youtubeadl is an opensource project based on django and celery. You can see the implementation here - <https://github.com/jcalazan/youtube-audio-dl>
