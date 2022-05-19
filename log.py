from loguru import logger

# 超过1M就新生成一个文件
logger.add("size.log", rotation="1 MB")

def log(title, message):
    logStr = '\n'.join(['', title, message])
    logger.info(logStr)

log('1', '2')
