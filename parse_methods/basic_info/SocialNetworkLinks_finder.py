import re


def find_links(text):
    links_array = ['instagram.com', 'facebook.com', 'linkedin.com', 'twitter.com', 'youtube.com', 'pinterest.com',
                   'snapchat.com', 't.me', 'soundcloud.com', 'vimeo.com', 'slideshare.net']
    founded_links = []
    for link in links_array:
        founded_link = re.search(r"\S*" + re.escape(link) + r"\S+", text)
        if founded_link:
            founded_links.append(founded_link.group())

    print(founded_links)
