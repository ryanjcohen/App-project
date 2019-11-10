from bs4 import BeautifulSoup, element

# Function to convert confluence media links in in_file to URL for actual locations in the export
def attachmentsub(in_file):
	soup = BeautifulSoup(in_file, "html.parser")

	for element in soup.find_all('p'):
		if(element['class']==[u'media-group']):
			container_id = element.a["data-linked-resource-container-id"]
			default_alias = element.a["data-linked-resource-default-alias"]
			resource_id = element.a["data-linked-resource-id"]
			data_mime_type = element.a["data-mime-type"].split("/")[1]

			new_href = "attachments/" + container_id + "/" + resource_id + "." + data_mime_type

			new_tag = soup.new_tag('a', href=new_href)
			new_tag.string = default_alias
			element.replace_with(new_tag)

	return str(soup).decode('utf-8')
