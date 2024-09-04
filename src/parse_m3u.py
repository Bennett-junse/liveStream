import os

def parse_m3u(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    channels = []
    channel = {}
    for line in lines:
        line = line.strip()
        if line.startswith('#EXTINF:'):
            channel_info = line.split(',', 1)
            channel['name'] = channel_info[1]
        elif line.startswith('http'):
            channel['url'] = line
            channels.append(channel)
            channel = {}
    return channels

def generate_html(channels, output_file):
    html_content = '<html><head><title>IPTV Channels</title></head><body>'
    html_content += '<h1>IPTV Channels</h1><ul>'
    
    for channel in channels:
        html_content += f'<li><a href="{channel["url"]}">{channel["name"]}</a></li>'
    
    html_content += '</ul></body></html>'
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    m3u_files = ['file1.m3u', 'file2.m3u']
    output_files = ['file1.html', 'file2.html']
    
    for m3u_file, output_file in zip(m3u_files, output_files):
        channels = parse_m3u(m3u_file)
        generate_html(channels, output_file)