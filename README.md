# jitterpic
add jitter noise to picture by using python


By using this python script, it can help you to add jitter noise to the original picture/photo/image.
We use these noise pictures as the original picture dataset's complement. To expect a better training result in CNN. 

The original pic:
![Alt text](https://github.com/lpcclown/jitterpic/blob/master/1.png?raw=true "The original pic")


The noised pic:
![Alt text](https://github.com/lpcclown/jitterpic/blob/master/2.png?raw=true "The noised pic")


Some possible issues you might get during you run this small piece of python code:
1. Install numpy on Windows server, pop error cannot find python.

Solution: You do not need to reinstall 32bits python, just run the attached reg file, to update the python path in register table.

2. cv2 cannot be install directly in pycharm.

Solution: You might follow this solution to install openCV (cv2)
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
