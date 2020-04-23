
# http协议？
1 首先 Chrome 搜索自身的 DNS 缓存。(如果 DNS 缓存中找到百度的 IP 地址，就跳过了接下来查找 
IP 地址步骤，直接访问该 IP 地址。)
2 搜索操作系统自身的 DNS 缓存。(浏览器没有找到缓存或者缓存已经失效)
3 读取硬盘中的 host 文件，里面记录着域名到 IP 地址的映射关系，Mac 电脑中位于 /etc/hosts。(如果前1.2步骤都没有找到)
4 浏览器向宽带运营商服务器或者域名服务器发起一个 DNS 解析请求，之后浏览器获得了网站的 IP 地址。
5 拿到 IP 地址后，浏览器就向该 IP 所在的服务器建立 TCP 连接(即三次握手)。
6 连接建立起来之后，浏览器就可以向服务器发起 HTTP 请求了。(这里比如访问百度首页，就向服务器发起 HTTP 中的 GET 请求)
7 服务器接受到这个请求后，根据路径参数，经过后台一些处理之后，把处理后的结果返回给浏览器，html json等。
8 浏览器拿到了百度首页的完整 HTML 页面代码，内核和 JS 引擎就会解析和渲染这个页面，里面的 JS，CSS，
图片等静态资源也通过一个个 HTTP 请求进行加载。
  浏览器根据拿到的资源对页面进行渲染，最终把完整的页面呈现给用户。
9 如果浏览器没有后续的请求，那么就会跟服务器端发起 TCP 断开(即四次挥手)。



# http、https协议有什么区别？
http协议是超文本传输协议，被用于在web浏览器和网站服务器之间传递信息，
以明文方式发送内容，不对数据加密，很容易被黑客入侵，安全性不高 为了数据传输的安全，
https在http的基础上加入了SSL协议，SSL依靠ca证书来验证服务器的身份，为浏览器和服务器之间的通信加密


# http状态码？
表示网页服务器http响应状态的3位数字代码
2开头 （请求成功）表示成功处理了请求的状态代码
3开头 （请求被重定向）表示要完成请求，需要进一步操作
4开头 （客户端错误）这些状态代码表示请求可能出错，妨碍了服务器的处理
5开头（服务器错误）这些状态代码表示服务器在尝试处理请求时发生内部错误


# 简单描述三次握手 4次挥手？

# mysql引擎有哪些

# 熟悉的数据库有什么 有什么特点






