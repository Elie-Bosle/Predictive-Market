import pandas as pd
import json

def translate_and_convert_to_csv(data, csv_filename='Polymarket_open.csv'):
    """Convertit les données en CSV avec pandas en gardant les noms de colonnes originaux"""
    try:
        # Créer le DataFrame pandas
        df = pd.DataFrame(data)
        print(f"\n📊 DataFrame créé avec {len(df)} lignes et {len(df.columns)} colonnes")
        
                
        df.to_csv(csv_filename, index=False, encoding='utf-8')
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la conversion CSV: {e}")
        return False

# Ce fichier contient maintenant seulement la fonction translate_and_convert_to_csv
# Le code principal a été supprimé pour éviter la duplication
