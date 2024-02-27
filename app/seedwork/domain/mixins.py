"""Mixins reusables parte del seedwork del proyecto

En este archivo usted encontrará las Mixins reusables parte del seedwork del proyecto

"""

from .rules import BusinessRule
from .exceptions import BusinessRuleException


class ValidateRulesMixin:
    @staticmethod
    def validate_rule(rule: BusinessRule):
        if not rule.is_valid():
            raise BusinessRuleException(rule)
