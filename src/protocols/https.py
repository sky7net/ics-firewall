def analyze(packet):
    """
    HTTPS paketini analiz eder.
    
    :param packet: HTTPS protokolüne uygun bir paket
    :return: bool - Paket geçerliyse True, değilse False
    """
    # HTTPS trafiği genellikle şifreli olduğu için sadece temel bilgileri kontrol edebiliriz
    if packet.get("is_encrypted") is True:
        print("[HTTPS] Encrypted HTTPS request detected.")
        return True
    else:
        print("[HTTPS] Non-encrypted HTTPS packet, this is unusual.")
        return False
