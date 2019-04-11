# -*- coding: utf-8 -*-
import http.client, urllib.parse, json
from rango.keys import BING_TRIAL_KEY1
subscriptionKey = BING_TRIAL_KEY1
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"


def run_query(search):
    results = []
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    try:
        conn = http.client.HTTPSConnection(host)
        query = urllib.parse.quote(search)
        conn.request("GET", path + "?q=" + query, headers=headers)
        response = conn.getresponse()
        json_response = json.loads(response.read().decode("utf8"))
        # Loop through each page returned, populating out results list.
        for result in json_response['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet']})
    # Catch a URLError exception - something went wrong when connecting!
    except BaseException as e:
        print(("Error when querying the Bing API: ", e))
    return results


def main():
    s = input()
    print(run_query(s))


if __name__ == '__main__':
    main()
