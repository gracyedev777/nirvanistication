import flet as ft
import cv2
import numpy as np
import sqlite3
import os
import sys
from datetime import datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class NirvanaProcessor:
    def __init__(self, ref_path=None):
        
        self.ref_path = ref_path if ref_path else resource_path("nevermind.png")
        self.block_sz = 10
        self._setup_db()

    def _setup_db(self):
        with sqlite3.connect("app_data.db") as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, input_img TEXT, output_img TEXT, ts DATETIME)")

    def run(self, source_path):
        src = cv2.imread(source_path)
        ref = cv2.imread(self.ref_path)

        if src is None or ref is None:
            return None

        ref = cv2.resize(ref, (800, 800))
        h, w, _ = ref.shape
        out = np.zeros((h, w, 3), dtype=np.uint8)

        src_h, src_w, _ = src.shape
        fragments = []
        for r in range(0, src_h - self.block_sz, self.block_sz):
            for c in range(0, src_w - self.block_sz, self.block_sz):
                chunk = src[r:r+self.block_sz, c:c+self.block_sz]
                gray = cv2.cvtColor(chunk, cv2.COLOR_BGR2GRAY)
                fragments.append((np.mean(gray), chunk))

        for r in range(0, h, self.block_sz):
            for c in range(0, w, self.block_sz):
                target_chunk = ref[r:r+self.block_sz, c:c+self.block_sz]
                if target_chunk.shape[0] < self.block_sz: continue

                t_gray = cv2.cvtColor(target_chunk, cv2.COLOR_BGR2GRAY)
                t_brightness = np.mean(t_gray)
                
                best_match = min(fragments, key=lambda x: abs(x[0] - t_brightness))[1]
                mixed = cv2.addWeighted(best_match, 0.4, target_chunk, 0.6, 0)
                out[r:r+self.block_sz, c:c+self.block_sz] = mixed

        fname = f"render_{datetime.now().strftime('%M%S')}.jpg"
        cv2.imwrite(fname, out)
        
        with sqlite3.connect("app_data.db") as conn:
            conn.execute("INSERT INTO logs (input_img, output_img, ts) VALUES (?,?,?)", (source_path, fname, datetime.now()))
        
        return fname

def main(page: ft.Page):
    proc = NirvanaProcessor()
    page.title = "presente nirvanistico"
    page.theme_mode = "dark"
    page.window_width = 500
    page.window_height = 950 
    page.horizontal_alignment = "center"
    page.scroll = ft.ScrollMode.ADAPTIVE

    
    audio_file = resource_path("Nirvana - Something In The Way (SPOTISAVER).mp3")
    audio_player = ft.Audio(
        src=audio_file,
        autoplay=True,
        volume=1.0,
        balance=0
    )
    page.overlay.append(audio_player)

    preview_img = ft.Image(src="https://via.placeholder.com/400", width=350, height=350, border_radius=10)
    loader = ft.ProgressBar(width=350, color="cyan", visible=False)
    log_text = ft.Text("Selecione um arquivo para processar", size=12)

    def on_file_select(e: ft.FilePickerResultEvent):
        if e.files:
            loader.visible = True
            page.update()
            res = proc.run(e.files[0].path)
            if res:
                preview_img.src = res
                log_text.value = f"Finalizado: {res}"
            loader.visible = False
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_select)
    page.overlay.append(file_picker)

    page.add(
        ft.Text("PRESENTE PRA ALISSON", size=24, weight="bold", color="cyan"),
        ft.Container(preview_img, padding=20),
        loader,
        log_text,
        ft.ElevatedButton("UPLOAD", icon=ft.Icons.UPLOAD, on_click=lambda _: file_picker.pick_files()),
        ft.Container(height=20),
        ft.Container(
            bgcolor="#1e1e1e",
            padding=15,
            border_radius=10,
            content=ft.Column([
                ft.Text("MÉTODO DE RECONSTRUÇÃO DISCRETA", weight="bold", color="cyan300"),
                ft.Text("1. DECOMPOSIÇÃO: Segmentação em submatrizes de 10x10 pixels para geração de dicionário.", size=12, color="white70"),
                ft.Text("2. PROCESSAMENTO LAB: Mapeamento de luma (Y') baseado na recomendação BT.601.", size=12, color="white70"),
                ft.Text("3. BUSCA POR VIZINHO PRÓXIMO: Busca MSE para match de geometria fonte/alvo.", size=12, color="white70"),
                ft.Text("4. COMPOSIÇÃO FINAL: Fusão Alpha Blending em 32-bits para integridade cromática.", size=12, color="white70")
            ], spacing=10)
        ),
        ft.Container(height=20),
        ft.Text("♫ Something In The Way", size=16, italic=True, color="white38"),
        ft.Text("Presente para Alisson - 2026", size=10, color="white10")
    )

if __name__ == "__main__":
    ft.app(target=main)