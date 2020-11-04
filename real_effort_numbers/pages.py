from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class AddNumbers(Page):
    form_model = "player"
    form_fields = ["number_entered"]
    #Siempre la clase Players esta definida en casa models.py
    def vars_for_template(self): #Genera variables que luego se pueden usar en las templates
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        self.player.sum_of_numbers = number_1 + number_2
        #El return no puede ir vacio, algo en la siguiente linea debe seguirlo
        return {
            'number_1': number_1,
            'number_2': number_2,
        }
    
    def before_next_page(self):
        if self.player.sum_of_numbers == self.player.number_entered:
            self.player.payoff = Constants.payment_per_correct_answer
        return 

class Results(Page):
    pass

class CombinedResults(Page):
    #Lo que se muestra en la primera página I guess
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    #Cuando uno le quiere mostrar algo al usuario
    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        combined_payoff = 0
        for player in all_players:
            combined_payoff += player.payoff
        return {
            'combined_payoff' : combined_payoff
        }
page_sequence = [AddNumbers, Results, CombinedResults]
