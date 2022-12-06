# Jogo da Velha em Python

Projeto criado no intuito de avaliação de Redes de Computadores I. Esse projeto consiste em um jogo da velha simples jogado no terminal.

## Tecnologias usadas

Esse projeto utiliza apenas duas bibliotecas padrão do python:

- [os] - Limpar a tela
- [socket] - Para transferência de dados pela rede

## Como executar o projeto

Apenas tenha o python instalado:

Execute o comando a seguir no terminal:

```
python server.py
```

Em seguida execute o comando a seguir em outra instância do terminal ou em outro computador conectado na mesma rede:

```
  python client.py
```

## Como a aplicação funciona?

A aplicação funciona de forma interativa no terminal. Como tabuleiro, temos uma matriz 3x3 onde a cada jogada tem como entrada uma string no formato `(linha,coluna)`.

No lado do servidor criada uma instância do socket a partir da função `host_game()`, após isso é definido o host e porta passados por parâmetro. A partir disso servidor começa a ouvir eventos com `server.listen()`. Após isso obtém-se o socket cliente e o endereço ao chamar a função `server.accept()`. Logo em seguida são definidos os jogadores e se inicia o loop principal do game passando o socket cliente como parâmetro.

No lado do cliente cria-se também uma instancia do socket a partir da função `connect_game()` que também tem como parâmetros o host e a porta usada na criação do servidor. Após isso são definidos os jogadores e entra no loop principal.

O loop principal é o mesmo para ambas as partes. O usuário digita a entrada, por exemplo, `1,2` linha 1 coluna 2 .O programa verifica se o movimento é válido, caso seja, registra o movimento feito, muda o turno e envia a informação para o servidor codificada em utf-8
na função `client.send(move.encode('utf-8'))`. Caso seja a vez do oponente, é salvo os dados recebidos no cliente na função `client.recv()` esses dados são decodificados e então registra o movimento que foi enviado ao servidor. Caso não exista mais dados recebidos o cliente e fechado na função `client.close()`.

No lado do servidor quando o cliente é fechado e finaliza o loop principal, o servidor é fechado com a função `server.close()`.

## Por que protocolo TCP?

Diferente de jogos muito mais complexos e muito mais elaborados onde se passa uma quantidade enorme de informações a por pacote, a perda de pacotes é tolerável, porém, o jogo da velha é muito simples, onde so é passada a uma simples string de 3 caracteres. Sendo assim caso essas informação seja perdida afetara diretamente o funcionamento do programa, assim, sendo mais interessante o uso do protocolo TCP para a confiabilidade de que os dados cheguem ao seu destino.
