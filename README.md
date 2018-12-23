# generative-art-python
My experiments with generative art in Python.

This is my first attempt in using generative art to improve my Python skills and also to have some fun.

## Testing animated-circles example
In animated circles I use *pycairo* to generate frames and than *mencoder* to generate the video itself.

I got the idea of generating the video from [this tutorial from pritschet](https://www.pritschet.me/wiki/python/example-scripts-python/animations-cairo-and-numpy/). 

Since I'm using MACOS, I installed [mplayer](http://www.mplayerhq.hu) with [homebrew](https://brew.sh/) and than used mencoder to create videos based on the generated frames.

```
brew install mplayer
```