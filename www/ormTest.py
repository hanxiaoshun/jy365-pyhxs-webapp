import orm
# from models import User
from pmModels import HisAddress
import asyncio
loop = asyncio.get_event_loop()
async def test():
    # await orm.create_pool(loop=loop,user='root', password='123456', db='awesome')
    await orm.create_pool(loop=loop, user='root', password='123456', db='personmanage')
    address = HisAddress()
    address.addresstype = '2'
    address.address = '大兴区旧宫镇旧忠路'
    await address.save()
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