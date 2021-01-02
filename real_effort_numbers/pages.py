from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, math

class AddNumbers(Page):
    #Falta algoritmo de asignación de equipos
    form_model = 'player'
    form_fields = ['number_entered']
    timer_text = 'Tiempo restante para completar la Etapa 1:'

    def before_next_page(self):
        self.player.total_sums = 1
        if self.player.sum_of_numbers == self.player.number_entered:
            self.player.payoff = Constants.payment_per_correct_answer
            self.player.correct_answers = 1
        else:
            self.player.wrong_sums = 1    
        return

    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        #Luego de que se acaba el tiempo, se salta las rondas (no las muestra) y va automáticamente a la siguiente página (Pagos).
        if self.round_number <= 4:
            return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        correct_answers = 0
        combined_payoff = 0
        combined_payoff_others = 0
        wrong_sums = 0
        total_sums = 0
        self.player.sum_of_numbers = number_1 + number_2
        all_players = self.player.in_all_rounds()
        me = self.player.id_in_group
        me_in_session = self.player.participant.id_in_session
        #opponent = self.player.other_player().id_in_group #self.player.get_others_in_group()[0].id_in_group
        others = self.player.get_others_in_group()[0] #Como es un juego de dos jugadres, devuelve al oponente. Nótese que "Oponente" es sólamente el id del otro jugador en el grupo
        opponent = self.player.other_player()
        correct_answers_opponent = 0
        opponent_id = self.player.other_player().id_in_group
        # Matriz del grupo: 
        # [[<Player  1>, <Player  2>], 
        # [<Player  3>, <Player  4>]]
        # Yo: 1
        # Yo en la sesión: 1
        # Oponente: 2 
        # all_players: Jugadores en todas las rondas. O sea yo, en mi ronda.
        # Others: Otros jugadores (distintos a mí) en el grupo. 
        # print("Yo " + str(me))
        # print("Yo en la sesión " + str(me_in_session))
        # print("Oponente " + str(opponent))
        # print("All players: " + str(all_players))
        # print("Others: " + str(others))
        # print("Epa: " + str(self.player.get_others_in_subsession()))
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            wrong_sums += player.wrong_sums
            total_sums += player.total_sums
        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums,
            'total_sums': total_sums
        }

