# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
2. Show a video of how you embed one of these algorithms into your observant system.
3. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

**See Part B/C/D.**


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

First, I tried the OpenCV examples.

<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/contour_out.jpg" width=300> <img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/flow.png" width=300>    <img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/detected_out.jpg" width=300>

Additionally, I edited the code for face detection and made it a face counter. It counts the number of human face in front of the Pi camera and shows the number of faces on Pi display.

Then, I experimented with Teachable Machines using happy and sad face examples in an attempt to create a facial expression classifier.

<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/1.png" height=500>  <img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/2.png" height=500>  <img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/3.png" height=500>

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:

<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/sad.png" width=600>
<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/happy.png" width=600>

For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

> To start off, I used the happy/sad face training model to classify the emotion. However, it worked fine on webcam, but it didn't really do what it supposed to do on the Pi camera - it failed to identify different emotions most of the time. For example, the result was always only sad or happy, even though I have changed my facial expression. 
> 
> I think one of the reasons why it failed is that facial expressions are relatively subtle and still, so the model might not be accurate due to a limited training data. And the Pi camera captured a different lighting and resolution from the webcam on my laptop, which lead to the inconsistency.
> 
> Based on the behavior I've seen, scenarios where the user is not me, the lighting/background/facial structure/hairstyle/etc. are different could cause problems.

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

> I don't think users are aware of the uncertainties in the system because it's a fairly simple interaction. Miss classification would be pretty bad because the decvice can't even complete the one and only thing it's supposed to do, which makes it useless.
> 
> To address the issue, I modified my model, instead of building an emotion classifer, I switched to an energy detetor that detects if I'm tired or not. My initial idea was to train the model using more straightforward data with more movement and contrast. 

<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/energetic.png" width=600>
<img src="https://github.com/renzhihu98/Interactive-Lab-Hub/blob/Spring2021/Lab%205/tired.png" width=600>

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
> Energy detector can be used for teaching quality improvement. It can detect if a student is tired and not paying attention to the zoom lecture/recording. If a lot of students get tired during the lecture or recording, the instructor could choose to take a break or switch topics, and the recording video could pause or provide the students with interesting materials to wake them up.
* What is a good environment for X?
> Well lit, stable environment.
* What is a bad environment for X?
> Dim, shaky environment.
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**Include a short video demonstrating the answers to these questions.**

[Video](https://youtu.be/SP18nrz0hgg)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**

