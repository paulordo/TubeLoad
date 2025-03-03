import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
from downloader import download_video  # Importa a função de download do módulo separado


class TubeLoadApp(ctk.CTk):
    """Classe principal da aplicação TubeLoad"""

    def __init__(self):
        """Inicializa a interface gráfica"""
        super().__init__()

        # Configurações da janela principal
        self.title("TubeLoad - YouTube Downloader")
        self.geometry("500x450")
        self.resizable(False, False)

        # Variáveis para armazenar as informações fornecidas pelo usuário
        self.url_var = ctk.StringVar()  # Armazena a URL do vídeo
        self.folder_var = ctk.StringVar()  # Caminho da pasta de destino
        self.quality_var = ctk.StringVar(value="720p")  # Qualidade padrão do vídeo
        self.file_format_var = ctk.StringVar(value="Vídeo")  # Formato padrão

        # Cria os elementos da interface gráfica
        self.create_widgets()

    def create_widgets(self):
        """Cria os componentes da interface gráfica"""

        # Campo para inserir a URL do vídeo
        ctk.CTkLabel(self, text="Insira o link do vídeo:", font=("Arial", 14)).pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.url_var, width=400).pack(pady=5)

        # Seleção de qualidade do vídeo
        ctk.CTkLabel(self, text="Qualidade:", font=("Arial", 12)).pack()
        ctk.CTkComboBox(self, values=["144p", "240p", "360p", "480p", "720p", "1080p"], variable=self.quality_var).pack(pady=5)

        # Seleção do formato (vídeo ou áudio)
        ctk.CTkLabel(self, text="Formato:", font=("Arial", 12)).pack()
        ctk.CTkComboBox(self, values=["Vídeo", "Áudio"], variable=self.file_format_var).pack(pady=5)

        # Botão para selecionar pasta de destino
        ctk.CTkButton(self, text="Selecionar Pasta", command=self.select_folder).pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.folder_var, width=400, state="disabled").pack(pady=5)

        # Botão para iniciar o download
        ctk.CTkButton(self, text="Baixar", command=self.start_download, fg_color="green").pack(pady=20)

        # Barra de progresso do download
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)  # Inicializa zerada
        self.progress_bar.pack(pady=10)

    def select_folder(self):
        """Abre o explorador de arquivos para que o usuário escolha a pasta de destino"""
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)  # Define a pasta selecionada

    def update_progress(self, progress):
        """Atualiza a barra de progresso da interface"""
        self.after(10, self.progress_bar.set, progress)

    def start_download(self):
        """Inicia o processo de download do vídeo"""

        # Obtém os valores inseridos pelo usuário
        url = self.url_var.get()
        quality = self.quality_var.get()
        file_format = self.file_format_var.get()
        output_path = self.folder_var.get() or os.getcwd()  # Usa a pasta atual se nenhuma for selecionada

        # Verifica se a URL foi inserida
        if not url:
            messagebox.showerror("Erro", "Insira um link válido!")
            return

        self.progress_bar.set(0)  # Reinicia a barra de progresso

        def run_download():
            """Executa o download em uma thread separada"""
            try:
                download_video(url, quality, file_format, output_path, self.update_progress)
                messagebox.showinfo("Sucesso", "Download concluído!")  # Exibe mensagem de sucesso
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao baixar: {str(e)}")  # Exibe mensagem de erro

        # Inicia o download em uma nova thread para não travar a interface gráfica
        threading.Thread(target=run_download, daemon=True).start()


if __name__ == "__main__":
    # Cria e executa a aplicação
    app = TubeLoadApp()
    app.mainloop()
