# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, simpledialog
from engine import MotusEngine
import os

class DifficultyDialog(simpledialog.Dialog):
    def body(self, master):
        self.result = "Moyen"
        tk.Label(master, text="Choisissez la difficulté :", font=("Segoe UI", 12)).pack(pady=10)
        self.var = tk.StringVar(value="Moyen")
        opts = [("Facile (90s, 1ère & Dernière lettre)", "Facile"), 
                ("Moyen (60s, 1ère lettre)", "Moyen"), 
                ("Difficile (30s, Aucune lettre)", "Difficile")]
        for text, val in opts:
            tk.Radiobutton(master, text=text, variable=self.var, value=val, 
                           font=("Segoe UI", 10)).pack(anchor="w", padx=20)
        return master
    def apply(self):
        self.result = self.var.get()

class MotusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Motus Python Elite API")
        self.root.configure(bg="#f0f2f5")
        
        # 1. Mode API ou Local ?
        self.use_api = messagebox.askyesno("Mode de jeu", "Voulez-vous jouer avec l'API en ligne ?")
        
        # 2. Longueur
        self.longueur = simpledialog.askinteger("Configuration", "Longueur du mot (2-15) :", 
                                               initialvalue=7, minvalue=2, maxvalue=15)
        if not self.longueur: self.root.destroy(); return
            
        # 3. Difficulté
        self.difficulte = self.demander_difficulte()
        if not self.difficulte: self.root.destroy(); return

        temps_map = {"Facile": 90, "Moyen": 60, "Difficile": 30}
        self.temps_restant = temps_map.get(self.difficulte, 60)
            
        chemin_dico = None
        if not self.use_api:
            chemin_dico = self.trouver_dictionnaire(self.longueur)
            if not chemin_dico:
                messagebox.showerror("Erreur", "Dictionnaire local introuvable.")
                self.root.destroy(); return

        try:
            self.jeu = MotusEngine(dictionnaire_path=chemin_dico, longueur=self.longueur, 
                                   use_api=self.use_api, mode_difficulte=self.difficulte)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            self.root.destroy(); return
            
        self.labels = []
        self.timer_running = True
        self.root.geometry(f"{max(450, self.longueur * 50)}x700")
        self.creer_interface()
        self.afficher_indices()
        self.update_timer()

    def demander_difficulte(self):
        dialog = DifficultyDialog(self.root, "Niveau de difficulté")
        return dialog.result

    def trouver_dictionnaire(self, longueur):
        chemins = [f"data/dico{longueur}lettre.txt", f"dico{longueur}lettre.txt"]
        for c in chemins:
            if os.path.exists(c): return c
        return None

    def creer_interface(self):
        header = tk.Frame(self.root, bg="#1a73e8", height=80)
        header.pack(fill="x")
        tk.Label(header, text=f"MOTUS - {self.difficulte.upper()}", fg="white", bg="#1a73e8", font=("Segoe UI", 24, "bold")).pack(pady=10)
        
        self.lbl_timer = tk.Label(self.root, text=f"Temps : {self.temps_restant}s", font=("Segoe UI", 16, "bold"), bg="#f0f2f5", fg="#d93025")
        self.lbl_timer.pack(pady=10)
        
        self.grid_frame = tk.Frame(self.root, bg="#f0f2f5")
        self.grid_frame.pack(pady=20)
        
        for r in range(self.jeu.tentatives_max):
            row_labels = []
            for c in range(self.jeu.taille):
                lbl = tk.Label(self.grid_frame, text=".", width=3, height=1, relief="flat", font=("Consolas", 20, "bold"), bg="white", fg="#bdc1c6")
                lbl.grid(row=r, column=c, padx=4, pady=4)
                row_labels.append(lbl)
            self.labels.append(row_labels)
            
        control = tk.Frame(self.root, bg="#f0f2f5")
        control.pack(pady=20)
        self.entree = tk.Entry(control, font=("Segoe UI", 18), width=self.longueur + 2, justify="center")
        self.entree.pack(side="left", padx=10)
        self.entree.focus_set()
        self.entree.bind("<Return>", lambda e: self.valider())
        tk.Button(control, text="VALIDER", command=self.valider, bg="#1a73e8", fg="white", font=("Segoe UI", 12, "bold")).pack(side="left")

    def update_timer(self):
        if self.timer_running and self.temps_restant > 0:
            self.temps_restant -= 1
            self.lbl_timer.config(text=f"Temps : {self.temps_restant}s")
            self.root.after(1000, self.update_timer)
        elif self.temps_restant <= 0:
            self.timer_running = False
            messagebox.showinfo("Temps écoulé", f"Le mot était : {self.jeu.secret}")
            self.root.destroy()

    def afficher_indices(self):
        etat = self.jeu.obtenir_etat()
        row = self.jeu.tentatives_faites
        for i, lettre in enumerate(etat["indices_decouverts"]):
            if row < self.jeu.tentatives_max and lettre != "_":
                self.labels[row][i].config(text=lettre, fg="#1a73e8")

    def valider(self):
        mot = self.entree.get().upper()
        self.entree.delete(0, tk.END)
        res = self.jeu.proposer_mot(mot)
        if res == "WRONG_SIZE": messagebox.showwarning("Attention", f"Il faut {self.jeu.taille} lettres !"); return
        elif res == "NOT_IN_DICT": messagebox.showwarning("Inconnu", f"'{mot}' est inconnu."); return
        
        row = self.jeu.tentatives_faites - 1
        for i, lettre in enumerate(res):
            lbl = self.labels[row][i]
            if lettre.isupper(): lbl.config(text=lettre, bg="#d93025", fg="white")
            elif lettre.islower(): lbl.config(text=lettre.upper(), bg="#f9ab00", fg="white")
            else: lbl.config(text=mot[i], bg="#5f6368", fg="white")
                
        etat = self.jeu.obtenir_etat()
        if etat["termine"]:
            self.timer_running = False
            msg = f"Mot : {etat['secret']}"
            if etat["definition"]: msg += f"\n\nDéfinition : {etat['definition']}"
            messagebox.showinfo("Fin de partie", msg)
            self.root.destroy()
        else:
            self.afficher_indices()

if __name__ == "__main__":
    root = tk.Tk()
    app = MotusGUI(root)
    root.mainloop()
