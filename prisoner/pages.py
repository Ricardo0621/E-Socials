from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
            same_choice=me.decision == opponent.decision,
        )
class Consent(Page):
    form_model = 'player' #Le dice que es un jugador
    form_fields = ['accepts_data', 'name', 'id_cc', 'accepts_terms']
    def is_displayed(self):
        return self.round_number == 1

class CombinedResults(Page):
    #Cuando uno le quiere mostrar algo al usuario
    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        combined_payoff = 0
        for player in all_players:
            combined_payoff += player.payoff
        return {
            'combined_payoff' : combined_payoff
        }

page_sequence = [Consent, Introduction, Decision, ResultsWaitPage, Results, CombinedResults]