class AddNumbers2(Page):
    #Falta algoritmo de asignación de equipos
    form_model = 'player'
    form_fields = ['number_entered_2']
    timer_text = 'Tiempo restante para completar la Etapa 2:'
    

    def before_next_page(self):
        self.player.total_sums_2 = 1
        if self.player.sum_of_numbers_2 == self.player.number_entered_2:
            self.player.pago = Constants.payment_per_correct_answer_2
            self.player.correct_answers_2 = 1
        else:
            self.player.wrong_sums_2 = 1    
        return

    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        #Luego de que se acaba el tiempo, se salta las rondas (no las muestra) y va automáticamente a la siguiente página (Pagos).
        if self.round_number >= 5:
            return self.get_timeout_seconds() > 3    

    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        correct_answers = 0
        combined_payoff = 0
        combined_payoff_others = 0
        wrong_sums_2 = 0
        total_sums_2 = 0
        self.player.sum_of_numbers_2 = number_1 + number_2
        all_players = self.player.in_all_rounds()
        me = self.player.id_in_group
        me_in_session = self.player.participant.id_in_session
        #opponent = self.player.other_player().id_in_group #self.player.get_others_in_group()[0].id_in_group
        others = self.player.get_others_in_group()[0] #Como es un juego de dos jugadres, devuelve al oponente. Nótese que "Oponente" es sólamente el id del otro jugador en el grupo
        opponent = self.player.other_player()
        correct_answers_opponent = 0
        opponent_id = self.player.other_player().id_in_group
        # Matriz del grupo: 
        # [[<Player  1>, <Player  2>], 
        # [<Player  3>, <Player  4>]]
        # Yo: 1
        # Yo en la sesión: 1
        # Oponente: 2 
        # all_players: Jugadores en todas las rondas. O sea yo, en mi ronda.
        # Others: Otros jugadores (distintos a mí) en el grupo. 
        # print("Yo " + str(me))
        # print("Yo en la sesión " + str(me_in_session))
        # print("Oponente " + str(opponent))
        # print("All players: " + str(all_players))
        # print("Others: " + str(others))
        # print("Epa: " + str(self.player.get_others_in_subsession()))
        for player in all_players:
            combined_payoff += player.pago
            correct_answers += player.correct_answers_2
            wrong_sums_2 += player.wrong_sums_2
            total_sums_2 += player.total_sums_2
        return {
            'number_1': number_1,
            'number_2': number_2,
            'combined_payoff' : math.trunc(combined_payoff),
            'correct_answers': correct_answers,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'wrong_sums': wrong_sums_2,
            'total_sums': total_sums_2
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

class Stage2Instructions(Page):
    def is_displayed(self):
        return self.round_number == 4        

class Stage2Questions(Page):
    form_model = 'player'
    form_fields = ['control_question_3', 'control_question_4', 'control_question_5', 'control_question_6', 'control_question_7']
    def is_displayed(self):
        return self.round_number == 4        

class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + 60

class Start2(Page):
    def is_displayed(self):
        return self.round_number == 4   

    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + 5*60        

class Consent(Page):
    form_model = 'player'
    form_fields = ['accepts_data', 'num_temporal', 'accepts_terms']

    def is_displayed(self):
        return self.round_number == 1

class ResultsWaitPage(WaitPage):
    #Muestra el WaitPage al final de la cuarta ronda. Antes del pago
    def is_displayed(self):
        return self.round_number == 4

class RoleAssignment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 4

class Decision(Page):
    form_model = 'player'
    form_fields = ['pay_contract', 'believe_pay_contract', 'suggested_sums']
    def is_displayed(self):
        return self.round_number == 4
    def vars_for_template(self):
        me = self.player.id_in_group
        titulo = ""
        if me == 1:
            titulo = "Decision Jugador X - Parte 1"
        else:
            titulo = "Decision Jugador Y - Parte 1"
        return{
                'titulo': titulo
            }

class Decision2(Page):
    form_model = 'player'
    form_fields = ['suggested_sums']
    def is_displayed(self):
        return self.round_number == 4 
    def vars_for_template(self):
        me = self.player.id_in_group
        opponent = self.player.other_player()
        opponent_contract_decision = opponent.pay_contract
        opponent_suggested_sums = opponent.suggested_sums
        titulo = ""
        if me == 1:
            titulo = "Reporte de decisión Jugador X"
        else:
            titulo = "Decision Jugador Y - Parte 2"
        return{
                'titulo': titulo,
                'opponent_contract_decision': opponent_contract_decision,
                'opponent_suggested_sums': opponent_suggested_sums
            }

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == 4

    def vars_for_template(self):
        # self.player.get_others_in_group()[0] == self.player.other_player() -> Player Object
        all_players = self.player.in_all_rounds()
        all_others = self.player.get_others_in_group()[0].in_all_rounds()
        others = self.player.get_others_in_group()[0]
        combined_payoff = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        combined_payoff_total = 0
        opponent = self.player.other_player()
        opponent_id = self.player.other_player().id_in_group
        # print("Yo " + str(me))
        # print("Oponente " + str(opponent_id))
        # print("Other " + str(others))
        # print("All Others " + str(all_others))
        # print("Group players" + str(self.group.get_players()))
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers
            correct_answers_opponent += player.other_player().correct_answers
            combined_payoff_opponent += player.other_player().payoff

        correct_answers_team = correct_answers + correct_answers_opponent
        combined_payoff_team = combined_payoff + combined_payoff_opponent
        combined_payoff_total = combined_payoff + Constants.fixed_payment
        self.player.payment_stage_1 = math.trunc(combined_payoff_total)
        print("Jugador "+ str(player.id_in_group) + ". Pago total "+ str(self.player.payment_stage_1))
        return {
            'combined_payoff' : math.trunc(combined_payoff),
            'combined_payoff_opponent': math.trunc(combined_payoff_opponent),
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'round_number' : self.round_number,
            'opponent_id': opponent_id,
            'correct_answers_team': correct_answers_team,
            'combined_payoff_team': math.trunc(combined_payoff_team),
            'combined_payoff_total': math.trunc(combined_payoff_total)
        }
page_sequence = [Consent, GenInstructions,Stage1Instructions, Stage1Questions, Start, AddNumbers, ResultsWaitPage,  CombinedResults, Stage2Instructions, Stage2Questions, RoleAssignment, Decision,ResultsWaitPage, Decision2, Start2, AddNumbers2 ]
# page_sequence = [Start, AddNumbers, ResultsWaitPage, CombinedResults, Stage2Instructions, Stage2Questions, RoleAssignment, Decision, ResultsWaitPage, Decision2, Start2, AddNumbers2]
# page_sequence = [Decision, ResultsWaitPage, Decision2]

