from concurrent import futures
import subprocess
import time
import grpc
import flint.flint_pb2_grpc as pb2_grpc
import flint.flint_pb2 as pb2

class FlintService(pb2_grpc.FlintServicer):
  def Run(self, request, context):
    print(request.type)
    s = time.time()
    res = subprocess.run(['moja.cli', '--help'], stdout=subprocess.PIPE)
    e = time.time()
    response = {
      'exitCode' : res.returncode,
      'execTime' : e - s,
      'response' : res.stdout.decode('utf-8')
    }
    return pb2.FlintResponse(**response)

if __name__ == '__main__':
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  pb2_grpc.add_FlintServicer_to_server(FlintService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()