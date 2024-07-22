from dispositivos.termostato import Termostato
from dispositivos.sistema_seguranca import SistemaSeguranca
from dispositivos.luz import Luz
from functools import reduce
from padroes.observadores import Observadores


class CasaInteligente(Observadores):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CasaInteligente, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        super().__init__()
        self.dispositivos = []
        self.__initialized = True

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        self.notificar_observers(f"Dispositivo '{dispositivo.nome}' adicionado.")

    def remover_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)
            self.notificar_observers(f"Dispositivo '{dispositivo.nome}' removido.")
    
    def observar_status(self):
        status = [dispositivo.get_status() for dispositivo in self.dispositivos]
        return status

    def dispositivos_ligados(self):
        return list(filter(lambda d: d.state == 'ligada', self.dispositivos))

    def total_dispositivos_ligados(self):
        return reduce(lambda total, d: total + (1 if d.state == 'ligada' else 0), self.dispositivos, 0)



class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo, nome):
        if tipo == 'luz':
            return Luz(nome)
        elif tipo == 'termostato':
            return Termostato(nome)
        elif tipo == 'sistema_seguranca':
            return SistemaSeguranca(nome)
        else:
            raise ValueError(f"Dispositivo {tipo} desconhecido")

class Observer:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu notificação: {mensagem}")


