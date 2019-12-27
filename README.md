# 图形学pj报告

<center>
  16307130193,陈天成
</center>

## pj概述

* 编程实现音乐节奏或旋律的可视化
* 编程画一个真实感静态景物
* 创作一个Flash动画

## project 1

**项目描述**

用python语言实现音乐可视化。

**项目环境**

使用语言：python3.7

IDE：pycharm

主要库：pyaudio、wave：处理音频；pygame：生成窗口，展示可视化

**提交文件**

project1.py：py文件

test1.wav：wav测试文件

**代码介绍**

首先利用wave库读入音频_test.wav_

```python
wf = wave.open("test1.wav", 'rb')
```

使用pyaudio库对音频做处理

```python
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
```

使用pygame库创建窗口，导入_zelda2.jpg_作为窗口的背景图片

```python
pygame.display.set_caption('音乐可视化')
screen = pygame.display.set_mode((840, 400), 0, 32)
bg = pygame.image.load('zelda2.jpg')
```

当音频还未停止的时候：

读入音频，播放音频，将_data_由字符串形式转换为数组。通过傅立叶变换获取实数部分。

```python
stream.write(data)
data = wf.readframes(CHUNK)
numpydata = np.fromstring(data, dtype=np.int16)
transforamed=np.real(np.fft.fft(numpydata))
```

添加背景

读取频域中的数据，并用其实数部分作为可视化矩形的高度。

窗口刷新

```
screen.blit(bg, (0, 0))
for n in range(0,transforamed.size,count):
    hight=abs(int(transforamed[n]/10000))

    pygame.draw.rect(screen,(127,255,212),Rect((20*n/count,400),(20,-hight*3)))
pygame.display.update()
```

**效果展示**

![](https://github.com/handcomechan-1997/Graphics_PJ/pics/result1.png)

## project 2

**项目描述**

使用python语言和turtle库，画一个静态景物。

**项目环境**

使用语言：python 3.7

IDE：pycharm

主要库：turtle：模仿画笔绘制图片；random：随机确定画笔的方向与树叶的颜色

**代码介绍**

首先根据节点的长度，判断此节点是树叶还是树枝，对其添加不同的颜色，如果是树枝，便添加棕色（sienna4）。此外，还根据长度判断是否要继续生成树枝或树叶。

如果节点的长度大于3，就继续生成节点。如果长度小于12，则添加树叶。并且：随机确定树叶的颜色，（green yellow与spring green）

```python
def tree(branchLen, t):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('green yellow')
            else:
                t.color('spring green')
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('green yellow')
            else:
                t.color('spring green')
            t.pensize(branchLen / 2)
        else:
            t.color('sienna4')
            t.pensize(branchLen / 10)
```

随机转动画笔，并且继续在当前节点上添加树枝/树叶。

```python
t.forward(branchLen)
a = 1.5 * random.random()
t.right(20 * a)
b = 1.5 * random.random()
tree(branchLen - 10 * b, t)
t.left(40 * a)
tree(branchLen - 10 * b, t)
t.right(20 * a)
t.up()
t.backward(branchLen)
t.down()
```

添加落叶效果，同样通过random随机确定落叶的位置

```python
def petal(m, t):  
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color("gold2")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)
```

添加背景颜色，生成树与落叶效果

```python
t = turtle.Turtle()
myWin = turtle.Screen()
t.getscreen().tracer(5, 0)
turtle.screensize(bg='turquoise1')
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')
tree(60, t)
petal(100, t)

myWin.exitonclick()
```

**参考资料**

turtle库介绍：https://blog.csdn.net/cx243698/article/details/91047123

**效果展示**

![](https://github.com/handcomechan-1997/Graphics_PJ/pics/result2.png)

## project 3

**项目描述**

使用an，完成一段flash制作

**项目环境**

使用软件：adobe animate cc2018

**提交文件**

送礼物.fla

送礼物.swf

