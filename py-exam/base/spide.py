

# 如何编写一个简单的爬虫


# 使用过哪些爬虫框架 手动组装爬虫框架如何实现大规模爬取


# 对抗过哪些反爬虫机制


# 常用的网络数据爬取方法
正则表达式
Beautiful Soup
Lxml


# 遇到过得反爬虫策略以及解决方法
1.通过headers反爬虫
2.基于用户行为的发爬虫：(同一IP短时间内访问的频率)
3.动态网页反爬虫(通过ajax请求数据，或者通过JavaScript生成)
4.对部分数据进行加密处理的(数据是乱码)
解决方法：
对于基本网页的抓取可以自定义headers,添加headers的数据
使用多个代理ip进行抓取或者设置抓取的频率降低一些，
动态网页的可以使用selenium + phantomjs 进行抓取
对部分数据进行加密的，可以使用selenium进行截图，使用python自带的pytesseract库进行识别，
但是比较慢最直接的方法是找到加密的方法进行逆向推理。



# urllib 和 urllib2 的区别
urllib 和urllib2都是接受URL请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers，
urllib仅可以接受URL。urllib不可以伪装你的User-Agent字符串。
urllib提供urlencode()方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。


# 设计一个基于session登录验证的爬虫方案


# 列举网络爬虫所用到的网络数据包，解析包
网络数据包 urllib、urllib2、requests
解析包 re、xpath、beautiful soup、lxml


# 熟悉的爬虫框架


# 你用过多线程和异步嘛？除此之外你还用过什么方法来提高爬虫效率？
scrapy-redis 分布式爬取
对于定向爬取可以用正则取代xpath


# POST与 GET的区别
GET数据传输安全性低，POST传输数据安全性高，因为参数不会被保存在浏览器历史或web服务器日志中；
在做数据查询时，建议用GET方式；而在做数据添加、修改或删除时，建议用POST方式；
GET在url中传递数据，数据信息放在请求头中；而POST请求信息放在请求体中进行传递数据；
GET传输数据的数据量较小，只能在请求头中发送数据，而POST传输数据信息比较大，一般不受限制；
在执行效率来说，GET比POST好






















