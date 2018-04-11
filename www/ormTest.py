import orm
from models import User
import asyncio
loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop=loop,user='root', password='123456', db='awesome')
    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()
loop.run_until_complete(test())

# import orm
# from modes import User, Blog, Comment
# import asyncio
# loop = asyncio.get_event_loop()
# async def test():
#     #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
#     await orm.create_pool(loop=loop,host='127.0.0.1', port=3306,user='root', password='123456',db='awesome')
#     #没有设置默认值的一个都不能少
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank',id="123")
#     await u.save()
# #把协程丢到事件循环中执行
# loop.run_until_complete(test())