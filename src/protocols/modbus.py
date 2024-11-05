def analyze(packet):
    """
    Modbus paketini analiz eder.
    
    :param packet: Modbus protokolüne uygun bir paket
    :return: bool - Paket geçerliyse True, değilse False
    """
    # Modbus paketi için function_code değerine göre karar veriyoruz
    if packet.get("function_code") == 0x03:  # Read Holding Registers
        print("[Modbus] Read Holding Registers request detected.")
        return True
    elif packet.get("function_code") == 0x06:  # Write Single Register
        print("[Modbus] Write Single Register request detected.")
        return True
    else:
        print("[Modbus] Unknown Modbus function code.")
        return False
