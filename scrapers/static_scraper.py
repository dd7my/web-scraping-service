# import requests
# from scrapling import Adaptor

# def scrape_titles(url, selector):
#     try:
#         # Removed verify=False for better security in production
#         response = requests.get(url, timeout=10)
#         page = Adaptor(response.text, url=url)
#         elements = page.css(selector)
#         data = [el.text.strip() for el in elements if el.text]
#         return {'success': True, 'data': data, 'count': len(data)}
#     except Exception as e:
#         return {'success': False, 'error': str(e)}

import requests
from scrapling import Adaptor


def scrape_data(url, selectors):
    try:
        response = requests.get(url, timeout=10)
        page = Adaptor(response.text, url=url)

        results = {}

        for name, config in selectors.items():
            selector = config.get("selector")
            attr = config.get("attr", "text")

            elements = page.css(selector)

            values = []

            for el in elements:
                if attr == "text":
                    if el.text:
                        values.append(el.text.strip())

                elif attr == "html":
                    values.append(el.html)

                else:
                    values.append(el.attrib.get(attr))

            results[name] = [v for v in values if v]

        return {
            "success": True,
            "data": results,
            "counts": {k: len(v) for k, v in results.items()}
        }

    except Exception as e:
        return {"success": False, "error": str(e)}