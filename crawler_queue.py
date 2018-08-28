from downloader import get_page 
from link_parser import link_parser
from robot_sitemaps import robot_filter
from link_parser import is_html


def crawler_queue(seed_url):
    frontier_q = seed_url
    visited_q = []
    black_lists = []
    html_page = []
    # while len(frontier_q) > 0:
    while len(html_page) < 50 and len(frontier_q) > 0:
        current_url = frontier_q[0]
        frontier_q = frontier_q[1:]
        
        if not robot_filter(current_url):
            black_lists.append(current_url)
            continue

        text = get_page(current_url)
        extracted_links = link_parser(current_url, text)
        
        # print(text)

        for link in extracted_links:
            if link not in frontier_q and link not in visited_q and link not in black_lists:
                print(link)
                frontier_q.append(link)
                if is_html(current_url):
                    html_page.append(current_url)
                    print(f'{len(html_page)} html {current_url}')
        
        visited_q.append(current_url)
        # print(f'visited queue length {len(visited_q)}')
        # print(f'frontier queue length {len(frontier_q)}')
        # break
    # print(frontier_q) 
    return frontier_q