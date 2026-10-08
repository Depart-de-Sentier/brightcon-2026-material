# regex.py
# regular expressions to extract data from an Ecospold1 database

import re


punct_pattern = r"[\s,;:.\n\r()\"/-]"
re_punct = re.compile(punct_pattern)
re_strip = re.compile(rf"(?:^{punct_pattern}+|{punct_pattern}+$)")
re_strip_title = re.compile(r"(?:^[\s,;:.\n\r)\"/-]+|[\s,;:.\r\n(\"/-]+$)")

def strip_title(s: str) -> str:
    if "(" not in s:
        s = s.strip(")")

    return re_strip_title.sub("", s)

# detecting potential sources using a year or "et al"
year_base = r"(19\d{2}|2[012]\d{2})"
year_pattern = rf"[^\d]{year_base}([^\w]|$)"  # something not a digit, then 4 digits, then something that's not a word or digit
re_source = re.compile(rf"{year_pattern}|et al", flags=re.M)
re_year = re.compile(rf"{year_pattern}", flags=re.M)

# detecting the authors (using capitalized words coming before a year or et al)
and_pattern = r"(?:&|et|and|und|y)"
author_pattern = r"[A-Z][a-z]+(-[A-z][a-z]+)?(, [A-Z]+\.?)?"
author_pattern = r"[A-Z][\w-]+(, [A-Z]+\.?)?[\s&,]?"

re_authoryear = re.compile(
    rf"\((?P<author>([A-Z]\w*(,? [A-Z]+?\.?)*[\s&,-]*)+),?\s+{year_base}\)")

re_author = re.compile(
    rf"(?P<first>({author_pattern})+)(?:,?\s+{and_pattern}\s+)?( (guidebook|statistics?|data|AG)\s?)?"
    rf"(?P<second>{author_pattern})?(?=,?\s?({year_pattern}(\W|$)|et al))",
    flags=re.M
)

# detecting data from standardized format
p_title = r"([^\n]+\s\d+\.?\s?|^(\d+\.\s)?)(?P<title>[^;\n]+)"
p_type = r"^Type:\s+(?P<type>[^\n]+)$"
p_first_author = r"^First author:\s+(?P<first_author>[^\n]+)$"
p_other_authors = r"^Other authors:\s+(?P<other_authors>[^\n]+)$"
p_year = rf"^Year:\s+(?P<year>{year_base})$"
p_publisher = r"^Publisher:\s+(?P<publisher>[^\n]+)$"
re_formatted_source = re.compile(rf"{p_title}.+?{p_type}.+?{p_first_author}.+?({p_other_authors}.*?)?{p_year}.+?({p_publisher}.*?)?", flags=re.M|re.DOTALL)

# trying to detect other types of sources if detecting authors failed
re_any_source = re.compile(rf"\s?[A-Z][^;\d.]+(?=,?[\s]+\(?({year_pattern}|et al))", flags=re.M)

# detecting specific source type
re_report = re.compile("report|thesis", flags=re.IGNORECASE)
re_interview = re.compile("questionn|interview", flags=re.IGNORECASE)
re_personal_corr = re.compile(r"(personal (correspondence|communication)|persönlicher mitteilung)(?:\swith|,\s+)", flags=re.M|re.IGNORECASE)

# detecting the pedigree matrix
base_pm_pattern = r"(\d|[nN]\.?[aA]\.?)\s?"
first_patterns = rf"{base_pm_pattern}[,;]\s?"
last_pattern = rf"{base_pm_pattern}[,;]?\s?"
bu_pattern = r"([,;]?BU:?(?P<base_uncertainty>\d\.?\d?))?"
re_pedigree = re.compile(rf"[({{\[]?(?P<matrix>({first_patterns}){{3,5}}({last_pattern})){bu_pattern}[)}}\]]?", flags=re.M)
