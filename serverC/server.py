import grpc 
from concurrent import futures 
import time 
import services_pb2
import services_pb2_grpc

class ServiceC_implementation(services_pb2_grpc.serviceCServicer):
    def verify_validation(self, request, context):
        print(f"Protocal to be exectued bcz{request.valid} from server b")
        return services_pb2.ok(ok="SMB protocal executed ")
    
def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_serviceCServicer_to_server(ServiceC_implementation(),server)
    server.add_insecure_port("[::]:50053")
    print("Server on 50053")
    server.start()
    server.wait_for_termination()

serve()