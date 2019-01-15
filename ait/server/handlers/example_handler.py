from ait.server.handler import Handler


class CcsdsPacketHandler(Handler):

    def __init__(self, name, input_type, output_type=None):
        super(CcsdsPacketHandler, self).__init__(name, input_type, output_type)

    def handle(self, input_):
        return input_ + 5


class TmTransFrameDecodeHandler(Handler):

    def __init__(self, name, input_type, output_type=None):
        super(TmTransFrameDecodeHandler, self).__init__(name, input_type, output_type)

    def handle(self, input_):
        return input_ + 5