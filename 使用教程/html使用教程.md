# HyperText Markup Language
# 1.常见标签
## 区块元素
- `<h1>`
- `<p>`
- `<ol>`(ordered list)
- `<ul>`
- `<li>`
## 行内元素
- `<strong>`
- `<em>`
- `<a>`(`<a href="#">`)
- `<br>`
- `<blockquote>`(`<blockquote cite="#">`)
# 2.插入图片
`<img src="#" alt= >`
`<img>` 标签是 **Image**（图像）的缩写。它的作用很简单：**在网页上显示一张图片**。
它有两个非常特殊的特点，和你之前见过的 `<title>` 或 `<a>` 都不一样：
1. **它是“单身”标签**：它不需要结束标签。你写 `<img ...>` 就行，不用写 `</img>`。
2. **它必须靠属性工作**：如果不写属性，它本身没有任何意义。
下面是它的核心用法，我用你的“烘培工坊”来举例。
---
### 1. 基础语法（必背）
最简单的写法如下：
```html
<img src="图片地址" alt="图片的描述">
```

这里有两个**必须**要写的属性：
#### A. `src` (Source) —— 图片在哪里？
这是核心。还记得刚才学的 `href` 吗？
- `href` (在 `<a>` 里) 是告诉浏览器 **“要去哪里”**（目标）。
- `src` (在 `<img>` 里) 是告诉浏览器 **“去哪里把东西拿过来”**（资源）。
如果你的项目文件夹里有一张叫 `cake.jpg` 的图片，你就这样写：
```html
<img src="cake.jpg">
```
#### B. `alt` (Alternative Text) —— 图片挂了怎么办？
这是很多新手容易忽略，但**极其重要**的属性。
它有两个作用：
1. **备胎**：如果图片地址错了，或者网速太慢加载不出来，网页上会显示这段文字，告诉用户原本这里是什么。
2. **盲人阅读**：视障人士使用“屏幕阅读器”上网时，读不到图片，但机器会读出 `alt` 里的字：“这是一张巧克力蛋糕的图片”。
---
### 2. 进阶用法：控制大小
通常我们会用 CSS 来控制大小，但在 HTML 里直接写也是可以的，单位默认是像素 (px)。
```html
<img src="logo.png" alt="烘培工坊Logo" width="300">

<img src="logo.png" alt="烘培工坊Logo" width="300" height="100">
```
---
### 3. 难点：路径怎么写？ (`src` 填什么)
这通常是新手最头疼的地方。假设你的 `index.html` 在桌面的“Web”文件夹里。
#### 情况一：图片在网上 (绝对路径)
直接复制图片的网址。
```html
<img src="https://example.com/images/bread.jpg" alt="网上的面包图">
```
#### 情况二：图片在你自己电脑里 (相对路径)
这取决于图片相对于 `index.html` 的位置：
- **图片和 html 在一起：**
    `src="cake.jpg"`
- **图片在下级文件夹 (比如有个 images 文件夹)：**
    `src="images/cake.jpg"` (最推荐的做法，把图片整理分类)
- **图片在上级文件夹 (不常见)：**
    `src="../cake.jpg"` (`..` 代表退回到上一层目录)
---
# 3.CSS
为了方便你记忆，我把常用的 CSS 操作分成了 **5 大类**（文字、盒子、布局、背景、交互）。你可以把这篇回答当作你的**“速查字典”**。

---
### 第一类：文字美容 (Typography)
这是最基础的，决定了网页上的字好不好看。

