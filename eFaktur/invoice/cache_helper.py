import re
from django.core.cache import cache
from .const import REGEX_WORD_PATTERN


# Cache key names can not contain control characters and spaces
def _clean_name(company):
    return re.sub(re.compile(REGEX_WORD_PATTERN), '', company)


def _join_names(first_company, second_company):
    return _clean_name(first_company) + "_" + _clean_name(second_company)


def _create_key_combinations(first_company, second_company):
    first_combination = _join_names(first_company, second_company)
    second_combination = _join_names(second_company, first_company)

    return first_combination, second_combination


def get_cache_frequency(first_company, second_company):
    """
    This function returns the frequency with which two companies have done business

    In case where we get a request where vendor and company names are exchanged
    we only want to store the combination and not permutations. 

    Example - CompanyA_CompanyB = CompanyB_CompanyA
    """
    cache_key_1, cache_key_2 = _create_key_combinations(
        first_company, second_company)

    count = cache.get(cache_key_1)
    if count is None:
        count = cache.get(cache_key_2)

    return count


def set_cache_frequency(first_company, second_company, count):
    cache_key = _join_names(first_company, second_company)
    cache.set(cache_key, count)


def delete_cache_frequency(first_company, second_company):
    cache_key_1, cache_key_2 = _create_key_combinations(
        first_company, second_company)

    if not cache.delete(cache_key_1):
        cache.delete(cache_key_2)
