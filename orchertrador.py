def orquestrar_dialogo(mensagem_usuario):
    contexto = f"""
    Mensagem do usuário: "{mensagem_usuario}"
    Os agentes disponíveis são: C3PO (protocolo) e R2D2 (técnico).
    Escolha quem deve responder e envie a mensagem.
    """
    resposta = anakin.send_message(contexto)
    return resposta