|**属性 (Property)**|**作用**|**常用写法 (示例)**|**备注**|
|---|---|---|---|
|**color**|字体颜色|`color: #333;` 或 `color: red;`|推荐用十六进制代码 (#...)|
|**font-size**|字体大小|`font-size: 16px;`|网页正文一般 16px-18px|
|**font-weight**|字体粗细|`font-weight: bold;`|bold(粗), normal(正常)|
|**text-align**|文字对齐|`text-align: center;`|center(居中), left(左), right(右)|
|**line-height**|行高|`line-height: 1.5;`|让多行文字不拥挤，1.5 倍很舒服|
|**font-family**|字体类型|`font-family: "微软雅黑", sans-serif;`|优先用什么字体|

---

### 第二类：盒子模型 (Box Model) —— **核心概念**

这是新手最容易晕的地方。在 CSS 眼里，**所有元素（图片、标题、段落）都是一个矩形的盒子**。

你需要控制这个盒子的三个“厚度”：

1. **Padding (内边距)**：内容到边框的距离（像**填充泡沫**，让盒子变胖）。
    
2. **Border (边框)**：盒子的壳。
    
3. **Margin (外边距)**：盒子和其他盒子之间的距离（像**社交距离**，推开别人）。
    

|**属性**|**作用**|**示例**|**顺口溜**|
|---|---|---|---|
|**padding**|内边距|`padding: 20px;`|**自己变胖**，内容不贴边|
|**margin**|外边距|`margin: 20px;`|**推开别人**，产生空隙|
|**border**|边框|`border: 1px solid black;`|粗细 + 样式 + 颜色|
|**width**|宽度|`width: 300px;`|也可以用百分比 `50%`|
|**height**|高度|`height: 200px;`|通常不写，让内容自动撑开|

> **💡 小技巧：** 想要一个东西（有宽度的）**水平居中**，最著名的写法是：`margin: 0 auto;` (上下为0，左右自动)。

---

### 第三类：布局排版 (Layout) —— 让元素排排坐

以前排版很难，现在有了神器 **Flexbox (弹性盒子)**，你只需要记住这三行代码，就能搞定 90% 的布局（比如导航栏、图片列表）。

首先，你要给这些元素的**父容器**（比如装它们的 `<div>`）加上魔法：

CSS

```
.container {
    display: flex; /* 开启弹性布局，子元素会自动横向排列 */
    justify-content: center; /* 横向居中 (justify-content) */
    align-items: center; /* 纵向居中 (align-items) */
}
```

|**属性**|**作用**|**常用值**|
|---|---|---|
|**display**|显示模式|`flex` (最常用), `block` (独占一行), `none` (隐藏)|
|**justify-content**|横向对齐|`center` (居中), `space-between` (两端对齐，导航栏常用)|
|**align-items**|纵向对齐|`center` (垂直居中)|

---

### 第四类：美化修饰 (Decoration)

让网页看起来不像 90 年代产品的关键。

|**属性**|**作用**|**示例**|
|---|---|---|
|**background-color**|背景色|`background-color: #f0f0f0;`|
|**background-image**|背景图|`background-image: url('bg.jpg');`|
|**border-radius**|**圆角**|`border-radius: 10px;` (如果是 50% 就变成圆形)|
|**box-shadow**|**阴影**|`box-shadow: 5px 5px 10px #888;` (让元素有立体感)|

---

### 第五类：交互动作 (Interaction)

这是最让新手有成就感的一个：**“鼠标悬停效果”**。

使用 `:hover` 伪类。

CSS

```
/* 当鼠标移到 img 图片上时 */
img:hover {
    transform: scale(1.1); /* 图片放大 1.1 倍 */
    cursor: pointer;       /* 鼠标变成小手形状 */
}
```

---

### 🚀 实战：给你的“烘培工坊”来个大装修

你可以把下面这段代码直接复制到你的 `<style>` 标签里，替换掉原来的，看看效果：

CSS

```
/* 1. 全局设置 */
body {
    background-color: #FFFAF0; /* 奶油色背景 */
    font-family: sans-serif;   /* 现代无衬线字体 */
    margin: 0;                 /* 去掉浏览器默认的白边 */
}

/* 2. 标题修饰 */
h1 {
    color: #8B4513;            /* 巧克力色 */
    text-align: center;        /* 居中 */
    padding: 20px;             /* 给标题周围留点空间 */
    border-bottom: 3px solid #D2691E; /* 底部加根线条 */
}

/* 3. 图片修饰 (重点看这里) */
img {
    display: block;            /* 为了能用 margin: auto */
    width: 300px;              /* 限制图片宽度 */
    margin: 30px auto;         /* 上下30px间距，左右自动居中 */
    border-radius: 15px;       /* 变成圆角矩形 */
    box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* 加一点淡淡的阴影，有立体感 */
    transition: transform 0.3s; /* 动画过渡时间 */
}

/* 4. 鼠标悬停特效 */
img:hover {
    transform: scale(1.05);    /* 鼠标放上去时，稍微放大一点点 */
    cursor: pointer;           /* 鼠标变小手 */
}

/* 5. 段落修饰 */
p {
    text-align: center;
    color: #555;
    font-size: 18px;
    line-height: 1.6;          /* 行高大一点，阅读舒服 */
}
```