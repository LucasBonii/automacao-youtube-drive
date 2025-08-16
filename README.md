# 🎬 Projeto de Download e Integração com API

## Objetivo: Automatizar o processo de download de um vídeo no youtube e uploado do mesmo no drive

## 🚀 Tecnologias utilizadas:
- **Python** → linguagem principal do projeto
- **yt-dlp** → biblioteca para download de vídeos do YouTube
- **Google Drive API (via Google Cloud)** → upload de arquivos
- **OAuth2 (Google)** → autenticação e autorização


## 🛠️ Decisões técnicas e processo de desenvolvimento:
- Para o download, optei por yt-dlp por ser estável, atualizado e simples.
- Para o upload, cogitei o uso de ferramentas de web scraping como Selenium, mas decidi usar a API oficial do Google Drive, garantindo maior confiabilidade e escalabilidade.
- Foi necessário criar um projeto no Google Cloud Console, habilitar a Google Drive API e gerar as credenciais para autenticação.

## Funções:
- baixar_video: função simples, recebe um link e através do yt-dlp faz o download do video em 360p e mp4.
- autenticar_drive: através do arquivo credenciais.json(informações privadas relacionadas a API do Google Drive), irá fazer o login no google na primeira execução, gerará o token.json, que será utilizado nas outras execuções do código, para evitar fazer login todas as vezes.
- enviar_para_drive: função utilizada para buscar o arquivo baixado anteriormente, fazer o upload no drive e alterar as permissões relacionadas ao vídeo.


## Execução e demonstração:
- Para uso cotidiano, esse código seria transformado em um executável.
- Vídeo demonstrando o uso: https://youtu.be/uGtvOtgW6Gc
