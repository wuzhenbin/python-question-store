


# 压力控制
利用协程来控制并发数
爬行频率要进行控制，不要短时间访问大量请求。
每次访问间隔时间要尽量随机，更像是人的行为。
一般情况下，IP、UA、Referrer是记录在日志里的~so 要做到人不知鬼不觉，起码做到以下三点

1 随机换代理
2 随机换UserAgent
3 最好带上Referrer

# 爬虫基本流程？
发起请求，
服务器响应内容，
对响应内容进行解析内容
保存数据或存库


# 有哪些反爬手段？
通过headers中的 User-Agent
# 使用User-Agent池来解决,我们可以考虑收集一堆User-Agent的方式，或者是随机生成User-Agent
通过headers中的 referer字段或者是其他字段
# 手动添加上就可以
通过cookie来反爬
# 如果目标网站不需要登录 每次请求带上前一次返回的cookie，比如requests模块的session
# 如果目标网站需要登录 准备多个账号，通过一个程序获取账号对应的cookie，组成cookie池，其他程序使用这些cookie
通过js对请求参数进行加密加签
# 对应的需要分析js，观察加密的实现过程
# 可以使用selenium模块解决
通过验证码来反爬
# 通过打码平台或者是机器学习的方法识别验证码，其中打码平台廉价易用，建议使用
通过ip地址来反爬
# 同一个ip大量请求了对方服务器，有更大的可能性会被识别为爬虫，
# 对应的通过购买高质量的ip的方式能够解决
通过自定义字体来反爬
# 可以尝试切换到手机版试试
通过css来反爬如通过css掩盖真实数据
# 计算css的偏量


# 如何提高爬取效率？
采用协程异步和多线程
采用消息队列模式


# post、get有什么区别？ 
GET一般用于获取/查询资源信息，而POST一般用于更新资源信息get是在url中传递数据，
数据放在请求头中，post是在请求体中传递数据get安全性非常低，
post安全性较高，但是get执行效率却比Post方法好



# xpath、css选择器及返回类型区分？
response.selector.xpath(css)    
为了方便，其中的selector可以省略返回：由selector组成的list，每个元素都是一个selector对象
1、SelectorList类型
case = response.xpath('//*[@class="content"]/ul/li')
2、List类型
case = response.xpath('//*[@class="content"]/ul/li').extract()
3、str类型
case = ''.join(response.xpath('//*[@class="content"]/ul/li').extract())
# extract()[0]选取第一个元素， extract_first()能达到一样的效果


# 模拟登陆原理？
因为http请求是无状态的，网站为了识别用户身份，需要通过cookie记录用户信息（用户、密码），
这些信息都会在手动登陆时记录在post请求的form-data里，那么在爬虫时候只需要将这些信息添加到请求头里即可。


# 验证码？
可以通过ocr对大量的图片进行训练来提高识别准确度


# 分布式原理？
单机的话是一个爬取队列一个调度器 分布式就是把爬取队列共享 然后分发给多个调度器进行爬取 这样就可以保证每台机器爬取的任务
不会重复 实现这个架构需要去重 防止中断 实现这样一个架构的框架就是scrapy-redis


# 用的什么框架，为什么选择这个框架？ 
1 scrapy，用少量代码，就能够快速的抓取到数据内容。
2 Scrapy 使用了 Twisted异步网络框架来处理网络通讯，
不用自己去实现异步框架，并且包含各种中间件接口，可以灵活的完成各种需求。

# scrapy的基本结构？
引擎(Scrapy)
调度器(Scheduler)
Item
下载器(Downloader)
爬虫(Spiders)
项目管道(Pipeline)
下载器中间件(Downloader Middlewares)


# scrapy框架执行爬虫的流程？
1 引擎从调度器中取出一个链接(URL)把URL封装成一个请求(Request)传给下载器
2 下载器把资源下载下来，并封装成应答包(Response) 
3 爬虫解析Response解析出实体（Item）, 则交给实体管道进行进一步的处理
解析出的是链接（URL）,则把URL交给调度器等待抓取


爬虫协议？Robots协议（也称为爬虫协议、爬虫规则、机器人协议等）
也就是robots.txt，网站通过robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。
Robots协议是网站国际互联网界通行的道德规范，其目的是保护网站数据和敏感信息、确保用户个人信息和隐私不被侵犯。
因其不是命令，故需要搜索引擎自觉遵守。
















