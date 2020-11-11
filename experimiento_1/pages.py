from datetime import datetime, timedelta

from ._builtin import Page, WaitPage


class MyPage(Page):
    form_model = 'player'


class ResultsWaitPage(WaitPage):
    pass


class EncuestaSocioEconomica(Page):
    template_name = 'experimiento_1/encuesta_economica.html'
    form_model = 'player'
    form_fields = ['survey']


class Session1(Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_1']
    document = 'experimiento_1/session_1.pdf'
    text_info = "Las siguientes páginas hacen parte del libro El crimen como oficio: ensayos sobre economía del crimen en Colombia (2007), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session1, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session2(Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_2']
    document = 'experimiento_1/session_2.pdf'

    text_info = "Las siguientes páginas hacen parte del libro Informe de la desigualdad global (2018), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session2, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session3(Page):
    template_name = 'experimiento_1/session_1.html'
    form_model = 'player'
    form_fields = ['file_session_3']
    document = 'experimiento_1/session_3.pdf'
    text_info = "Las siguientes páginas hacen parte del libro Informe de la desigualdad global (2018), y es necesario para nosotros transcribir la información contenida en el documento. El tiempo aproximado del siguiente trabajo es de 15 min, por favor transcriba la información en el espacio disponible. "

    def get_context_data(self, *args, **kwargs):
        context = super(Session3, self).get_context_data(*args, **kwargs)
        context['text_info'] = self.text_info
        context['document_url'] = self.document
        return context


class Session4(Page):
    template_name = 'experimiento_1/session_2.html'
    form_model = 'player'
    form_fields = ['monto_session_2']

class IntermedioSession(Page):
    template_name = 'experimiento_1/intermedio.html'
    form_model = 'player'
    form_fields = ['money_decision', 'percentage_saved']

    def post(self, *args, **kwargs):
        self.player.intermedio = self.player.intermedio + 1
        self.player.save()
        return super(IntermedioSession, self).post(*args, **kwargs)


class SevenDaysWaitPage(Page):
    template_name = 'experimiento_1/wait_page.html'

    def get_context_data(self, *args, **kwargs):
        day_available = self.player.updated_at.replace(hour=0, tzinfo=None) + timedelta(days=7)
        today = datetime.now()
        context = super(SevenDaysWaitPage, self).get_context_data(*args, **kwargs)
        context['day_available'] = day_available
        context['can_access'] = today > day_available
        return context


page_sequence = [
    MyPage,
    IntermedioSession,
    Session1,
    IntermedioSession,
    #SevenDaysWaitPage,
    Session2,
    IntermedioSession,
    #SevenDaysWaitPage,
    Session2,
    EncuestaSocioEconomica,
    Session4,
]
