# Sockets

# Tarefa A: Desenvolver um servidor de data
Faça as alterações necessárias tanto no cliente quanto no servidor para que o cliente 
envie uma solicitação ao servidor e este responda com a data e o horário do sistema.
- a. Implemente utilizando sockets UDP;
- b. Utilize a biblioteca import time e o método time.ctime() para capturar a hora;
- c. Atente que será necessário converter o método time.ctime() em string por meio do método
str(): str(time.ctime())
- d. O cliente deve digitar o comando: data e aguardar o servidor responder com a data. Outros
comandos não devem ser aceitos.

# Tarefa B: Desenvolver um servidor de arquivos
Faça as alterações necessárias tanto no cliente quanto no servidor para que o cliente envie
uma solicitação ao servidor e este responda com conteúdo de um arquivo texto.
- a. Implemente utilizando sockets TCP;
- b. Crie um arquivo de texto simples (por exemplo: arquivo.txt) e escreva alguma informação
em 1 linha nesse arquivo;
- c. Faça com que o servidor leia o arquivo (local) e retorne o seu conteúdo para o cliente
quando este digitar o comando: obter arquivo.txt . Outros comandos não devem ser aceitos.
- d. Use o método open(arquivo.txt) para abrir o arquivo solicitado e o método .read() para
ler o seu conteúdo.

# Tarefa C: Desenvolver um acesso remoto
Faça as alterações necessárias tanto no cliente quanto no servidor para que o cliente envie um comando
para o servidor e este o execute localmente.
- a. Implemente utilizando sockets TCP;
- b. Utilize a biblioteca import os e o método os.system(comando)
- c. O método os.system(comando) tem como parâmetro de entrada o comando que o cliente
digitar, por exemplo: cliente digita ls ou dir e o servidor recebe e passa como parâmetro para
os.system('ls') ou os.system('dir') e exibirá o resultado na própria tela do servidor


Para executar uma das tarefas bastas executar use:
```shell script
python tarefa_<tarefa desejada>.py # deve retornar um help, caso esqueça os comanandos 
```
Exemplo:
```shell script
python tarefa_a.py
# saída do script
usage: tarefa_a.py [-h] [-server] [-client]

Desenvolver um servidor de data

optional arguments:
  -h, --help  show this help message and exit
  -server     caso queria iniciar o server utilize -server
  -client     caso queria iniciar o cliente utilzie -client
```
Use python tarefa_a.py -server para iniciar o servidor da tarefa A
```shell script
python tarefa_a.py -server
```
analogamente use -client para executar o client do servidor
```shell script
python tarefa_a.py -client
```
__OBS:__ A versão do python usada par o desenvolvimento da aplicação foi a 3.8.6,
utilizar uma versão diferente pode ou __não__ conter bugs