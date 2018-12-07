"""
程序主入口Server.py：Run函数创建Socket接收客户端（浏览器）的消息（抽象为Request），并根据HTTP协议的格式解析出协议各部分内容
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''
        self.headers = {}
        self.cookies = {}
再根据解析出的path即路由返回对应的路由函数，将函数结果封装成HTTP协议的消息编码后又socket发送回给客户端（浏览器）
models:样例数据模型
routes:定义路由字典和路由函数
template：样例页面
data:样例数据存储，因为没有数据库，就是简单的把数据存到文件，后期可以把数据迁移到mogodb等数据库
static：图片等静态资源
log.gua.txt: 日志文件
utils.py: 一些工具函数， 日志，读取模板文件，跳转url, http报文的组织

"""