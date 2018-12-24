import os

from requests_html import HTMLSession
lang_map = ["php"]

def get_url(lang):
    return "https://" + lang + ".happycodings.com"


def write_sample(response, lang, sample):
    code_elem_list = response.html.find('code')
    if code_elem_list:
        elem = code_elem_list[0].full_text
        with open("./resources/" + lang + "/" + str(sample) + ".txt", "w") as f:
            f.write(elem)
        return True
    else:
        return False


if __name__=="__main__":
    sample = 21439
    for lang in lang_map:
        os.mkdir("./resources/" + lang)
    sess = HTMLSession()
    for lang in lang_map:
        r = sess.get(get_url(lang))
        refs = r.html.find('a')
        for ref in refs:
            sub_url = ref.attrs.get('href')
            if lang in sub_url:
                if lang not in ('csharp', 'javascript'):
                    while True:
                        i = 1
                        url_to_go = sub_url + "code" + str(i) + ".html"
                        r = sess.get(url_to_go)
                        if r.status_code != 200:
                            break
                        if write_sample(r, lang, sample):
                            sample += 1
                        i += 1
                        print(f"processed: {sample}")
                else:
                    r = sess.get(sub_url)
                    if write_sample(r, lang, sample):
                        sample += 1
                    print(f"processed: {sample}")
            print(f"sub_url {sub_url} processed")
    print("hurray")

