import random
import json
class Pokemon:
    def __init__(self, nom, attaque, defense, points_de_vie):
       self.__nom = nom
       self.__points_de_vie = points_de_vie
       self.__attaque = attaque
       self.__defense = defense

    def get_nom(self):
      return self.__nom
    
    def get_points_de_vie(self):
      return self.__points_de_vie

    def set_points_de_vie(self, points_de_vie):
      self.__points_de_vie = points_de_vie

    def get_attaque(self):
      return self.__attaque

    def get_defense(self):
       return self.__defense
    


    def afficher_informations(self):
      print("Nom:", self.__nom)
      print("Points de vie:", self.__points_de_vie)
      print("Attaque:", self.__attaque)
      print("Défense:", self.__defense)




class Pokemon_normal(Pokemon):
    def __init__(self, nom):
      super().__init__(nom, 100, 10, 100)
      

    def afficher_pokemon_normal(self):
      super().afficher_informations()


class Pokemon_feu(Pokemon):
    def __init__(self, nom):
      super().__init__(nom, 80, 15, 100)
    

    def afficher_pokemon_feu(self):
        super().afficher_informations()


class Pokemon_eau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, 120, 5, 100)


    def afficher_pokemon_eau(self):
        super().afficher_informations()


class Pokemon_terre(Pokemon):
    def __init__(self, nom):
        super().__init__(self, nom, 90, 10, 100)

    def afficher_pokemon_terre(self):
        super().afficher_informations()
    



class Combat:
    def __init__(self, pokemon1, pokemon2):

        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        
    def plus_en_vie(self):
       if self.pokemon1.get_points_de_vie() <= 0:
          return self.pokemon2
       elif self.pokemon2.get_points_de_vie() <= 0:
          return self.pokemon1
       else:
          return None

    def get_vainqueur(self):
       if self.pokemon1.get_points_de_vie() > 0:
          return self.pokemon1.get_nom()
       else:
          return self.pokemon2.get_nom()
        
    def attaque(self, attaquant, defenseur):
      if random.randint(0, 1) == 1:
          degats = attaquant.get_attaque() - defenseur.get_defense()
          if degats < 0:
             degats = 0
          defenseur.set_points_de_vie(defenseur.get_points_de_vie() - degats)
          print(attaquant.get_nom(), "inflige", degats, "points de dégâts à", defenseur.get_nom())
      else:
          print(attaquant.get_nom(), "a raté son attaque")





    def enlever_vies(self, attaquer, defenseur):
        degats = self.calculer_degats(attaquer, defenseur)
        defenseur.vies -= degats

    def obtenir_nom_perdant(self):
        if self.pokemon1.get_points_de_vie() <= 0:
            return self.joueur.nom
        elif self.pokemon2.get_points_de_vie() <= 0:
            return self.adversaire.nom
        else:
            return None
        
    
    def enregistrer_pokemon(self, pokemon):
        with open("pokedex.json", "r") as f:
            pokedex = json.load(f)

        if pokemon.nom not in pokedex:
            pokedex[pokemon.nom] = {
                "type": pokemon.type,
                "attaque": pokemon.attaque,
                "defense": pokemon.defense,
                "vies": pokemon.vies
            }

        with open("pokedex.json", "w") as f:
            json.dump(pokedex, f, indent=4)

    
    
  
