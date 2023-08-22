def filter_unique_links(link_elements: list) -> list:
    filtered_links = []

    for link_element in link_elements:
        if (link := link_element.get_attribute("href")) not in filtered_links and link is not None and "mailto" not in link:
            filtered_links.append(link)

    return filtered_links
