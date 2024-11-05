def analyze(packet):
    """
    HTTP paketini analiz eder.
    
    :param packet: HTTP protokolüne uygun bir paket
    :return: bool - Paket geçerliyse True, değilse False
    """
    method = packet.get("method")
    path = packet.get("path")
    
    if method in ["GET", "POST"]:
        print(f"[HTTP] {method} request detected for {path}")
        return True
    else:
        print("[HTTP] Unknown HTTP method.")
        return False
