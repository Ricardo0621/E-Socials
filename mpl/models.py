from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from mpl.config import *
import random
from random import randrange


author = 'Ricardo Diaz'

doc = """
Experimento 1.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:

            n = Constants.num_choices
            for p in self.get_players():

                # create list of lottery indices
                # ----------------------------------------------------------------------------------------------------
                indices = [j for j in range(1, n)]
                indices.append(n) if Constants.certain_choice else None

                # create list of probabilities
                # ----------------------------------------------------------------------------------------------------
                if Constants.percentage:
                    probabilities = [
                        # "{0:.2f}".format((k-1) / (n-1) * 100) + "%"
                        (n-k)
                        for k in indices
                    ]
                else:
                    probabilities = [
                        str(k-1) + "/" + str(n-1)
                        for k in indices
                    ]

                # create list corresponding to form_field variables including all choices
                # ----------------------------------------------------------------------------------------------------
                form_fields = ['choice_' + str(k) for k in indices]
                #form_fields = ['choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5', 'choice_6', 'choice_7', 'choice_8', 'choice_9', 'choice_10', 'choice_11']

                # create list of choices
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_choices'] = list(
                    zip(indices, form_fields, probabilities)
                )
                #p.participant.vars= [(1, 'choice_1', '0/10'), (2, 'choice_2', '1/10'), (3, 'choice_3', '2/10'), (4, 'choice_4', '3/10'), (5, 'choice_5', '4/10'), (6, 'choice_6', '5/10'), (7, 'choice_7', '6/10'), (8, 'choice_8', '7/10'), (9, 'choice_9', '8/10'), (10, 'choice_10', '9/10'), (11, 'choice_11', '10/10')]
                # randomly determine index/choice of binary decision to pay
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_index_to_pay'] = random.choice(indices) #Return a random indice 1-11. It0s the election that will pay the person. That was the winner
                p.participant.vars['mpl_choice_to_pay'] = 'choice_' + str(p.participant.vars['mpl_index_to_pay']) #-> choice_(random number). Same numer of the last line
                # randomize order of lotteries if <random_order = True>
                # ----------------------------------------------------------------------------------------------------
                if Constants.random_order:
                    random.shuffle(p.participant.vars['mpl_choices']) #Randomize choices dict
                # initiate list for choices made
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['mpl_choices_made'] = [None for j in range(1, n + 1)]
                #p.participant.vars['mpl_choices_made'] = [None, None, None, None, None, None, None, None, None, None, None]
            # generate random switching point for PlayerBot in tests.py
            # --------------------------------------------------------------------------------------------------------
            for participant in self.session.get_participants():
                participant.vars['mpl_switching_point'] = random.randint(1, n) #Only used for testing


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if Constants.certain_choice: #Useless
        for j in range(1, Constants.num_choices + 1):
            locals()['choice_' + str(j)] = models.StringField()
        del j
    else:
        for j in range(1, Constants.num_choices):
            locals()['choice_' + str(j)] = models.StringField()
        del j

    random_draw = models.IntegerField()
    choice_to_pay = models.StringField()
    option_to_pay = models.StringField()
    inconsistent = models.IntegerField()
    switching_row = models.IntegerField()
    name = models.StringField(label= "Nombre Completo")
    id_cc = models.IntegerField(label="Cédula de Ciudadanía (Sin puntos)")
    accepts_data = models.BooleanField(
        label = "¿Autoriza el uso de los datos recolectados para futuros estudios?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ],
        default=True)
    accepts_terms = models.BooleanField()
    monto = models.IntegerField(label = 
    "Por favor, indica el monto que invertirás en el activo de riesgo (sin puntos o comas)", min=0, max=10000)
    nombre_entidad = models.StringField(label= "¿Cuál es el nombre de la entidad en la que usted trabaja?")
    tiempo_entidad = models.IntegerField(label="¿Cuánto tiempo (en años) lleva trabajando en esta entidad?")
    tipo_contrato =  models.StringField(
        label="Por favor, seleccione cuál es el tipo de contrato que lo vincula a esta entidad",
        choices = [
            ["Contrato a término indefinido", "Contrato a término indefinido"],
            ["Contrato a término fijo", "Contrato a término fijo"],
            ["Contrato de obra o labor", "Contrato de obra o labor"],
            ["Contrato por prestación de servicios", "Contrato por prestación de servicios"],
            ["Contrato a término fijo", "Contrato a término fijo"],
        ]
    )
    horas_semanales = models.IntegerField(label="Cuántas horas a la semana trabaja normalmente en este trabajo?")    
    rango_pago = models.StringField(
        label="¿Puede decirme en cuál de los siguientes rangos está el ingreso que usted gana al mes por su trabajo?",
        choices = [
            ["Menos de 205.000", "Menos de 205.000"],
            ["Entre 205.000 y 325.000", "Entre 205.000 y 325.000"],
            ["Entre 325.0001 y 440.000", "Entre 325.0001 y 440.000"],
            ["Entre 440.001 y 565.000", "Entre 440.001 y 565.000"],
            ["Entre 650.001 y 710.000", "Entre 650.001 y 710.000"],
            ["Entre 710.001 y 750.000", "Entre 710.001 y 750.000"],
            ["Entre 810.001 y 915.000", "Entre 810.001 y 915.000"],
            ["Entre 915.001 y 1.000.00", "Entre 915.001 y 1.000.00"],
            ["Entre 1.000.001 y 1.250.000", "Entre 1.000.001 y 1.250.000"],
            ["Entre 1.250.001 y 1.365.000", "Entre 1.250.001 y 1.365.000"],
            ["Entre 1.365.001 y 1.600.000", "Entre 1.365.001 y 1.600.000"],
            ["Entre 1.600.001 y 2.000.000", "Entre 1.600.001 y 2.000.000"],
            ["Entre 2.000.001 y 3.150.000", "Entre 2.000.001 y 3.150.000"],
            ["Más de 3.150.000", "Más de 3.150.000"],
        ]
    )
    satisfecho_trabajo_actual = models.BooleanField(
        label = "¿Con su trabajo actual?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    satisfecho_beneficios = models.BooleanField(
        label = "¿Con los beneficios y las prestaciones que recibe?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    satisfecho_jornada = models.BooleanField(
        label = "¿Con su jornada laboral actual?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    conforme_contrato = models.BooleanField(
        label = "¿Está conforme con su tipo de contrato?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    empleo_estable = models.BooleanField(
        label = "¿Considera que su empleo actual es estable?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    contrato_credito_vivienda = models.BooleanField(
        label = "¿Su tipo de contrato actual le permite acceder a créditos de vivienda?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    contrato_credito_carro = models.BooleanField(
        label = "¿Su tipo de contrato actual le permite acceder a créditos para carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    contrato_opciones =  models.StringField(
        label="De acuerdo con su contrato actual, usted recibe o tiene derecho a algunas de las siguientes opciones:",
        choices = [
            ["Prima de navidad", "Prima de navidad"],
            ["Cesantías ", "Cesantías "],
            ["Vacaciones con sueldo", "Vacaciones con sueldo"],
        ]
    )
    aporte_vejez = models.StringField(
        label="¿Qué está haciendo usted actualmente para mantener económicamente en su vejez?",
        choices = [
            ["Aportar en un fondo de pensiones obligatorias", "Aportar en un fondo de pensiones obligatorias"],
            ["Aportar en un fondo de pensiones voluntarias", "Aportar en un fonde de pensiones voluntarias"],
            ["Ahorrando", "Ahorrando"],
            ["Haciendo inversiones", "Haciendo inversiones"],
            ["Pagando un seguro por su cuenta", "Pagando un seguro por su cuenta"],
            ["Preparando a sus hijos para que pueda mantenerlo en su vejez", "Preparando a sus hijos para que pueda mantenerlo en su vejez"],
            ["Otro", "Otro"],
            ["Nada", "Nada"],
        ]
    )
    cambiar_empresa = models.BooleanField(
        label = "¿Desearía trabajar en otra organización/empresa?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    cambiar_trabajo = models.BooleanField(
        label = "¿Desea cambiar el tipo de trabajo que realiza actualmente?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    mejorar_capacidades = models.BooleanField(
        label = "¿Para mejorar la utilización de sus capacidades o formación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    mejorar_ingresos = models.BooleanField(
        label = "¿Desea mejorar sus ingresos?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    trabajar_menos = models.BooleanField(
        label = "¿Desea trabajar menos horas?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    trabajo_temporal = models.BooleanField(
        label = "¿Porque el trabajo actual es temporal?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    trabajo_estable = models.BooleanField(
        label = "¿Porque su trabajo no es estable?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    crecimiento_profesional = models.BooleanField(
        label = "¿Porque no ve posibilidades de crecimiento profesional?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    dinero_compra_vivienda = models.BooleanField(
        label = "¿Porque con el dinero que gana no puede realizar planes de compra de vivienda, carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    contrato_compra_vivienda = models.BooleanField(
        label = "¿Porque su tipo de contrato no le permite realizar planes de compra de vivienda, carro o educación?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    problemas_companeros = models.BooleanField(
        label = "¿Problemas con sus compañeros de trabajo?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    problemas_jefe = models.BooleanField(
        label = "¿Problemas con su jefe?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    labor_desempenada = models.BooleanField(
        label = "Le gusta la labor que desempeña?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    esfuerzo_fisico = models.BooleanField(
        label = "¿Su trabajo actual exige mucho esfuerzo físico o mental?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    problemas_ambientales = models.BooleanField(
        label = "¿Problemas ambientales (aire, olores, ruidos, temperatura, etc.)?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    otro_problema = models.BooleanField(
        label = "¿Otro?",
        choices = [
            [True, "Sí"],
            [False, "No"],
        ]
    )
    # set player's payoff
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_payoffs(self):

        # random draw to determine whether to pay the "high" or "low" outcome of the randomly picked lottery
        # Randomnly decides wheter to pay the high or low value
        # ------------------------------------------------------------------------------------------------------------
        self.random_draw = randrange(1, len(self.participant.vars['mpl_choices'])) #Selects rando number 1-11
        # set <choice_to_pay> to participant.var['choice_to_pay'] determined creating_session
        # ------------------------------------------------------------------------------------------------------------
        self.choice_to_pay = self.participant.vars['mpl_choice_to_pay'] 
        #self.choice_to_pay = choice_(random number 1-11). Here the choce is selected

        # elicit whether lottery "A" or "B" was chosen for the respective choice
        # ------------------------------------------------------------------------------------------------------------
        self.option_to_pay = getattr(self, self.choice_to_pay)
        #self.option_to_pay = A or B. Here the lottery is selected

        # set player's payoff
        # ------------------------------------------------------------------------------------------------------------
        print("Choice to play model" + str(self.choice_to_pay))
        print(self.option_to_pay)
        print(self.random_draw)
        print(self.participant.vars['mpl_index_to_pay'])
        if self.option_to_pay == 'A': #A Toma la opción a ganar y la compara con con un número aleatorio. Si es menor escoge el mayor pago
            if self.random_draw <= self.participant.vars['mpl_index_to_pay']:
                self.payoff = Constants.lottery_a_hi
            else:
                self.payoff = Constants.lottery_a_lo
        else:
            if self.random_draw <= self.participant.vars['mpl_index_to_pay']:
                self.payoff = Constants.lottery_b_hi
            else:
                self.payoff = Constants.lottery_b_lo

        # set payoff as global variable
        # ------------------------------------------------------------------------------------------------------------
        self.participant.vars['mpl_payoff'] = self.payoff

    # determine consistency
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_consistency(self):

        n = Constants.num_choices

        # replace A's by 1's and B's by 0's
        self.participant.vars['mpl_choices_made'] = [
            1 if j == 'A' else 0 for j in self.participant.vars['mpl_choices_made']
        ]
        print("Choices Model" + str(self.participant.vars['mpl_choices_made']))
        # check for multiple switching behavior
        for j in range(1, n):
            choices = self.participant.vars['mpl_choices_made']
            self.inconsistent = 1 if choices[j] > choices[j - 1] else 0
            if self.inconsistent == 1:
                break

    # determine switching row
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_switching_row(self):

        # set switching point to row number of first 'B' choice
        if self.inconsistent == 0:
            self.switching_row = sum(self.participant.vars['mpl_choices_made']) + 1
