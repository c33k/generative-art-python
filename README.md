# generative-art-python
My experiments with generative art in Python.

This is my first attempt in using generative art to improve my Python skills and also to have some fun.

# Examples

Bellow there are some example outputs you can get on each program.

## CIRCLES

### circles.py

![circles.py example](/circles/outputs/circles.svg)

### dots.py

Inspired by [aaronpene](https://github.com/aaronpenne/generative_art). 

Each time you run dots.py, it chooses one background color between green and red. 
Then it draw dots and it's shadows with some randomness to create a feeling of displacement.

Running dots.py without arguments creates an image of width and height of 1600px, 10 dots per line/column and each dot having a radius of 30. 

![dots.py default example](/circles/outputs/dots_red.png)

Bellow is an example running the program with the following parameters:

```
python dots.py 1600 1600 20 15
```

![](/circles/outputs/dots_greenbig.png)

## Testing animated-circles example
In animated circles I use *pycairo* to generate frames and than *mencoder* to encode the video itself.

I got the idea of generating the video from [this tutorial from pritschet](https://www.pritschet.me/wiki/python/example-scripts-python/animations-cairo-and-numpy/). 

Since I'm using MACOS, I installed [mplayer](http://www.mplayerhq.hu) with [homebrew](https://brew.sh/) and than used mencoder to create videos based on the generated frames.

```
brew install mplayer
```