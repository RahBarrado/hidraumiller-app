# Como colocar o app HidrauMiller pra gerar o .apk sozinho

Este guia é pra quando você estiver pronta pra esse passo — não tem pressa.

## 1. Criar a conta no GitHub (grátis, uns 2 minutos)

1. Acesse **github.com** e clique em "Sign up".
2. Escolha um nome de usuário, seu e-mail e uma senha.
3. Confirme o e-mail que o GitHub manda pra você.

## 2. Instalar o GitHub Desktop (só clicar, sem linha de comando)

1. Acesse **desktop.github.com** e baixe o programa (tem versão Windows e Mac).
2. Instale e abra. Faça login com a conta que você criou no passo 1.

## 3. Publicar o projeto

Quando eu terminar de preparar o projeto, eu te mando uma pasta (arquivo .zip) com tudo dentro. Você:

1. Descompacta o .zip em algum lugar do computador.
2. No GitHub Desktop, vá em **File > Add Local Repository** e escolha essa pasta.
3. Ele vai perguntar se quer "criar um repositório" ali — clique em **create a repository**.
4. Clique em **Publish repository**. Deixe **desmarcada** a opção "Keep this code private" (precisa ser público pra build automática funcionar de graça) — não tem problema, é só o código do app, sem nenhum dado de cliente ali dentro.
5. Pronto — o projeto está no GitHub.

## 4. Baixar o .apk pronto

1. No site do GitHub, abra o repositório que você acabou de publicar.
2. Clique na aba **Releases** (fica na barra lateral direita da página do repositório).
3. Vai ter um arquivo `HidrauMiller_....apk` — clique nele pra baixar.
4. Toda vez que eu atualizar o app, é só voltar nessa mesma aba: o arquivo mais novo estará lá (leva uns 3-5 minutos depois de eu avisar que atualizei, que é o tempo do GitHub compilar sozinho).

## 5. Instalar no celular Android

1. Transfira o arquivo `.apk` baixado para o celular (por cabo, WhatsApp Web, e-mail, Google Drive — qualquer jeito).
2. Abra o arquivo no celular. O Android vai avisar que "instalar de fontes desconhecidas" está bloqueado — isso é normal pra qualquer app fora da Play Store. Toque em **Configurações**, ative a permissão pra esse instalador, e volte pra instalar.
3. Pronto — o ícone do HidrauMiller aparece na tela como qualquer outro app.

Qualquer dúvida nesse processo, é só me chamar que eu vou te guiando pelos cliques.
