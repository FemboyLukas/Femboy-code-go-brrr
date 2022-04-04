from requests import get

def save_image(url, image_name=None, debug=False):
    if url[-1]=='/':
        url = url[:-1]
    if image_name == None:
        image_name = url[url.rfind('/')+1:]
    
    with open(image_name, 'wb') as handle:
        response = get(url, stream=True)
        
        if not response.ok and debug:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
