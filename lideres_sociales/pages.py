from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Consent(Page):
    form_model = 'player' 
    form_fields = ['num_temporal','genero', 'accepts_terms']

class Survey(Page):
    form_model = 'player'    
    form_fields = ['calidad_noticia', 'informacion_noticia', 'noticia_incompleta', 'noticia_credibilidad', 'noticia_tiempo',
    'noticia_calidad', 'noticia_imagenes', 'noticia_publico_general', 'noticia_informacion_importante',
    'noticia_informacion_importante_politicos', 'noticia_lenguaje', 'noticia_lideres_similar',
    'noticia_impactante', 'noticia_angustiante', 'noticia_violenta', 'lider_necesario', 'acuerdo_paz', 
    'gobierno_responsable_lideres', 'conflicto_armado_cesado', 'frase_identificado_1', 'frase_identificado_2', 'frase_identificado_3',
    'victima_responsable', 'siente_compasion', 'entristece_persona_solitaria', 'importancia_sentimientos',
    'muestras_afecto', 'molestan_personas_infelices', 'ponerse_nervioso', 'llorar_felicidad', 'involucrarse_emocionalmente', 
    'cancion_conmueve', 'perder_control_malas_noticias', 'gente_influencia_estado_animo', 'extrajeros_geniales', 'trabajador_social',
    'enfado_amigo', 'abrir_regalos', 'gente_solitaria_no_amistosa', 'llorar_molesta', 'canciones_feliz', 'sentimientos_personajes_novela',
    'enfado_maltrato', 'mantener_calma', 'amigo_problemas', 'risa_otro', 'llanto_divierte', 'decisiones_sin_sentimientos', 'gente_deprimida_alrededor', 
    'irritar_gente', 'disgusto_animal_sufriendo', 'involucrarse_libros_tonto', 'ancianos_indefensos', 'irrita_lagrimas_otros', 'involucrar_pelicula', 
    'mantener_calma_emocion', 'ninos_lloran_sin_razon']


class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = ['edad', 'ciudad', 'estrato', 'estado_civil', 'numero_hijos', 'identifica_cultura',
    'identifica_religion','nivel_estudios', 'tendencia_politica', 'disposicion_riesgos', 'victima_violencia_farc_eln', 
    'victima_violencia_auc_otros', 'victima_violencia_otros_delicuencia', 'victima_no_violencia', 'familia_victima_farc_eln', 
    'familia_victima_auc_otros', 'familia_victima_otros_delincuencia', 'familia_victima_no_violencia',
    'conseguir_esfuerzo','planes_termino', 'juego_suerte', 'propongo_aprender', 'mayores_logros', 'establecer_metas', 'competencia_excelencia',
    'salir_adelante', 'comparar_calificaciones', 'empeno_trabajo', 'alcanzar_objetivos', 'cumplir_tareas', 'obtener_resultados',
    'exito_esfuerzo','superar_desafios', 'confianza_tareas', 'tareas_excelencia', 'tareas_dificiles']

class Invitation(Page):
    form_model = 'player'

page_sequence = [Consent, Survey, SocioDemSurvey, Invitation]
