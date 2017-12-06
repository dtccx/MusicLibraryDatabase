from django.utils.translation import ugettext_lazy as _


class EnumChoice(object):

    def __init__(self, *args):
        for x in args:
            if not isinstance(x, tuple) or len(x) != 2:
                raise Exception("Args Error")
        self.pairs = args
        self._pairs = dict(self.pairs)
        self._rpairs = dict([(k, v) for k, v in self.pairs])

    def __getattr__(self, item):
        if self._rpairs.has_key(item):
            return self._rpairs[item]
        return None

    def choice(self):
        return self.pairs

    def filter_choice(self):
        res = [('', 'All')]
        res.extend(list(self.pairs))
        return res

    def to_dict(self):
        if not self.pairs or len(self.pairs) == 0:
            return {}
        if self._pairs:
            return self._pairs
        self._pairs = dict(self.pairs)
        return self._pairs

    def keys(self):
        return [k for k, v in self.pairs]

    def values(self):
        return [v for k, v in self.pairs]

    def get_display_name(self, key):
        if not self.pairs:
            return None
        return self.to_dict().get(key, None)

RATESCORE = EnumChoice(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

SOURCETYPE = EnumChoice(
    (0, 'P'),
    (1, 'A'),
    (2, 'NULL')
)
