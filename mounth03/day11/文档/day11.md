[TOC]

# 项目中的方法

## 1. jQuery hover() 方法

  hover() 方法规定当鼠标指针悬停在被选元素上时要运行的两个函数。
  方法触发 mouseenter 和 mouseleave 事件。

```javascript
$(selector).hover(handlerIn, handlerOut)
```

## 2. jQuery stop() 方法
  stop() 方法为被选元素停止当前正在运行的动画。

```javascript
$(selector).stop(stopAll,goToEnd)
```

  stopAll	可选。布尔值，规定是否停止被选元素的所有加入队列的动画。默认是 false。
  goToEnd	可选。布尔值，规定是否立即完成当前的动画。默认是 false。

## 3. 动画加载页面效果
  1. html页面引入文件 scrollReveal.js

  2. 在需要加载动画效果的 div 或者其他标签中添加 data-scroll-reveal 属性
     
  3. <div data-scroll-reveal="enter left and move 50px over 1.33s">
          内容动画效果
     </div> 
     
  4. 然后在js区域加入以下代码：
     
```javascript
window.scrollReveal = new scrollReveal({reset: true});
```

  5. data-scroll-reveal 属性

      - enter

        说明: 动画起始方向
        值: top | right | bottom | left

      - move

        说明: 动画执行距离
        值: 数字，以 px 为单位

      -  over

        说明: 动画持续时间
        值: 数字，以秒为单位

      -  after/wait

        说明: 动画延迟时间

        值: 数字，以秒为单位

## 4. 编辑器使用

1. ##### 引入wangEditor插件

   ```javascript
   <script src="js/wangEditor.js"></script>
   ```

2. ##### 实例化插件

   ```javascript
   var E = window.wangEditor
   var editor = new E('#editor')
   editor.create();
   ```

3. ##### 获取富文本插件框的值

   ```javascript
   editor.txt.text()/editor.txt.html()
   ```

## 5. 本地存储对象

1. Web 存储 API 提供了 sessionStorage （会话存储） 和 localStorage（本地存储）两个存储对象来对网页的数据进行添加、删除、修改、查询操作。

2. localStorage 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。

3. sessionStorage 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。

4. 对象属性

   | 属性   | 说明                         |
   | ------ | ---------------------------- |
   | length | 返回存储对象中包含多少条数据 |

5. 对象方法

   | 方法                        | 说明                                             |
   | --------------------------- | ------------------------------------------------ |
   | key(*n*)                    | 返回存储对象中第 *n* 个键的名称                  |
   | getItem(*keyname*)          | 返回指定键的值                                   |
   | setItem(*keyname*, *value*) | 添加键和值，如果对应的值存在，则更新该键对应的值 |
   | removeItem(*keyname*)       | 移除键                                           |
   | clear()                     | 清除存储对象中所有的键                           |


## 6. 字符与对象的转换

1. ##### JSON.stringify 方法

   方法用于将 JavaScript 值转换为 JSON 字符串。

   ```javascript
   JSON.stringify(value)
   ```

   参数 value 为必需， 要转换的 JavaScript 值（通常为对象或数组）

2. ##### JSON.parse 方法

   方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象

   ```javascript
   JSON.parse(text)
   ```

   参数 text 为必要参数，表示要被解析成J 和 mouseleave 事件。

```javascript
$(selector).hover(handlerIn, handlerOut)
```

## 2. jQuery stop() 方法
  stop() 方法为被选元素停止当前正在运行的动画。

```javascript
$(selector).stop(stopAll,goToEnd)
```

  stopAll	可选。布尔值，规定是否停止被选元素的所有加入队列的动画。默认是 false。
  goToEnd	可选。布尔值，规定是否立即完成当前的动画。默认是 false。

## 3. 动画加载页面效果
  1. html页面引入文件 scrollReveal.js

  2. 在需要加载动画效果的 div 或者其他标签中添加 data-scroll-reveal 属性
     
  3. <div data-scroll-reveal="enter left and move 50px over 1.33s">
          内容动画效果
     </div> 
     
  4. 然后在js区域加入以下代码：
     
```javascript
window.scrollReveal = new scrollReveal({reset: true});
```

  5. data-scroll-reveal 属性

      - enter

        说明: 动画起始方向
        值: top | right | bottom | left

      - move

        说明: 动画执行距离
        值: 数字，以 px 为单位

      -  over

        说明: 动画持续时间
        值: 数字，以秒为单位

      -  after/wait

        说明: 动画延迟时间

        值: 数字，以秒为单位

## 4. 编辑器使用

1. ##### 引入wangEditor插件

   ```javascript
   <script src="js/wangEditor.js"></script>
   ```

2. ##### 实例化插件

   ```javascript
   var E = window.wangEditor
   var editor = new E('#editor')
   editor.create();
   ```

3. ##### 获取富文本插件框的值

   ```javascript
   editor.txt.text()/editor.txt.html()
   ```

## 5. 本地存储对象

1. Web 存储 API 提供了 sessionStorage （会话存储） 和 localStorage（本地存储）两个存储对象来对网页的数据进行添加、删除、修改、查询操作。

2. localStorage 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。

3. sessionStorage 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。

4. 对象属性

   | 属性   | 说明                         |
   | ------ | ---------------------------- |
   | length | 返回存储对象中包含多少条数据 |

5. 对象方法

   | 方法                        | 说明                                             |
   | --------------------------- | ------------------------------------------------ |
   | key(*n*)                    | 返回存储对象中第 *n* 个键的名称                  |
   | getItem(*keyname*)          | 返回指定键的值                                   |
   | setItem(*keyname*, *value*) | 添加键和值，如果对应的值存在，则更新该键对应的值 |
   | removeItem(*keyname*)       | 移除键                                           |
   | clear()                     | 清除存储对象中所有的键                           |


## 6. 字符与对象的转换

1. ##### JSON.stringify 方法

   方法用于将 JavaScript 值转换为 JSON 字符串。

   ```javascript
   JSON.stringify(value)
   ```

   参数 value 为必需， 要转换的 JavaScript 值（通常为对象或数组）

2. ##### JSON.parse 方法

   方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象

   ```javascript
   JSON.parse(text)
   ```

   参数 text 为必要参数，表示要被解析成JavaScript值的字符串