import grpc
import services_pb2
import services_pb2_grpc

def test_service_a(packet):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services_pb2_grpc.serviceAStub(channel)
        response = stub.verify_payload(services_pb2.payloadData(payload=packet))
        print("Response from Service A:", response.ok)
def test_service_b():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = services_pb2_grpc.serviceBStub(channel)
        response = stub.verify_image(services_pb2.imageData(imageData="Test image data"))
        print("Response from Service B:", response.ok)



from scapy.all import sniff


def packet_callback(packet):
    
    if packet.haslayer('TCP'):
    
        src_port = packet['TCP'].sport
        dst_port = packet['TCP'].dport
        
        
        payload = bytes(packet['TCP'].payload)

        payload_hex = payload.hex()
        test_service_a(f"{payload_hex}")

        print(f"Source Port: {src_port}, Destination Port: {dst_port}")
        print(f"Payload (Hex): {payload_hex}")
        print("-" * 40)

print("Available Interfaces:")
print("--------------")
from scapy.all import show_interfaces
show_interfaces()

# Capture packets on a specified interface (e.g., 'Ethernet' or 'Wi-Fi')
# You can replace 'Ethernet' with the name of your interface (check with `show_interfaces()`)
sniff(iface='Wi-Fi', prn=packet_callback, store=0, count=0)

 
