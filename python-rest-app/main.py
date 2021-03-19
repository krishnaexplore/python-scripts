import http_bin_adaptor


response = http_bin_adaptor.get_response()
print(response.json())


resp = http_bin_adaptor.post_response("Take out trash")
print(resp.json())