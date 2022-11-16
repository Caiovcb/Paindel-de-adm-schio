from .models import Formularios
from rest_framework import serializers

class FormularioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formularios
        fields = [
            'id',
            'tipo',
            'cliente',
            'cnpj',
            'nome',
            'nr_contato',
            'email',
            'validacao_contrato',
            'validade_certificacao',
            'descricao'
        ]

