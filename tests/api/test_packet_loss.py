import random

def simulate_packet_send():
    return random.random() < 0.9


def test_packet_loss_rate():
    random.seed(42)   # make test reproducible

    total_packets = 1000
    success_count = 0

    for _ in range(total_packets):
        if simulate_packet_send():
            success_count += 1

    loss_rate = 1 - (success_count / total_packets)

    print(f"Packet Loss Rate: {loss_rate:.2%}")

    assert loss_rate <= 0.1