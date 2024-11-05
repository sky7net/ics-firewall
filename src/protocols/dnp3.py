def analyze(packet):
    """
    DNP3 paketini analiz eder.
    
    :param packet: DNP3 protokolüne uygun bir paket
    :return: bool - Paket geçerliyse True, değilse False
    """
    # DNP3 protokolü için function_code kontrolü
    if packet.get("function_code") == "READ":
        print("[DNP3] Read request detected.")
        return True
    elif packet.get("function_code") == "WRITE":
        print("[DNP3] Write request detected.")
        return True
    else:
        print("[DNP3] Unknown DNP3 function code.")
        return False
