import io
import os
import re
from typing import List

from lxml import etree

from .base import HttpSession


def pull_plos(source: dict, project: str, path: str) -> List[str]:
    """
    Pull a plos article.

    Fetches the XML of the article from https://journals.plos.org
    and then walks the XML tree, downloading any graphic media.
    """
    assert "article" in source, "plos source must have an article"

    doi = source["article"]
    m = re.match(r"^10\.1371\/journal\.([a-z]+)\.(\d+)$", doi)
    assert m is not None, "unknown plos article format"

    journals = dict(
        pbio="plosbiology",
        pcbi="ploscompbiol",
        pgen="plosgenetics",
        pmed="plosmedicine",
        pntd="plosntds",
        pone="plosone",
        ppat="plospathogens",
    )

    assert m.group(1) in journals, "unknown plos journal: {}".format(m.group(1))

    code = m.group(1)
    journal = journals[code]

    url = "https://journals.plos.org/{}/article/file?id={}&type=manuscript".format(
        journal, doi
    )

    folder, xml = os.path.split(path)
    folder = os.path.join(project, folder)

    session = HttpSession()
    response = session.fetch_url(url)
    tree = etree.parse(io.BytesIO(response.content))
    root = tree.getroot()
    xlinkns = "http://www.w3.org/1999/xlink"
    os.makedirs(os.path.join(project, "{}.media".format(path)), exist_ok=True)

    # Get the figures and rewrite hrefs
    for graphic in root.iterdescendants(tag="graphic"):
        href = graphic.attrib.get("{%s}href" % xlinkns)

        if not href.startswith("info:doi/{}".format(doi)):
            continue

        url = "https://journals.plos.org/{}/article/".format(journal)
        id = href.split(".").pop()
        if id.startswith("e"):  # Equation
            url += "file?id=info:doi/{}.{}&type=thumbnail".format(doi, id)
        else:  # Everything else
            url += "figure?image?id={}.{}&size=medium".format(doi, id)

        filename = "{}.png".format(id)
        new_href = "{}.media/{}".format(xml, filename)
        graphic.attrib["{%s}href" % xlinkns] = new_href
        graphic.attrib["mime-subtype"] = "png"
        session.pull(url, os.path.join(folder, new_href))

    tree.write(open(os.path.join(folder, xml), "wb"))

    return [path]
