# functions to extract the metadata
from babel.dates import get_month_names
import numpy as np

from regex import (
    re_source, re_year, re_authoryear, re_author, re_any_source,  # regex for author/year
    re_formatted_source,                                          # specific case for processes
    re_report, re_interview, re_personal_corr,                    # regex for type of source
    re_pedigree                                                   # regex for pedigree matrix
)


# custom values encountered as incorrect author detection
incorrect_author = set((v.lower() for v in get_month_names('wide', locale='en_US').values()))
incorrect_author.update((v.lower() for v in get_month_names('wide', locale='de').values()))
incorrect_author.update(
    ("in", "average", "annual report", "calculation", "data", "glo", "mpa, rna only, glo",
     "fakten", "zahlen", "ch", "update", "questionnaire", "questionnaires", "statistics")
)

# conversion from source type to ecospold2 format
source_type_to_int = {
    "article": 1,
    "chapters in anthology": 2,
    "separate publication": 3,
    "measurement on site": 4,
    "pral communication": 5,
    "personal written communication": 6,
    "questionnaries": 7
}

# valid entries for the pedigree matrix in ecospold2
pm_es2 = {
    "reliability",
    "completeness",
    "temporalCorrelation",
    "geographicalCorrelation",
    "furtherTechnologyCorrelation"
}


def extract_process_metadata(comment: str) -> dict:
    """
    Produce a metadata dict to update the process if the
    pre-processed data is missing.
    
    Returns
    -------
    A dict potentially containing any of the following entries:
    {
        'sourceType': int,
        'title': str,
        'firstAuthor': str,
        'additionalAuthors': str,
        'year': str
    }
    """
    raw_data = comment.replace("\\n", "\n")
    source = re_formatted_source.search(raw_data)

    if source:
        res_dict = source.groupdict()

        title = res_dict.get("title")

        if title is None:
            title = raw_data.split("\n")[0]

        st_string = res_dict.get("source_type")

        source_type = (
            0 if st_string is None else
            source_type_to_int.get(st_string.lower(), 0)
        )

        if source_type == 0 and "report" in raw_data.lower():
                source_type = 3

        return {
            "title": title,
            "year": res_dict.get("year"),
            "firstAuthor": res_dict.get("first_author"),
            "additionalAuthors": res_dict.get("other_authors"),
            "sourceType": source_type
        }

    return {}


def extract_exchange_metadata(comment: str) -> dict:
    """
    Produce a metadata dict to update the exchanges.

    Returns
    -------
    A dict potentially containing any of the following entries:
    {
        'pedigreeMatrix': {
            'reliability': str,
            'completeness': str,
            'temporalCorrelation': str,
            'geographicalCorrelation': str,
            'furtherTechnologicalCorrelation': str,
            'sampleSize': str,
            'basicUncertainty': str
        },
        'source': {
            'sourceType': int,
            'title': str,
            'firstAuthor': str,
            'additionalAuthors': str,
            'year': str
        }
    }
    """
    metadata = {}

    pedigree_list = [
        'reliability',
        'completeness',
        'temporalCorrelation',
        'geographicalCorrelation',
        'furtherTechnologicalCorrelation',
        'sampleSize',
        'basicUncertainty'
    ]

    # pedigree matrix
    pedigree = re_pedigree.search(comment)

    if pedigree:
        pedigree_text = pedigree.groupdict()["matrix"]
        splitter = ";" if ";" in pedigree_text else ","
        tpl = tuple(
            v.strip()
            for v in pedigree.groupdict()["matrix"].split(splitter)
            if v.strip()
        )

        metadata["pedigreeMatrix"] = {
            k: int(v) for k, v in zip(pedigree_list, tpl)
            if v.isdigit()
        }

    # process the comment to check for a source
    # we can only set one source so we keep the one with the
    # lowest, non-zero source type
    sources = []
    source_types = []

    start = 0

    for match in re_year.finditer(comment):
        source_type = 0
        end = match.span()[1]
        subpart = comment[start:end+7]

        start = max(end, 1)
        
        year = None
        author = None
        other_authors = None

        res = re_year.search(subpart)

        if res:
            year = res.group()

        # first try the author within the parenthesis with the year,
        # e.g. "(Smith, J. 2021)"
        res_author = re_authoryear.search(subpart)
        author_start = 0

        if res_author and res_author.groupdict()["author"]:
            author_start = res_author.span()[0]

            matched_str = res_author.groupdict()["author"].strip(",")

            splitter = "&" if "&" in matched_str else " and "
            author_split = matched_str.split(splitter)

            author = author_split[0].strip()

            if author.lower() in incorrect_author:
                author = None
            elif len(author_split) > 1:
                other_authors = author_split[1].strip()
        else:
            res_author = re_author.search(subpart)

            if res_author:
                author_start = res_author.span()[0]
                gdict = res_author.groupdict()
                first_auth = gdict["first"].strip(",")

                if first_auth.lower() not in incorrect_author:
                    author = first_auth.strip()

                    if "second" in gdict:
                        other_authors = gdict["second"]
                else:
                    author = None

                    res_author = re_any_source.search(subpart)

                    if res_author:
                        first_auth = res_author.group().strip()

                        if first_auth.lower() not in incorrect_author:
                            author = first_auth

        if not author and not year:
            continue

        if author:
            if "et al" in subpart or "&" in subpart:
                source_type = 1
            else:
                source_type = 3

        if re_interview.search(subpart):
            source_type = 7
        elif re_personal_corr.search(subpart):
            source_type = 6

        src = {
            "sourceType": source_type,
            "title": subpart[author_start:end+1]
        }

        if author:
            src["firstAuthor"] = author

        if other_authors:
            src["additionalAuthors"] = other_authors

        if year:
            src["year"] = year

        sources.append(src)
        source_types.append(source_type)

    if sources:
        best_id = 0
        best_st_val = np.inf

        for i, st in enumerate(source_types):
            if st > 0 and st < best_st_val:
                best_id = i
                best_st_val = st
            elif st > 0 and st == best_st_val:
                src1 = sources[best_id]
                src2 = sources[i]

                if len(src2) > len(src1):
                    best_id = i
                    best_st_val = st

        metadata["source"] = sources[best_id]

    return metadata
