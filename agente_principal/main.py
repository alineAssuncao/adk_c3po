from google.adk.agent import Agent

class C3POAgent(Agent):
    def on_message(self, message, history):
        # Resposta simpática com toque de C3PO
        return f"Olá! Sou C3PO, e recebi sua mensagem com grande honra: '{message}'. Precisa de ajuda com tradução, protocolo, ou tecnologia?"

    def on_start(self):
        return "Sistema diplomático inicializado. C3PO pronto para servir!"