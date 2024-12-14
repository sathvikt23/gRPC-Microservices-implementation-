import grpc 
from concurrent import futures 
import time 
import services_pb2
import services_pb2_grpc
def test_dervice_c():
    with grpc.insecure_channel("localhost:50053") as channel:
        stub=services_pb2_grpc.serviceCStub(channel)
        response=stub.verify_validation(services_pb2.validation(valid=True))
        print("Response from server C :",response.ok)
class Working(services_pb2_grpc.serviceBServicer):
    def verify_image(self, request , context ):
        print("Server A recived ip :",request.imageData)
        test_dervice_c()
        return services_pb2.ok(
            ok="Ip address recived "
        )
def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_serviceBServicer_to_server(Working(),server)

    server.add_insecure_port('[::]:50052')
    print("Server on 50052")
    server.start()
    server.wait_for_termination()
    
    

serve()