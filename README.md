# opencv-kloler

If someone is spamming you on WhatsApp or hangouts, use this to reply 'k lol' to whatever they say, hence the name 'kloler'.

Simple process: It detects the top part of the chat box and detects changes to the pixels lying at the top of the chatbox, by refreshing the pixels at the top of the chatbox each time. Whenever a msg is sent, the message at the top of the chatbox moves out of the screen and hence the array of pixels changes.

![alt text] (https://raw.githubusercontent.com/pranay-venkatesh/opencv-kloler/master/s1.png)

Whenever the pixels at the top of the chat window changes, i.e., the person at the other end has sent a message, pyautogui will automatically press 'k', 'l', 'o', 'l', 'enter' in that order and send it.

Immediate frustration will ensue for the spammer and they will give up on spamming you, eventually (hopefully).

Image detection is done using OpenCV. numpy creates the required image array and pyautogui will press the required keys whenever the top pixels change.
