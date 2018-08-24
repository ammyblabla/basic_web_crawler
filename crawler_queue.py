from downloader import get_page 
from link_parser import link_parser

def crawler_queue(seed_url):
    frontier_q = seed_url
    visited_q = []
    while len(frontier_q) > 0:
        current_url = frontier_q[0]
        frontier_q = frontier_q[1:]
        visited_q.append(current_url)

        text = get_page(current_url)
        extracted_links = link_parser(text)
        # print(text)

        for link in extracted_links:
            if link not in frontier_q and link not in visited_q:
                frontier_q.append(link)
    print(visited_q)

# crawler_queue(['http://www.ku.ac.th/web2012/'])