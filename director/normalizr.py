from rest_framework.serializers import ListSerializer


class NormalizrSerializer(ListSerializer):
    entity_plural = None

    @property
    def data(self):
        if not self.entity_plural:
            raise TypeError('entity_plural must be set')

        data = super(NormalizrSerializer, self).data

        result = []
        entities = {
            self.entity_plural: {}
        }

        for item in data:
            entities[self.entity_plural][str(item['id'])] = item
            result.append(str(item['id']))

        return {
            'result': result,
            'entities': entities
        }
