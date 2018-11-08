# ythosting

HOW TO SET UP:
    In order to use ythosting, you must install the following.
      - moviepy 
        instructions @ https://zulko.github.io/moviepy/install.html

      - opencv 
        I used the following pip command
            pip install opencv-python
      
HOW TO USE:
    In order to encode a video into n**2 segments with n -cuts along each side of the video
   
          process_video.py -e "input_video.mp4" -n 4
    
    This command will cut the video input_video.mp4 into 16 segments
    
    *****note may not work with n > 2****
    
    By default, this will slice the video into 4 segements
    
          process_video.py -e "input_video.mp4"
          
    This command will slice input_video.mp4 into 4 segments
