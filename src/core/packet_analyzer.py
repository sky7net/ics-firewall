from protocols import modbus, dnp3, http, https

def analyze_packet(packet):
    """
    Paket içeriğini analiz eder ve uygun protokol işleme modülüne yönlendirir.
    
    :param packet: Protokol bilgisi içeren paket (örneğin, kaynak IP, hedef IP, protokol ve içerik)
    :return: bool - Paket geçerliyse True, değilse False
    """
    protocol = packet.get("protocol")
    
    # Protokole göre paket analiz fonksiyonuna yönlendirme
    if protocol == 'Modbus':
        return modbus.analyze(packet)
    elif protocol == 'DNP3':
        return dnp3.analyze(packet)
    elif protocol == 'HTTP':
        return http.analyze(packet)
    elif protocol == 'HTTPS':
        return https.analyze(packet)
    else:
        # Bilinmeyen protokol, geçersiz sayılır
        print("[Packet Analyzer] Unknown protocol.")
        return False
