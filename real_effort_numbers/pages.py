from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, math

class AddNumbers(Page):
    form_model = 'player'
    form_fields = ['number_entered']
    timer_text = 'Tiempo restante para completar esta etapa:'

    def before_next_page(self):
        if self.player.sum_of_numbers == self.player.number_entered:
            self.player.payoff = Constants.payment_per_correct_answer
            self.player.correct_answers = 1
        return

    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        #Luego de que se acaba el tiempo, se salta las rondas (no las muestra) y va automáticamente a la siguiente página (Pagos).
        return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        self.player.sum_of_numbers = number_1 + number_2
        all_players = self.player.in_all_rounds()
        correct_answers = 0
        combined_payoff = 0
        opponent = self.player.other_player()
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
            'opponent': opponent
        }
    
class GenInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Stage1Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Stage1Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_1', 'control_question_2']
    def is_displayed(self):
        return self.round_number == 1

class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + 60

class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_data', 'num_temporal', 'accepts_terms']
    def is_displayed(self):
        return self.round_number == 1

class ResultsWaitPage(WaitPage):
    #Muestra el WaitPage al final de la cuarta ronda. Antes del pago
    def is_displayed(self):
        return self.round_number == 4

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        combined_payoff = 0
        correct_answers = 0
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
        }
# page_sequence = [Consent, GenInstructions,Stage1Instructions, Stage1Questions, Start, AddNumbers, ResultsWaitPage,  CombinedResults]
page_sequence = [Start, AddNumbers, ResultsWaitPage, CombinedResults]


