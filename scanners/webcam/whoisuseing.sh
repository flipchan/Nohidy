echo 'Who is useing my webcam?'
#fuser /dev/video0
whatpid="$(fuser /dev/video0)"
echo 'checking the pid'
ps -aux | grep "${whatpid}"
echo 'done'
