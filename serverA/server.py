import grpc 
from concurrent import futures 
import time 
import services_pb2
import services_pb2_grpc
class ServerA(services_pb2_grpc.serviceAServicer):
    def verify_payload(self, request , context ):
        test_service_b()
        print("Server A recived ip :",request.payload)
        return services_pb2.ok(ok="Ip address recived ")
    
def test_service_b():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = services_pb2_grpc.serviceBStub(channel)
        response = stub.verify_image(services_pb2.imageData(imageData="Test image data"))
        print("Response from Service B:", response.ok)
def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_serviceAServicer_to_server(ServerA(),server)

    server.add_insecure_port('[::]:50051')
    print("Server on 50051")
    server.start()
    server.wait_for_termination()
    
    

if __name__ == "__main__":
   serve()
   
"""
import grpc
from concurrent import futures
import services_pb2
import services_pb2_grpc

class ServiceA(services_pb2_grpc.serviceAServicer):
    def verify_payload(self, request, context):
        print("Server A received payload:", request.payload)
        return services_pb2.ok(ok="Payload received successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_serviceAServicer_to_server(ServiceA(), server)
    server.add_insecure_port('[::]:50051')
    print("Server A running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
"""