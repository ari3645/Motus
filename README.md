# 🎮 Projet Motus Elite (Python)

Bienvenue dans cette version moderne et boostée du célèbre jeu **Motus** ! Ce projet propose une expérience complète en Python, jouable soit dans votre terminal, soit via une interface graphique élégante.

## ✨ Fonctionnalités
- **Deux modes de jeu** : Console (CLI) ou Graphique (GUI).
- **Connexion API** : Jouez avec l'intégralité des mots de la langue française grâce à l'intégration de l'API Heroku (Random Word) et Wiktionary.
- **Dictionnaires Locaux** : Possibilité de jouer sans connexion internet avec vos propres listes de mots.
- **Difficulté ajustable** : 3 niveaux de difficulté impactant le temps et les indices.
- **Définitions** : Apprenez de nouveaux mots avec l'affichage de la définition à la fin de chaque partie en ligne.

## 🚀 Installation & Lancement

### Prérequis
Assurez-vous d'avoir Python installé. Vous aurez également besoin de la bibliothèque `requests` pour le mode API :
```bash
pip install requests
```

### Lancer le jeu
- **Pour l'interface graphique (recommandé) :**
  ```bash
  python gui.py
  ```
- **Pour le terminal :**
  ```bash
  python cli.py
  ```

## ⚙️ Configuration du jeu

Au lancement, vous pourrez configurer :
1. **Source des mots** : Mode API (tous les mots français) ou Mode Local (fichiers .txt).
2. **Longueur du mot** : De 2 à 15 lettres.
3. **Difficulté** :
   - **Facile** : 90 secondes + 1ère et dernière lettres dévoilées.
   - **Moyen** : 60 secondes + 1ère lettre dévoilée.
   - **Difficile** : 30 secondes + aucune lettre dévoilée.

## 📏 Règles du Jeu (Motus)

Le but est de deviner un mot secret en un nombre limité d'essais (7 essais par défaut).

### Code Couleur :
- **ROUGE** : La lettre est **bien placée**.
- **JAUNE** : La lettre est présente dans le mot mais **mal placée**.
- **GRIS** : La lettre n'est **pas présente** dans le mot.

*Note : Les accents sont automatiquement gérés pour permettre une saisie simplifiée.*

---
Projet développé avec passion pour l'apprentissage et le fun !
