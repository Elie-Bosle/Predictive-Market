import requests
import json
import time
import pandas as pd
import os
import sys

# Ajouter le dossier parent au path pour pouvoir importer read_json_pandas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from read_json_pandas import translate_and_convert_to_csv

def get_all_opened_markets():
    """Récupère tous les marchés ouverts de Polymarket"""
    base_url = "https://gamma-api.polymarket.com/markets"
    all_markets = []
    offset = 0
    limit = 100  
        
    while True:
        params = {
            "closed": "false",
            "limit": limit,
            "offset": offset
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if not data or len(data) == 0:
                break
                
            all_markets.extend(data)
            
            if len(data) < limit:
                print(f"{len(all_markets)} récupérés")
                break
                
            offset += limit
            time.sleep(0.1)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            break
    
    return all_markets

def save_markets_to_json(markets, filename='../polymarket_data.json'):
    """Sauvegarde les marchés dans un fichier JSON dans le dossier principal"""
    try:
        # Ouvrir en mode 'w' pour écraser l'ancien fichier s'il existe
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(markets, f, indent=2, ensure_ascii=False)
        print(f"✅ {len(markets)} marchés sauvegardés dans '{filename}'")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")
        return False

def clean_old_files():
    """Nettoie les anciens fichiers s'ils existent dans le dossier principal"""
    old_files = ['../polymarket_data.json', '../Polymarket_open.csv']
    for filename in old_files:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                print(f"❌ Erreur lors de la suppression de {filename}: {e}")

def main():
    # Nettoyer les anciens fichiers
    clean_old_files()
    
    # Récupérer tous les marchés ouverts
    markets = get_all_opened_markets()
    
    if markets:
        # Sauvegarder dans un fichier JSON dans le dossier principal
        if save_markets_to_json(markets):
            print(f"Total de marchés ouverts: {len(markets)}")
            
            # Convertir en CSV en gardant les noms de colonnes originaux
            # Le fichier CSV sera stocké dans le dossier principal
            translate_and_convert_to_csv(markets, '../Polymarket_open.csv')
    else:
        print("❌ Aucun marché récupéré")

if __name__ == "__main__":
    main()