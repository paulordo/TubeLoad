# TubeLoad

## English 🇺🇸

### 📌 Description
TubeLoad is a simple and efficient YouTube video downloader built with Python and Tkinter. It allows users to download videos in different qualities and formats, including audio-only mode.

### 🚀 Features
- Download YouTube videos in various resolutions (e.g., 720p, 1080p).
- Option to download only the audio in MP3 format.
- Simple and intuitive graphical user interface (GUI).
- Works offline after installation.

### 🛠️ Requirements
- Python 3.x
- yt-dlp
- FFmpeg (for audio conversion)
- Tkinter (for GUI)
- customtkinter

### 💾 Installation
#### Running the Executable (Windows)
1. Download the `TubeLoad.exe` file.
2. Run the `.exe` file and start downloading videos!

#### Running from Source Code
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/tubeload.git
   cd tubeload
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python gui.py
   ```

### ⚡ Building the Executable
To create a portable `.exe` file, use PyInstaller:
```sh
pyinstaller --onefile --noconsole --name "TubeLoad" --icon="logo.ico" -w gui.py
```

### 📜 License
This project is open-source and available under the MIT License.

---

## Português 🇧🇷

### 📌 Descrição
TubeLoad é um downloader de vídeos do YouTube simples e eficiente, desenvolvido com Python e Tkinter. Ele permite baixar vídeos em diferentes qualidades e formatos, incluindo apenas áudio.

### 🚀 Funcionalidades
- Baixe vídeos do YouTube em diversas resoluções (ex: 720p, 1080p).
- Opção de baixar apenas o áudio em formato MP3.
- Interface gráfica (GUI) simples e intuitiva.
- Funciona offline após a instalação.

### 🛠️ Requisitos
- Python 3.x
- yt-dlp
- FFmpeg (para conversão de áudio)
- Tkinter (para GUI)
- customtkinter

### 💾 Instalação
#### Executando o Arquivo Executável (Windows)
1. Baixe o arquivo `TubeLoad.exe`.
2. Execute o `.exe` e comece a baixar vídeos!

#### Executando o Código Fonte
1. Clone este repositório:
   ```sh
   git clone https://github.com/paulordo/TubeLoad.git
   cd tubeload
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```sh
   python gui.py
   ```

### ⚡ Criando o Executável
Para criar um arquivo `.exe` portátil, use o PyInstaller:
```sh
pyinstaller --onefile --noconsole --name "TubeLoad" --icon="logo.ico" -w gui.py
```

### 📜 Licença
Este projeto é open-source e está disponível sob a licença MIT.

