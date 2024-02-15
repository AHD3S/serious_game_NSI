import pygame
import json

# Définition des couleurs
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
NOIR = (0, 0, 0)

class BoutonCreer:
    def __init__(self, x, y, texte):
        self.texte = texte
        self.font = pygame.font.Font(None, 36)
        texte_surface = self.font.render(self.texte, True, NOIR)
        self.rect = texte_surface.get_rect()
        self.rect.topleft = (x, y)
        self.couleur = BLANC
        self.couleur_hover = GRIS
        self.popup_affiche = False
        self.texte_entreprise = ""
        self.texte_pdg = ""
        self.saisie_entreprise = True  # Indicateur de saisie active
        self.visible = True

    def afficher(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.couleur, self.rect)
            texte_surface = self.font.render(self.texte, True, NOIR)
            texte_rect = texte_surface.get_rect(center=self.rect.center)
            surface.blit(texte_surface, texte_rect)

    def gestion_evenements(self, event):
        if self.visible:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.couleur = self.couleur_hover
                else:
                    self.couleur = BLANC
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.popup_affiche = True  # Ouvre le popup

    def afficher_popup(self, surface):
        if self.popup_affiche:
            # Fond gris du popup
            popup_surface = pygame.Surface((1230, 680))
            popup_surface.fill(GRIS)
            popup_rect = popup_surface.get_rect(center=(1280 // 2, 720 // 2))
            surface.blit(popup_surface, popup_rect)
            pygame.draw.rect(surface, NOIR, popup_rect, 2)
            
            # Affichage du nom de l'entreprise saisi
            texte_saisi_surface = self.font.render("Nom de l'entreprise : " + self.texte_entreprise, True, NOIR)
            texte_saisi_rect = texte_saisi_surface.get_rect(center=(1280 // 2, (720 // 2) - 20))
            surface.blit(texte_saisi_surface, texte_saisi_rect)

            # Affichage du nom du PDG saisi
            texte_pdg_surface = self.font.render("Nom du PDG : " + self.texte_pdg, True, NOIR)
            texte_pdg_rect = texte_pdg_surface.get_rect(center=(1280 // 2, (720 // 2) + 20))
            surface.blit(texte_pdg_surface, texte_pdg_rect)

            # Bouton Commencer
            bouton_commencer_rect = pygame.Rect(0, 0, 200, 50)
            bouton_commencer_rect.center = (1280 // 2, (720 // 2) + 80)
            pygame.draw.rect(surface, BLANC, bouton_commencer_rect)
            pygame.draw.rect(surface, NOIR, bouton_commencer_rect, 2)
            texte_bouton_commencer = self.font.render("Commencer", True, NOIR)
            texte_bouton_commencer_rect = texte_bouton_commencer.get_rect(center=bouton_commencer_rect.center)
            surface.blit(texte_bouton_commencer, texte_bouton_commencer_rect)

            if bouton_commencer_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.sauvegarder_donnees()  # Sauvegarde les données dans un fichier JSON
                self.texte_entreprise = ""  # Effacer le texte saisi pour le nom de l'entreprise
                self.texte_pdg = ""  # Effacer le texte saisi pour le nom du PDG
                self.popup_affiche = False  # Fermer le popup

    def ajouter_texte_popup(self, event):
        if self.popup_affiche and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.saisie_entreprise:
                    self.texte_entreprise = self.texte_entreprise[:-1]
                else:
                    self.texte_pdg = self.texte_pdg[:-1]
            elif event.key == pygame.K_RETURN:
                self.saisie_entreprise = not self.saisie_entreprise  # Changer de saisie
            elif len(self.texte_entreprise) < 25 and self.saisie_entreprise:
                self.texte_entreprise += event.unicode
            elif len(self.texte_pdg) < 25 and not self.saisie_entreprise:
                self.texte_pdg += event.unicode

    def sauvegarder_donnees(self):
        # Créer un dictionnaire avec les données à sauvegarder
        donnees = {'nom_entreprise': self.texte_entreprise, 'nom_pdg': self.texte_pdg}

        # Écrire les données dans un fichier JSON
        with open('donnees.json', 'w') as f:
            json.dump(donnees, f)

class BoutonQuitter:
    def __init__(self, x, y, texte):
        self.texte = texte
        self.font = pygame.font.Font(None, 36)
        texte_surface = self.font.render(self.texte, True, NOIR)
        self.rect = texte_surface.get_rect()
        self.rect.topleft = (x, y)
        self.couleur = BLANC
        self.couleur_hover = GRIS
        self.visible = True

    def afficher(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.couleur, self.rect)
            texte_surface = self.font.render(self.texte, True, NOIR)
            texte_rect = texte_surface.get_rect(center=self.rect.center)
            surface.blit(texte_surface, texte_rect)

    def gestion_evenements(self, event):
        if self.visible:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.couleur = self.couleur_hover
                else:
                    self.couleur = BLANC
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    pygame.quit()

# Initialisation de Pygame
pygame.init()
TAILLE_ECRAN = (1280, 720)
ecran = pygame.display.set_mode(TAILLE_ECRAN)
pygame.display.set_caption("SeriousGame")

bouton_creer = BoutonCreer(50, 50, "Créer une entreprise")
bouton_quitter = BoutonQuitter(50, 120, "Quitter")

# Boucle principale
continuer = True
while continuer:
    ecran.fill(BLANC)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        bouton_creer.gestion_evenements(event)
        bouton_quitter.gestion_evenements(event)
        bouton_creer.ajouter_texte_popup(event)

    bouton_creer.afficher(ecran)
    bouton_quitter.afficher(ecran)
    bouton_creer.afficher_popup(ecran)

    pygame.display.flip()

    if bouton_creer.popup_affiche:  # Si le popup est affiché
        bouton_creer.visible = False
        bouton_quitter.visible = False
    else:
        bouton_creer.visible = True
        bouton_quitter.visible = True

pygame.quit()
