# hand-tracking
Basic gesture control program written in python for college open evening. 

## PyAudio not working?
PyAudio is difficult to install on most machines. Using pip mostly does not work. 
To fix this, find `PyAudio-0.2.11-cp37-cp37m-win32.whl` in the root of the branch,
then go to `C:\Users\You\Appdata\Local\Programs\Python\Python3x\Scripts\` and move it to there.

Copy the complete location (should be `C:\Users\You\Appdata\Local\Programs\Python\Python3x\Scripts\PyAudio-0.2.11-cp37-cp37m-win32.whl`)

Finally, run in command prompt the following command (from anywhere in your machine or venv):
`pip install C:\Users\You\Appdata\Local\Programs\Python\Python3x\Scripts\PyAudio-0.2.11-cp37-cp37m-win32.whl`

## Hand tracking unreliable?
Look in `main.py` for instances of HandTrackingModule.handDetector and play
around with the values until you get the best parameters for your webcam and situation. 
