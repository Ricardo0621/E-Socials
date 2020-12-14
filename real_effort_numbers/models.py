from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers'
    players_per_group = 4
    num_rounds = 4
    payment_per_correct_answer = 50

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    number_entered = models.IntegerField(label="")
    sum_of_numbers = models.IntegerField()
    correct_answers = models.IntegerField(initial=0)
# ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    control_question_1 = models.BooleanField(
        label="¿Estaré emparejado con la misma persona en toda la Etapa 1?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        widget = widgets.RadioSelect,
    )

    control_question_2 = models.IntegerField(
        label="Si en la ronda 1, mi compañero(a) y yo logramos 20 sumas correctas, cada uno ganará:",
        choices = [
            [1, "1000"],
            [2, "2000"],
            [3, "3000"],
        ],
        widget = widgets.RadioSelect,
    )

# ******************************************************************************************************************** #
# *** Validaciones
# ******************************************************************************************************************** #

    def control_question_1_error_message(self, value):
        if value != True:
            return 'Esta respuesta es incorrecta. Por favor, lea las instrucciones e intente de nuevo.'

    def control_question_2_error_message(self, value):
        if value != 1:
            return 'Recuerde que ganarán $50 por cada respuesta correcta que hayan dado juntos.'

# ******************************************************************************************************************** #
# *** Variables Consentimiento
# ******************************************************************************************************************** #
    num_temporal = models.IntegerField(label= "Por favor, ingrese el numero de identificación temporal que le llegó en el correo de invitación")
    accepts_data = models.BooleanField(
        label = "¿Autoriza el uso de los datos recolectados para futuros estudios?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        default=True)
    accepts_terms = models.BooleanField()

    def other_player(self):
        #self.get_others_in_group() -> Vector[<Player  2>, <Player  3>, <Player  4>]
        return self.get_others_in_group()[0]