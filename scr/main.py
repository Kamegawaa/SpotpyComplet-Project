print("🎬 Iniciando o Autocomplete Playlist...")

from spotify_api import init_spotify

def main():
    try:
        print("🔍 Iniciando autenticação...")
        sp = init_spotify()

        print("🔍 Autenticado. Buscando faixa...")
        results = sp.search(q="Photograph Ed Sheeran", type="track", limit=1)

        print("🔍 Resultado recebido!")
        track = results['tracks']['items'][0]
        print(f"🎵 {track['name']} - {track['artists'][0]['name']}")

    except Exception as e:
        print("🚨 Entrou no except!")
        print(f"❌ Erro ao executar: {e}")

if __name__ == "__main__":
    main()