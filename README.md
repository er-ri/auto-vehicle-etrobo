# Autonomous Vehicle for ET Robot Contest

## Introduction
The project aims to use Machine Learning to implement an autonomous vehicle (Raspberry PI + BuildHat).

## Convolutional Neural Network
The `Convolutional Neural Network (ConvNet/CNN)` architecture typically contains three layers: a *convolutional layer*, a *pooling layer* and a *fully connected layer*.  

### Convolutional Layer
The layer performs a dot product between the `kernel` and the corresponding area of the image. When the input image has more than one channel, the kernel will also need to be extended up to the same depth. The kernel convolutely moves from the left to the right for the input image with certain step(`stride`). For some cases, we need to augment the input image to a larger size, the technique is called `padding`. In the below example, the `stride` value equals to 1 and no `padding` is applied.  

![Convolutional Layer Operation](https://github.com/vdumoulin/conv_arithmetic/blob/master/gif/no_padding_no_strides.gif?raw=true "4x4x1 image with 2x2x1 kernel, no padding")

### Pooling Layer
Same as Convolutional Layer, `Pooling Layer` acts as role of reducing the dimensionality of the input image and retaining the crucial informations. There are serveral pooling functions. The following example show the mechanism of of `Max Pooling` and `Average Pooling`.  

![Pooling Layer Operation](https://saturncloud.io/images/blog/types-of-pooling.jpg "Max Pooling and Average Pooling")

### Fully Connected Layer
A series of linear layer being used to extract specific information from the pooling layer outputs.   

## Roadmap
1. Implement a remote control vehicle (Flask + Flask-SocketIO) <- Current Status
2. Supervised learning (Tensorflow + Nvidia Model)
3. Reinforcement learning (OpenAI gym + Stable-Baselines3)

## License
Distributed under the MIT License. See `LICENSE` for more information.

---

## References
1. Running a script on the device(MicroPython)
    * https://docs.micropython.org/en/latest/reference/pyboard.py.html#running-a-command-on-the-device
2. Install OpenCV on your Raspberry Pi
    * https://raspberrypi-guide.github.io/programming/install-opencv
3. Balena Etcher
    * https://www.balena.io/
4. Getting Started with Raspberry Pi Build HAT
    * https://datasheets.raspberrypi.com/build-hat/getting-started-build-hat.pdf
5. A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way
    * https://saturncloud.io/blog/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way/
6. Convolution arithmetic
    * https://github.com/vdumoulin/conv_arithmetic
