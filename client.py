import grpc
import flint.flint_pb2_grpc as pb2_grpc
import flint.flint_pb2 as pb2

class FlintClient(object):
  def __init__(self):
    self.channel = grpc.insecure_channel('localhost:50051')
    self.stub = pb2_grpc.FlintStub(self.channel)

  def execFlint(self, type):
    request = pb2.FlintRequest(type=type)
    return self.stub.Run(request)

if __name__ == '__main__':
  client = FlintClient()
  response = client.execFlint('Hello!')
  print(response)