from django.apps import AppConfig


from search_engine.meili_customize.config import Config, create_documents, hanja_preprocessor


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        """초기화 테스트"""
        conf = Config()
        hanjas = hanja_preprocessor()
        documents = create_documents(hanjas)
        conf.add_docs(documents)
        conf.add_filter()
