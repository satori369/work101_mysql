class AtkError(Exception):
    def __init__(self, message, code, id):
        # 错误讯息
        self.message = message
        # 错误代码
        self.code = code
        # 错误编号
        self.id = id