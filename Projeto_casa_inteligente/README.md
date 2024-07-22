Sistema de Casa Inteligente

Visão Geral
A Casa Inteligente é um projeto de automação residencial desenvolvido em Python. Ele oferece uma estrutura para gerenciar dispositivos como luzes, sistemas de segurança e termostatos. Cada dispositivo é modelado como uma classe com estados e transições específicas. Esse projeto é feito para a disciplina de POO da pós granduação em IA e Robótica CIn - Softex da Universidade Federal de Pernambuco.

Configuração e Execução:

Pré-requisitos:
Certifique-se de ter o Python instalado (a versão mais superior, se possível).
Instale a biblioteca transitions usando o seguinte comando:

pip install transitions

Componentes e Padrões de Design utilizados:

1- Classes de Dispositivo

Luz:

A classe Luz representa uma luz com dois estados: ligada e desligada. Ela possui os seguintes métodos:

ligar(): Liga a luz.
desligar(): Desliga a luz.
get_status(): Retorna o estado atual da luz.

Sistema de Segurança:

A classe SistemaSeguranca modela um sistema de segurança com três estados: desarmado, armado com pessoas em casa e armado sem ninguém em casa.
Métodos disponíveis:

armar_com_gente_em_casa(): Ativa o sistema com pessoas em casa.
armar_sem_gente_em_casa(): Ativa o sistema sem ninguém em casa.
desarmar(): Desativa o sistema.
get_status(): Retorna o estado atual do sistema de segurança.

Termostato:

A classe Termostato controla o aquecimento e resfriamento. Estados: desligado, aquecendo e esfriando. Métodos:

aquecer(): Inicia o aquecimento.
esfriar(): Inicia o resfriamento.
desligar(): Desliga o termostato.
get_status(): Retorna o estado atual do termostato.

2- Padroes de projeto

Singleton: Aplicado na classe CasaInteligente para garantir que exista apenas uma instância do sistema.
Factory: Aplicado na classe DispositivoFactory para criar instâncias de diferentes tipos de dispositivos.
Observer: Aplicado nas classes Observer e Subject para notificar mudanças nos estados dos dispositivos.

3- Técnicas abordadas de programação Funcional

Compreensões de Listas: Usadas para obter o status de todos os dispositivos no sistema.
Map: Aplicado para controlar dispositivos em uma lista.
Filter: Usado para filtrar dispositivos com base no estado atual.
Reduce: Utilizado para calcular o número de dispositivos em alguma ação específica (ex: luzes ligadas)

Exemplo de uso da CLI

A CLI foi desenvolvida com um menu muito simples e fácil para que o usuário não se confunda, assim ele pode, facilmente, transitar entre adicionar dispositivos, removê-los, mudar o estado deles e etc.

Passos:

1. Adicionar dispositivo: Adiciona um dispositivo (você coloca o nome)
2. Escolha de dispositivos: Luz, Termostato e Sistema de seguranca
3. Digitar um nome para o dispositivo, exemplo: Luz sala
4. O sistema irá adicionar o novo dispositivo com o nome escrito.
5. Remover o dispositivo: Caso queira remover algum dispositivo, basta selecionar a opção 2: "Remover dispositivo" e colocar o nome que você botou nele. Caso não se lembre, irá aparecer logo acima do menu ou se você selecionar a opção "Meus dispositivos".
6. Controlar dispositivo: Caso queira controlar a luz (ligar e desligar), o termostato (ligar, desligar, aquecer, esfriar) ou o sistema de segurança (armar com gente em casa, armar sem ninguém em casa ou desarmar), basta selecionar a opção 3 "Controlar dispositivo" com o devido nome dele e depois selecionar a opção que você quer.
   7- Por fim, temos a opção de sair que finaliza a execução do programa.


Vídeo explicando e rodando o código:

https://drive.google.com/file/d/1lvRihRcQ2-SVyWU_yhrX7on7blBvDXoq/view?usp=sharing
