# automation

### Requirement : 
During my e-learning from nptel I realized that downloading vidoes and pdf is a great pain. We have to right click on each and every video and select download. If too many video are already in process, we have to wait till these video completes.

### Download video from nptel website
## Steps to follow
1. Login to your nptel account with your credentials.
2. Go to the page where the link of video is provided 
    https://nptel.ac.in/courses/nptel_download.php?subjectid=106106179
3. Right click on the page and click on "View source code".
4. Save the page with any name with html extension.
5. Run the script with the parameters mentioned in the help


## Steps to run the script
1. python download.py -f <fileName> -t <"mp3">
2. For help python download.py -h
3. download.py has below options
    a. -f "Name of the file downloded fron 'view source code'"
    b. -s "Skip no of video if few are already downloded. But limitation is, count start sequential from the html page."
    c. -t "file type supported by nptel are ''['pdf','mp4','flv','3gp','mp3']"
    d. -l "output of the result is in csv file."
